"""Write a program to read a 3 text files a tourist place with at least 20
sentences and 150 words. Implement TF-IDF. """

import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# Folder where your text files are stored
folder_path = os.path.join("CSV Files")

# List to store text from selected tourist files
documents = []

# Specify the 3 tourist place files you want
tourist_files = ["place1.txt", "place2.txt", "place3.txt"]

# Read each file
for filename in tourist_files:
    file_path = os.path.join(folder_path, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Clean text: remove special characters and extra spaces
            text = re.sub(r'[^A-Za-z\s]', '', text)
            text = re.sub(r'\s+', ' ', text)
            text = text.lower()
            documents.append(text)
    else:
        print(f"Warning: {filename} not found!")

# Step 2: Apply TF-IDF
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)

# Step 3: Show Results
print("Feature Names (Vocabulary):")
print(vectorizer.get_feature_names_out())

print("\nTF-IDF Matrix:")
print(X.toarray())
