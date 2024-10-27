from MedDataPreprocessor import MedDataPreprocessor
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from SlidingWindowSelector import SlidingWindowSelector

class DrChatbot:
    def __init__(self, qa_model="microsoft/BioGPT", window_size=1000, stride=500, batch_size=32):
        self.preprocessor = MedDataPreprocessor()
        self.qa_tokenizer = AutoTokenizer.from_pretrained(qa_model)
        self.qa_model = AutoModelForCausalLM.from_pretrained(qa_model)
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.device = torch.device(device=device)
        print (f"Using device: {self.device}")
        self.qa_model.to(self.device)
        self.context_selector = SlidingWindowSelector(window_size=window_size, stride=stride, batch_size=batch_size)

    def preprocess_data(self, df):
        processed_df = self.preprocessor.preprocess_dataframe(df)
        return processed_df['combined_text'].tolist()

    def fit_context_selector(self, all_contexts):
        self.context_selector.fit(all_contexts)

    def answer_question(self, question):
        relevant_contexts = self.context_selector.get_most_relevant_context(question, top_n=3)
        combined_context = " ".join(relevant_contexts)

        prompt = f"Based on the following medical information:\n{combined_context}\n\nQuestion: {question}\nAnswer:"
        inputs = self.qa_tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512).to(self.device)

        input_length = inputs["input_ids"].shape[1]
        max_new_tokens = min(100, 1024 - input_length)

        with torch.no_grad():
            output = self.qa_model.generate(
                inputs["input_ids"],
                max_new_tokens=max_new_tokens,
                num_return_sequences=1,
                do_sample=True,
                temperature=0.7
            )

        return self.qa_tokenizer.decode(output[0], skip_special_tokens=True)

