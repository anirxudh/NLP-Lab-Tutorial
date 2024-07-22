'''
Anirudh S Nair
EXPERIMENT 4

Preprocessing of text

'''
import nltk
import re

s = input("Enter the sentence that you want to preprocess: ")

# Script evaluation
streval = ''
for i in re.findall("<.*?>", s):
    streval += i[1:-1]

# Tokenize
word = nltk.word_tokenize(s)
lcword = [i.lower() for i in word]
print("Tokenized words:", lcword)

# Filter punctuation
fil = []
import string
for i in word:
    if i not in string.punctuation:
        fil.append(i)
print("Words without punctuation:", fil)

# Remove symbols
streval = []
pattern = "<[^>]+/\?"
for i in fil:
    if i not in re.findall(pattern, i):
        streval.append(i)
print("Words without symbols:", streval)

# Remove stopwords
remstop = []
stopwords = nltk.corpus.stopwords.words("english")
for i in streval:
    if i not in stopwords:
        remstop.append(i)
print("Words without stopwords:", remstop)

# Stemming and output
stemmed = []
stemmer = nltk.stem.PorterStemmer()
for i in remstop:
    stemmed.append(stemmer.stem(i))

print("Preprocessed text is:", stemmed)
