'''
ANIRUDH S NAIR
EXPERIMENT 7

Cosine Similarity
'''

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

t1=" i love watching movies "
t2=" love watching movies"
sw=stopwords.words('english')

t1_tok=word_tokenize(t1)
t2_tok=word_tokenize(t2)

t1_set={ w for w in t1_tok if w not in sw and w not in string.punctuation }
t2_set={ w for w in t2_tok if w not in sw and w not in string.punctuation }

v=t1_set.union(t2_set)
l1=[]
for i in v:
    if i in t1_set:
        l1.append(1)
    else:
        l1.append(0)
l2=[]
for i in v:
    if i in t2_set:
        l2.append(1)
    else:
        l2.append(0)
print(t1," : ",l1)
print(t2," : ",l2)

c=0
for i in range(len(v)):
    c+=l1[i]*l2[i]
cosine=c/float((sum(l1)**0.5)*sum(l2)**0.5)
print(cosine)