"""Write a program to read a text file with at least 30 sentences and 200 words
and perform the following tasks in the given sequence.
a. Text cleaning by removing punctuation/special characters, numbers
and extra white spaces. Use regular expression for the same.
b. Convert text to lowercase
c. Stemming and Lemmatization
d. Create a list of 3 consecutive words after lemmatization """

import re 
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.util import ngrams

file_path=os.path.join("CSV Files","sample_text.txt")

# Step a: Read and clean the text
with open(file_path,'r',encoding='utf-8') as file:
    text=file.read()

# Remove punctuation, numbers, and special characters
text=re.sub(r'[^A-Za-z\s]','',text)
text=re.sub(r'\s+',' ',text)  # Remove extra spaces

# convert to lowercase
text=text.lower()

# Step b: Tokenize the cleaned text
tokens = word_tokenize(text)
# print("Tokens:\n", tokens[:50])  # Print first 50 tokens

# Step c: Remove stop words
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]

# Step d: Perform Stemming and Lemmatization
# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]

# Step e: Create a list of 3 consecutive words after lemmatization (Trigrams)
trigrams = list(ngrams(lemmatized_tokens, 3))

# Display the output (for checking the first few outputs)
print("Stemmed Tokens:", stemmed_tokens[:10])  # Show first 10 stemmed words
print("Lemmatized Tokens:", lemmatized_tokens[:10])  # Show first 10 lemmatized words
print("3 Consecutive Word Sequences:", trigrams[:10])  # Show first 10 trigrams