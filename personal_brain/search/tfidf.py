import math
from typing import Dict, List
from personal_brain.search.tokenizer import tokenize

class TFIDFVectorizer:
    def __init__(self):
        self.vocabulary = {}
        self.idf = {}

    def fit_transform(self, docs: Dict[str, str]) -> Dict[str, Dict[str, float]]:
        df = {}
        n = len(docs)
        for doc_id, text in docs.items():
            tokens = set(tokenize(text))
            for t in tokens:
                df[t] = df.get(t, 0) + 1
        for t, freq in df.items():
            self.idf[t] = math.log((n + 1.0) / (freq + 1.0)) + 1.0
        vectors = {}
        for doc_id, text in docs.items():
            tokens = tokenize(text)
            tf = {}
            for t in tokens:
                tf[t] = tf.get(t, 0) + 1
            vec = {}
            norm = 0.0
            for t, count in tf.items():
                val = count * self.idf[t]
                vec[t] = val
                norm += val * val
            norm = math.sqrt(norm) or 1.0
            vectors[doc_id] = {t: val / norm for t, val in vec.items()}
        return vectors
