import re
import string
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

from typing import List

nltk.download('stopwords')

def clean_text(text: str) -> str:
    """
    Cleans a given text by converting it to lowercase, removing punctuation,
    and eliminating English stop words.

    Parameters:
    text (str): The text to be cleaned.

    Returns:
    str: The cleaned text with all words in lowercase, no punctuation, and 
         without stop words.

    Note:
    This function requires the NLTK library and its 'stopwords' dataset.
    Make sure to download the dataset using nltk.download('stopwords') before using this function.
    """
    # Convert text to lower case
    text = text.lower()

    # Remove punctuation
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])

    return text

def tokenize(text: str) -> List[str]:
    """
    Tokenizes the given text into individual words.

    This function splits a string into a list of words, using NLTK's word_tokenize method.
    It's useful for breaking down a text into its constituent words for further natural
    language processing tasks.

    Parameters:
    text (str): The text to be tokenized.

    Returns:
    List[str]: A list of words obtained by tokenizing the input text.

    Note:
    This function requires the NLTK library. Make sure to have NLTK installed
    and its relevant datasets downloaded as needed.
    """
    return word_tokenize(text)



def stem_sentence(sentence: str) -> str:
    """
    Stems each word in a given sentence.

    This function applies the Porter stemming algorithm (using NLTK's PorterStemmer)
    to each word in the input sentence. Stemming is a process of reducing words to their
    root or base form. For example, "running" would be stemmed to "run".

    Parameters:
    sentence (str): The sentence whose words are to be stemmed.

    Returns:
    str: A string containing the stemmed version of each word in the input sentence,
         with words separated by spaces.

    Note:
    This function requires the NLTK library and specifically the PorterStemmer module.
    Ensure that NLTK is installed and available.
    """
    stemmer = PorterStemmer()
    return " ".join([stemmer.stem(word) for word in sentence.split()])


def lemmatize_sentence(sentence: str) -> str:
    """
    Lemmatizes each word in a given sentence.

    This function applies word lemmatization using NLTK's WordNetLemmatizer. Lemmatization is 
    the process of reducing words to their base or root form in a meaningful way (unlike stemming).
    For instance, the word "better" would be lemmatized to "good".

    Parameters:
    sentence (str): The sentence whose words are to be lemmatized.

    Returns:
    str: A string containing the lemmatized version of each word in the input sentence,
         with words separated by spaces.

    Note:
    This function requires the NLTK library, specifically the WordNetLemmatizer. Ensure that NLTK 
    and the WordNet data are installed and available.
    """
    lemmatizer = WordNetLemmatizer()
    return " ".join([lemmatizer.lemmatize(word) for word in sentence.split()])

def downsample_to_number(df, class_column, n_samples, random_state=42):
    downsampled_dfs = []
    for class_value in df[class_column].unique():
        df_class = df[df[class_column] == class_value]
        df_class_downsampled = df_class.sample(
            n=min(n_samples, len(df_class)), 
            random_state=random_state
        )
        downsampled_dfs.append(df_class_downsampled)
    return pd.concat(downsampled_dfs)