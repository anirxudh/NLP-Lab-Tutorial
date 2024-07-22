'''
ANIRUDH S NAIR
EXPERIMENT 6

TF-IDF vectorisation
'''

from sklearn.feature_extraction.text import TfidfVectorizer

doc=input("enter the doc: ")

vectoriser=TfidfVectorizer()

tfidf_matrix=vectoriser.fit_transform([doc])

vocabulary=vectoriser.vocabulary_
idf=vectoriser.idf_

for word,tfidf_value in zip(vocabulary,tfidf_matrix.toarray()[0]):
    print(f"word: {word}    TF-IDF: {tfidf_value:4f}")
