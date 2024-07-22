'''
ANIRUDH S NAIR
EXPERIMENT 5

    5.1) One Hot Encoding
    5.2) Bag of words

'''


from nltk.tokenize import word_tokenize

n=int(input("enter the number of document: "))
doc=[]
for i in range(n):
    d=input("enter the documnet",i+1,": ")
    doc.append(d)

text=" "
for i in doc:
    text=text+" "+i.lower()
token=set(word_tokenize(text))
t=dict()
for i,word in enumerate(token):
    t[word]=i+1
print("index for eaxh word is:")
for i in t:
    print(i," : ", t[i])

# 5.1) One Hot Encoding

for text in doc:
    ohe=[]
    for word in text.split():
        vector=[ 0 for i in range(len(token))]
        vector[t[word.lower()]-1]=1
        ohe.append(vector)
    print("document: ",text)
    print("one hot encoding: ",ohe)

# 5.2) Bag of Words

for text in doc:
    vector=[0 for i in range(len(token))]
    for word in text.split():
        vector[t[word.lower()]-1]=1