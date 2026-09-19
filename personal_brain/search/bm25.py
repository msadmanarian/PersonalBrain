import math
from typing import List, Dict, Tuple
from personal_brain.search.tokenizer import tokenize

class BM25Ranker:
    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.corpus_size = 0
        self.avg_doc_len = 0.0
        self.doc_lens = {}
        self.doc_term_freqs = {}
        self.idf = {}

    def fit(self, docs: Dict[str, str]):
        self.corpus_size = len(docs)
        if self.corpus_size == 0:
            return
        total_len = 0
        df = {}
        for doc_id, text in docs.items():
            tokens = tokenize(text)
            length = len(tokens)
            self.doc_lens[doc_id] = length
            total_len += length
            tf = {}
            for t in tokens:
                tf[t] = tf.get(t, 0) + 1
            self.doc_term_freqs[doc_id] = tf
            for t in set(tokens):
                df[t] = df.get(t, 0) + 1
        self.avg_doc_len = total_len / self.corpus_size
        for term, freq in df.items():
            # Robertson-Sparck Jones IDF
            self.idf[term] = math.log((self.corpus_size - freq + 0.5) / (freq + 0.5) + 1.0)

    def score(self, query: str, top_k: int = 10) -> List[Tuple[str, float]]:
        q_tokens = tokenize(query)
        scores = {}
        for doc_id, tf in self.doc_term_freqs.items():
            score = 0.0
            doc_len = self.doc_lens[doc_id]
            for t in q_tokens:
                if t in tf:
                    t_idf = self.idf.get(t, 0.0)
                    t_freq = tf[t]
                    numerator = t_freq * (self.k1 + 1.0)
                    denominator = t_freq + self.k1 * (1.0 - self.b + self.b * (doc_len / (self.avg_doc_len or 1.0)))
                    score += t_idf * (numerator / denominator)
            if score > 0.0:
                scores[doc_id] = round(score, 4)
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]
