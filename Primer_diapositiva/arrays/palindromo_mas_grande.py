array_palindromos = [
    "radar", "nivel", "sol", "somos", "luz",
    "reconocer", "palabra", "ana", "computadora", "oso",
    "casa", "salas", "ratón", "anilina", "gato",
    "oro", "papel", "malayalam", "carro", "reparar"
]

def es_palindromo(palabra):
    return palabra == palabra[::-1], len(palabra)

def lista_de_palindromos(array):
    mas_grande = ""
    for palabra in array:
        palin, longitud = es_palindromo(palabra)
        if palin and longitud > len(mas_grande):
            mas_grande = palabra
    return mas_grande

print(lista_de_palindromos(array_palindromos))
