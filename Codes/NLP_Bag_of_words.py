"""Write a program to read a 3 text files on a movie review with at least 20
sentences and 150 words. Implement bag of words. """

import os
import re
from sklearn.feature_extraction.text import CountVectorizer

# Folder where your 3 text files are stored
folder_path = os.path.join("CSV Files")

# List to store text from selected review files
documents = []

# Specify only the 3 review file names you want
review_files = ["review1.txt", "review2.txt", "review3.txt"]

# Read each review file
for filename in review_files:
    file_path = os.path.join(folder_path, filename)
    if os.path.exists(file_path):  # Check if file actually exists
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Clean text: remove special characters and extra spaces
            text = re.sub(r'[^A-Za-z\s]', '', text)
            text = re.sub(r'\s+', ' ', text)
            text = text.lower()
            documents.append(text)
    else:
        print(f"Warning: {filename} not found!")

# Step 2: Bag of Words using CountVectorizer
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Step 3: Show Results
print("Feature Names (Vocabulary):")
print(vectorizer.get_feature_names_out())

print("\nBag of Words Matrix:")
print(X.toarray())

