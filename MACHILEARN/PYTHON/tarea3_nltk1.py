# Ejercicio 1 NLTK: Tokenización de palabras
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
texto = "Hola mundo, esto es NLTK."
tokens = word_tokenize(texto)
print('Tokens:', tokens)
