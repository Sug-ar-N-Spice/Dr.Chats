from sentence_transformers import SentenceTransformer
import numpy as np

class SlidingWindowSelector:
    def __init__(self, model_name='all-MiniLM-L6-v2', window_size=1000, stride=500, batch_size=32):
        self.model = SentenceTransformer(model_name)
        self.contexts = []
        self.embeddings = []
        self.window_size = window_size
        self.stride = stride
        self.batch_size = batch_size

    def fit(self, contexts):
        for i in range(0, len(contexts), self.stride):
            window = contexts[i:i+self.window_size]
            self.contexts.extend(window)

            # Process embeddings in batches
            for j in range(0, len(window), self.batch_size):
                batch = window[j:j+self.batch_size]
                batch_embeddings = self.model.encode(batch)
                self.embeddings.extend(batch_embeddings)

        self.embeddings = np.array(self.embeddings)

    def get_most_relevant_context(self, question, top_n=3):
        question_embedding = self.model.encode([question])

        # Calculate similarities in batches
        all_similarities = []
        for i in range(0, len(self.embeddings), self.batch_size):
            batch_embeddings = self.embeddings[i:i+self.batch_size]
            batch_similarities = np.dot(batch_embeddings, question_embedding.T).squeeze()
            all_similarities.extend(batch_similarities)

        top_indices = np.argsort(all_similarities)[-top_n:][::-1]
        return [self.contexts[i] for i in top_indices]
