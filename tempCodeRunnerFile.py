from MODEL.gramatica import Gramatica

simbolos_terminales = ['a', 'b']
simbolos_no_terminales = ['A', 'B']
producciones = {
    'A': ['aA', 'a'],
    'B': ['bB', 'b']
}
simbolo_inicial = 'A'

gramatica1 = Gramatica(simbolos_terminales, simbolos_no_terminales, producciones, simbolo_inicial)

resultado = gramatica1.verificar_palabra('aaaab')
print(resultado)  # True