# Ejercicio 2 NLTK: Frecuencia de palabras
import nltk
from nltk import FreqDist
nltk.download('punkt')
from nltk.tokenize import word_tokenize
texto = "Hola mundo mundo NLTK NLTK NLTK."
tokens = word_tokenize(texto)
frecuencia = FreqDist(tokens)
print('Frecuencia de palabras:', frecuencia)
