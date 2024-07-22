import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


sentences=[
    " i have a dog", "his name is jacki", "he is an obidient and calm dog", "he gaurds our home" 
]
ip=input("enter the sentence to check with: ")
sentences.append(ip)
vectors=CountVectorizer().fit_transform(sentences).toarray()
cosine=cosine_similarity(vectors)
ip_index=len(sentences)-1
ss_index=np.argmax(cosine[ip_index][:-1])

print("input: ",ip)
print("most similar sentence: ",sentences[ss_index])
print("similarity score: ",cosine[ip_index][ss_index])