'''
ANIRUDH S NAIR
EXPERIMENT 8

Semantic analysis using Naive Bayes

'''

from sklearn.naive_bayes import GaussianNB
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
import re

# Ensure required NLTK resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')

train_text = [
    "I love this movie", "This movie is great", "I dislike this movie", "I hate this movie"
]
train_label = [1, 1, 0, 0]
test_text = "I really like this movie"

def preprocess(text):
    text = re.sub(r"<[^>]+>", " ", text)
    token = word_tokenize(text)
    sw = stopwords.words('english')
    token = [w for w in token if w.lower() not in sw]  # Convert to lowercase
    stemmer = PorterStemmer()
    token = [stemmer.stem(w) for w in token]
    return ' '.join(token)

# Preprocess training data
train_text = [preprocess(text) for text in train_text]

# Preprocess test data
test = preprocess(test_text)

count_vectorizer = CountVectorizer(stop_words="english")

# Transform training data into feature vectors
train = count_vectorizer.fit_transform(train_text).toarray()

# Transform test data into feature vector
features = count_vectorizer.get_feature_names_out()
test_tokens = word_tokenize(test)

tv = [0 for _ in range(len(features))]
for i, feature in enumerate(features):
    if feature in test_tokens:
        tv[i] += 1

# Train the Naive Bayes model
model = GaussianNB()
model.fit(train, train_label)

# Predict sentiment of the test data
test_vector = np.array(tv).reshape(1, -1)
print(test_vector)
m = model.predict(test_vector)
if m == 0:
    print("negative")
else:
    print("positive")
