from MODEL.gramatica import Gramatica


if __name__ == "__main__":


    # Esta no funcionaaaaa:
    terminales = {'a', 'b'}
    no_terminales = {'S', 'A'}
    producciones = {'S': ['aSb',''], 'A': ['aA', '']}
    simbolo_inicial = 'S'

    gramatica1 = Gramatica(terminales, no_terminales, producciones, simbolo_inicial)

    #Esta si funcionaaaaa:
    terminales = {'a', 'b'}
    no_terminales = {'S', 'T'}
    producciones = {'S': ['b','bT',''], 'T': ['aT', '']}
    simbolo_inicial = 'S'

    gramatica2 = Gramatica(terminales, no_terminales, producciones, simbolo_inicial)

# Verificar si una cadena pertenece al lenguaje definido por la gramática
    #print(gramatica.producciones)
    #gramatica.eliminar_recursion_izquierda()
    #print(gramatica.producciones)
    cadena = 'baaaaaaaaaaaaa'
    print(f"Verificando si la cadena '{cadena}' pertenece al lenguaje {gramatica1.toPrint()}:")
    if gramatica1.pertenece_a_gramatica(cadena):
        print(f"La cadena '{cadena}' pertenece al lenguaje.")
    else:
        print(f"La cadena '{cadena}' no pertenece al lenguaje.")

'''G={Vt,Vn,S,P}

Vt={λ, b , a}
Vn={ S, T } , donde es S es el símbolo inicial


El conjunto de P:

S->  | b| bT | λ
T->aT| λ'''
