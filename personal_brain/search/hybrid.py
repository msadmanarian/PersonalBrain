from typing import List, Dict, Tuple
from personal_brain.search.bm25 import BM25Ranker
from personal_brain.search.tfidf import TFIDFVectorizer
from personal_brain.search.similarity import cosine_similarity
from personal_brain.search.tokenizer import tokenize

class HybridSearchEngine:
    def __init__(self, alpha: float = 0.6):
        self.alpha = alpha # Weight for BM25 vs Vector
        self.bm25 = BM25Ranker()
        self.tfidf = TFIDFVectorizer()
        self.vectors = {}

    def index(self, docs: Dict[str, str]):
        self.bm25.fit(docs)
        self.vectors = self.tfidf.fit_transform(docs)

    def search(self, query: str, top_k: int = 10) -> List[Tuple[str, float]]:
        bm25_results = dict(self.bm25.score(query, top_k=top_k * 2))
        q_tokens = tokenize(query)
        q_vec = {}
        for t in q_tokens:
            if t in self.tfidf.idf:
                q_vec[t] = self.tfidf.idf[t]
        # Normalize query vector
        norm = math.sqrt(sum(v*v for v in q_vec.values())) or 1.0
        q_vec = {t: v / norm for t, v in q_vec.items()}
        scores = {}
        all_ids = set(bm25_results.keys()).union(self.vectors.keys())
        max_bm25 = max(bm25_results.values(), default=1.0) or 1.0
        for doc_id in all_ids:
            bm25_norm = bm25_results.get(doc_id, 0.0) / max_bm25
            vec_sim = cosine_similarity(q_vec, self.vectors.get(doc_id, {}))
            score = (self.alpha * bm25_norm) + ((1.0 - self.alpha) * vec_sim)
            if score > 0.05:
                scores[doc_id] = round(score, 4)
        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return ranked[:top_k]
