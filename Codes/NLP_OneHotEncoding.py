"""Write a program to read a 3 text files on any technical concept with at least
20 sentences and 150 words. Implement one-hot encoding. """

import os
import re
from sklearn.preprocessing import OneHotEncoder
import numpy as np

folder_path="CSV Files"

# Define file paths relative to the folder
file_paths = [
    os.path.join(folder_path, "text_file1.txt"),
    os.path.join(folder_path, "text_file2.txt"),
    os.path.join(folder_path, "text_file3.txt")
]

# Step 1: Read and clean text from files
texts = []
for file_path in file_paths:
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Remove non-alphabetical characters and convert to lowercase
        text = re.sub(r'[^A-Za-z\s]', '', text).lower()
        texts.append(text)

# Combine all texts into a single list of words
words = []
for text in texts:
    words.extend(text.split())

# Step 2: Create a set of unique words
unique_words = sorted(set(words))

# Step 3: One-hot encoding using sklearn
encoder = OneHotEncoder(sparse_output=False)
word_matrix = encoder.fit_transform(np.array(unique_words).reshape(-1, 1))

# Display the one-hot encoded matrix (show first 10 rows for brevity)
print("One-Hot Encoding for the first 10 unique words:")
for i in range(min(10, len(unique_words))):
    print(f"Word: {unique_words[i]} -> One-Hot Encoding: {word_matrix[i]}")

# Optionally save the matrix to a CSV file for future reference
# np.savetxt("one_hot_encoded_words.csv", word_matrix, delimiter=",", fmt="%d")