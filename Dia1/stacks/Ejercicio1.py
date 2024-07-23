
#Dada una cadena que contiene parentesis. Identificar si todos los parentesis abren y cierran.

cadena = "{esta (es [una]) prueba}"

def abrenYCierran(cadena):
    stack = []
    for letter in cadena:
        if(letter == "{"):
            stack.append("}")
        elif(letter == "("):
            stack.append(")")
        elif(letter == "["):
            stack.append("]")
        elif (letter == "]" and stack.pop() != "]"):
            return False
        elif (letter == ")" and stack.pop() != ")"):
            return False
        elif (letter == "}" and stack.pop() != "}"):
            return False
        else:
            continue
    if(len(stack) >= 1):
        return False
    return True

print(abrenYCierran(cadena))
        