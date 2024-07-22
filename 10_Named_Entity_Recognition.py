import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
from nltk.chunk import ne_chunk
from nltk import pos_tag
import string
from nltk.tokenize import word_tokenize

s=input("enter the string: ")
words=word_tokenize(s)
tag=pos_tag(words)
tree=ne_chunk(tag)
print(tree)

def to_bio(tree):
    bio_tags = []
    for chunk in tree:
        if hasattr(chunk, 'label'):
            bio_tags.append("B-" + chunk.label())
            for subchunk in chunk[1:]:
                bio_tags.append("I-" + chunk.label())
        else:
            bio_tags.append("O")
    return bio_tags

bio_tags=to_bio(tree)
for i, t in zip(words, bio_tags):
    print(i,t)