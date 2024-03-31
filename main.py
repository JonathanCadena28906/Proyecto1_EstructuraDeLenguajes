from MODEL.gramatica import Gramatica

#La gramatica 1 funciona:

simbolos_terminales = ['a', 'b']
simbolos_no_terminales = ['A', 'B']
producciones = {
    'A': ['aB', 'a'],
    'B': ['bB', 'b']
}
simbolo_inicial = 'A'

gramatica1 = Gramatica(simbolos_terminales, simbolos_no_terminales, producciones, simbolo_inicial)
gramatica1.verificar_palabra('abbb')

#La gramatica 2 No funciona PRESENTA PROBLEMAS CON LA RECURSION DE LA PRODUCCION 'T -> xT | xU', NO SE PUEDE VERIFICAR LA PALABRA 'xxxy':

simbolos_terminales = ['x', 'y']
simbolos_no_terminales = ['S', 'T', 'U']
producciones = {
    'S': [['x'], ['T'], ['']],
    'T': [['x', 'T'], ['x', 'U']],
    'U': [['y']]
}
simbolo_inicial = 'S'

gramatica2 = Gramatica(simbolos_terminales, simbolos_no_terminales, producciones, simbolo_inicial)
gramatica2.verificar_palabra('xxxy')

#La gramatica 3 funciona:

simbolos_terminales = ['1', '0']
simbolos_no_terminales = ['S', 'X', 'Y']
producciones = {
    'S': [['X', 'Y']],
    'X': [['1', 'X'], ['1']],
    'Y': [['0']]
}
simbolo_inicial = 'S'

gramatica3 = Gramatica(simbolos_terminales, simbolos_no_terminales, producciones, simbolo_inicial)
gramatica3.verificar_palabra('11110')

#La gramatica 4 :

simbolos_terminales = ['a', 'b', '']
simbolos_no_terminales = ['S', 'T']
producciones = {
    'S': [['b'], ['bT'], ['']],
    'T': [['a', 'T'], ['']]
}
simbolo_inicial = 'S'

gramatica4 = Gramatica(simbolos_terminales, simbolos_no_terminales, producciones, simbolo_inicial)
gramatica4.verificar_palabra('baaaa')