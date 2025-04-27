"""Write a program to read a text file with at least 30 sentences and 200 words
and perform the following tasks in the given sequence.
a. Text cleaning by removing punctuation/special characters, numbers
and extra white spaces. Use regular expression for the same.
b. Convert text to lowercase
c. Tokenization
d. Remove stop words
e. Correct misspelled words """

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from spellchecker import SpellChecker
import os

# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')

# Path to file inside "CSV Files" folder
file_path = os.path.join("CSV Files", "sample_text.txt")

# Step a: Read and clean the text
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Remove punctuation, numbers, and special characters
text = re.sub(r'[^A-Za-z\s]', '', text)
text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
# print("Cleaned Text:\n", text[:500])  # Print first 500 characters of cleaned text
# Step b: Convert to lowercase
text = text.lower()

# Step c: Tokenization (no sentence split to avoid punkt_tab error)
tokens = word_tokenize(text)

# Step d: Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_tokens = [word for word in tokens if word not in stop_words]

# Step e: Correct spelling
spell = SpellChecker()
corrected_tokens = [spell.correction(word) for word in filtered_tokens]

# Final Output
print("Original Tokens:\n", tokens[:50])
print("\nFiltered Tokens (no stopwords):\n", filtered_tokens[:50])
print("\nCorrected Tokens:\n", corrected_tokens[:50])

