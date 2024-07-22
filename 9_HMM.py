import nltk
nltk.download('brown')
from nltk.corpus import brown

training=brown.tagged_sents()[:400]
testing=brown.tagged_sents()[400:500]

hmm_tag=nltk.HiddenMarkovModelTagger.train(training)
hmm_tag.accuracy(testing)

text=input("enter the text: ")
text=nltk.word_tokenize(text)
print(hmm_tag.tag(text))