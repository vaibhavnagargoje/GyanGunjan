from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from search.models import PDFDocument
import numpy as np

class SearchEngine:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        self.documents = []
        self._initialize()

    def _initialize(self):
        self.documents = list(PDFDocument.objects.filter(processed=True))
        if self.documents:
            corpus = [doc.content for doc in self.documents]
            self.tfidf_matrix = self.vectorizer.fit_transform(corpus)

    def search(self, query, top_n=10):
        if not self.documents:
            return []
            
        query_vec = self.vectorizer.transform([query])
        cosine_similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        sorted_indices = np.argsort(cosine_similarities)[::-1]
        
        results = []
        for idx in sorted_indices:
            if cosine_similarities[idx] > 0:
                results.append({
                    'document': self.documents[idx],
                    'score': cosine_similarities[idx]
                })
            if len(results) >= top_n:
                break
                
        return results