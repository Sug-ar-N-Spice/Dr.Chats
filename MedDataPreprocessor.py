import re
import nltk
import pandas as pd
from nltk.corpus import stopwords
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

## THIS IS CLASS THAT Cleans the data
class MedDataPreprocessor:
    """
    Preprocessor for general medical data.
    This class handles cleaning, normalization, and preparation of text data
    related to medical topics for use in a medical chatbot.
    """

    def __init__(self):
        """Initialize the preprocessor with necessary NLTK downloads."""
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        self.stop_words = set(stopwords.words('english'))

        # Minimal list of medical terms to preserve
        self.medical_terms = {
            # Terms conflicting with stopwords
            'a', 'am', 'an', 'as', 'at', 'be', 'by', 'in', 'no', 'on', 'or', 'to', 'up',
            # Critical abbreviations to always preserve
            'ct', 'dr', 'er', 'hiv', 'hr', 'icu', 'iv', 'mr', 'ms'
        }

        self.stop_words = self.stop_words - self.medical_terms

    def clean_text(self, text: str) -> str:
        """
        Clean and normalize the input text.

        Args:
            text (str): Raw input text

        Returns:
            str: Cleaned and normalized text
        """

        if pd.isna(text):
            return ""

        # Convert to lowercase
        text = text.lower()

        # Remove special characters but keep medical symbols
        text = re.sub(r'[^a-zA-Z0-9\s+\-/%]', '', text)

        # Remove extra whitespace
        text = ' '.join(text.split())

        return text

    def remove_stopwords(self, text: str) -> str:
        """
        Remove stopwords from the text, keeping medical specific terms.

        Args:
            text (str): Input text

        Returns:
            str: Text with stopwords removed
        """
        ### this is resulting in a list of words was converting sentence / paragraph into a list of words

        nlp = English()
        tokenizer = Tokenizer(nlp.vocab)
        words = tokenizer(text)

        filtered_words = [word for word in words if word not in self.stop_words]
        return ' '.join(filtered_words)

    def preprocess_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Preprocess the entire dataframe.

        Args:
            df (pd.DataFrame): Input dataframe

        Returns:
            pd.DataFrame: Preprocessed dataframe
        """
        # change columns names depending which csv file you are using cleaning text and removing stopwords
        df['clean_question'] = df['question'] # .apply(self.clean_text).apply(self.remove_stopwords)
        df['clean_context'] = df['context'] #.apply(self.clean_text).apply(self.remove_stopwords)

        # Combine cleaned abstract and results or full_texts depending on which csv you are using
        df['combined_text'] = df['clean_question'] + ' ' + df['clean_context']

        return df

    def prepare_for_model(self, text: str, max_length: int = 512) -> str: ##looks at paragraph, cuts the paragraph if more than 512 This takes the sentence splits to words and has a max length
        """
        Prepare text for model input, truncating if necessary.

        Args:
            text (str): Input text
            max_length (int): Maximum number of words

        Returns:
            str: Prepared text
        """
        words = text.split()
        if len(words) > max_length:
            return ' '.join(words[:max_length])
        return text

