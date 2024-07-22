import pandas as pd
import re
import nltk
from nltk.translate import AlignedSent, IBMModel1

# Ensure necessary NLTK data is downloaded
nltk.download('punkt')

# Load the dataset
df = pd.read_csv("engspn.csv")
eng_sentence = df['english'].tolist()
spn_sentence = df['spanish'].tolist()

# Function to clean sentences
def clean_sentence(sentences):
    if isinstance(sentences, list):
        cleaned_sentence = []
        for s in sentences:
            s = s.strip().lower()
            s = re.sub(r"[^a-zA-Z0-9]+", " ", s)
            cleaned_sentence.append(s.strip())
        return cleaned_sentence
    else:
        s = sentences.strip().lower()
        s = re.sub(r"[^a-zA-Z0-9]+", " ", sentences)
        return s.strip()

# Clean the sentences
cleaned_english_sentence = clean_sentence(eng_sentence)
cleaned_spanish_sentence = clean_sentence(spn_sentence)

# Function to train the translation model
def train_translation_model(source_sentence, target_sentence):
    aligned_sentence = [AlignedSent(source.split(), target.split()) for source, target in zip(source_sentence, target_sentence)]
    ibm_model = IBMModel1(aligned_sentence, 10)
    return ibm_model

# Train the model
translation_model = train_translation_model(cleaned_english_sentence, cleaned_spanish_sentence)

# Function to translate input sentences
def translate_input(ibm_model):
    while True:
        source_text = input("Enter the English sentence to be translated (or 'q' to quit): ")
        if source_text.lower() == 'q':
            print("Quitting...")
            break
        else:
            cleaned_text = clean_sentence(source_text).split()
            translated_words = []
            for source_word in cleaned_text:
                max_prob = 0
                translated_word = None
                if source_word in ibm_model.translation_table:
                    for target_word, prob in ibm_model.translation_table[source_word].items():
                        if prob > max_prob:
                            max_prob = prob
                            translated_word = target_word
                if translated_word is not None:
                    translated_words.append(translated_word)
                else:
                    translated_words.append(source_word)  # Handle OOV (out-of-vocabulary) words

            translated_text = ' '.join(translated_words)
            print("Translated text: ", translated_text)
            print()

# Start the translation input loop
translate_input(translation_model)
