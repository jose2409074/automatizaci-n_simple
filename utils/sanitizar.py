#Función para sanitizar texto
import unicodedata
def sanitizar(texto):
    # Convertir a minúsculas
    texto = texto.lower()
    # Normalizar el texto para eliminar tildes y diéresis
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    # Reemplazar la ñ por n
    texto = texto.replace('ñ', 'n')
    return texto