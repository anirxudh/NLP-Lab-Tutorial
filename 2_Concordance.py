'''
ANIRUDH S NAIR
EXPERIMENT 2
CONCORDANCE

'''
import nltk

s = input("Enter the sentence: ")  # input
word = nltk.word_tokenize(s)  # tokenize each word of the sentence
text = nltk.Text(word) # creating a text object for the tokenised words

t = input("Enter the word: ") # input the word to find matches
text.concordance(t) # concordance checks for matches and displays it
