# Ejercicio 3 NLTK: Eliminar stopwords
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
palabras = ["hola", "mundo", "esto", "es", "un", "ejemplo", "de", "tokenización"]
stop_words = set(stopwords.words('spanish'))
palabras_filtradas = [palabra for palabra in palabras if palabra.lower() not in stop_words]
print('Palabras filtradas:', palabras_filtradas)
