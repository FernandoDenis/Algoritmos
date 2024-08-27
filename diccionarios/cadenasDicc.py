# cadena = "casa perro gato casa perro gato árbol perro gato árbol flor gato flor perro árbol flor casa flor gato perro árbol perro gato casa flor gato árbol perro casa flor perro gato perro gato flor árbol gato casa flor perro"

libro = open("diccionarios\\Libro.txt", encoding="UTF-8")
cadena = libro.read()

palabrasEnCadena = {}

# Variable para almacenar cada palabra
palabra = ""

# Variable para almacenar la posicion de cada palabra
posicion = 0

for i in cadena:
    # Condicion para saber el momento en que termino una palabra
    if(i == " " or i == "," or i == "."):
        # Revisa que la palabra no se encuentre en el diccionario
        if(palabra in palabrasEnCadena) and palabra != "":
            posicion += 1
            # Obtiene la clave de la palabra existente, que es el numero de repeticiones de esa palabra y le suma 1 
            sumaRepeticiones = max(palabrasEnCadena[palabra].keys()) + 1
            # Elimina por medio de pop el subdiccionario dentro de la palabra y devuelve un array que son las posiciones de la palabra
            arrayCadena = palabrasEnCadena[palabra].pop(max(palabrasEnCadena[palabra].keys()))
            # Agrega la nueva posicion de la palabra
            arrayCadena.append(posicion)
            # Al no existir el subdiccionario de la palabra, le actualiza los datos con la suma de repeticiones y el numero array de cadena
            palabrasEnCadena[palabra][sumaRepeticiones] = arrayCadena

        # Condicion por si la palabra SI se encuentra en el diccionario    
        elif not((palabra in palabrasEnCadena)) and palabra != "":
            posicion += 1
            # Crea un diccionario como valor para agregar los campos de numero de repeticiones y posicion
            palabrasEnCadena[palabra] = {}
            # Declara como primer valor 1 dentro del array la posicion de esa palabra
            palabrasEnCadena[palabra][1] = [posicion]
        
        # Se borra la palabra porque habra terminado la palabra
        palabra = ""
        continue
    else:
        # La suma de letra por letra para obtener la palabra
        palabra += i
else:
    # Lo mismo de arriba
    if(palabra in palabrasEnCadena) and palabra != "":
        posicion += 1
        sumaRepeticiones = max(palabrasEnCadena[palabra].keys()) + 1
        arrayCadena = palabrasEnCadena[palabra].pop(max(palabrasEnCadena[palabra].keys()))
        arrayCadena.append(posicion)
        palabrasEnCadena[palabra][sumaRepeticiones] = arrayCadena
            
    elif not((palabra in palabrasEnCadena)) and palabra != "":
        posicion += 1
        palabrasEnCadena[palabra] = {}
        palabrasEnCadena[palabra][1] = [posicion]
        
print(palabrasEnCadena)