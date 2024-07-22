'''
Anirudh S Nair
EXPERIMENT 3

    Counting Vocabulary:
      1. no of words
      2. different words(type)
      3. frequency of word
      4. percentage of word
'''

# 1. NO. OF WORDS
# ---------------
 
import nltk

s=input("enter the sentence to be analysed: ")
word=nltk.word_tokenize(s)
l=len(word)

print("the number of words in the input is: ", len(word))


# DIFFERENT TYPE OF WORDS
# -----------------------
# if the program is done seperately then include the import, input and tokenization part of above program here 

list=[]
count=0
print("distinct words are: ")
for i in word:
    if i not in list:
        list.append(i)
        print(word)
        count+=1
print("the number of different words are: ", count) 

# FREQUENCY OF WORDS
# ------------------

from nltk import FreqDist
a=FreqDist(word)
print(a)

# PERCENTAGE OF WORDS
# -------------------

for i in a:
    r=a[i]
    p=r/l*100
    print("the percentage for the", i, "is: ", p)

