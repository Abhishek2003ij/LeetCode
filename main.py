import spacy
import idx
nlp = spacy.load('en_core_web_sm')
text = nlp("Abhishek IJ is a passionate software enthusiast. He enjoys solving challenging coding problems. He has strong expertise in Java and backend development. He actively explores data science, machine learning, and NLP concepts. He loves building real-world projects and continuously improving his technical skills.")
token = [token.text for token in text]
# print(token)
stop = spacy.lang.en.stop_words.STOP_WORDS
print([token for token in token if not stop])
