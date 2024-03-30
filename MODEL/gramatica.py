class Gramatica:
    def __init__(self, terminales, no_terminales, producciones, simbolo_inicial):
        self.terminales = terminales
        self.no_terminales = no_terminales
        self.producciones = producciones
        self.simbolo_inicial = simbolo_inicial

    def agregar_produccion(self, no_terminal, produccion):
        if no_terminal not in self.producciones:
            self.producciones[no_terminal] = []
        self.producciones[no_terminal].append(produccion)

    def pertenece_a_gramatica(self, cadena):
        return self._verificar_cadena(cadena, [self.simbolo_inicial])

    def _verificar_cadena(self, cadena, pila):
        if not cadena and not pila:
            return True
        if not pila:
            return False

        simbolo = pila.pop()

        if simbolo in self.no_terminales:
            for produccion in self.producciones[simbolo]:
                if self._verificar_cadena(cadena, list(produccion[::-1]) + pila):
                    return True
        elif simbolo in self.terminales and cadena and simbolo == cadena[0]:
            return self._verificar_cadena(cadena[1:], pila)

        return False

    '''def pertenece_lenguaje(self, cadena):
        return self.analizar_cadena(cadena, self.simbolo_inicial)
    
    def analizar_cadena(self, cadena, simbolo):
        if not cadena:
            return '' in self.producciones[simbolo]

        for produccion in self.producciones[simbolo]:
            if produccion == '':
                continue

            if self.match_produccion(cadena, produccion):
                return True

        return False

    def match_produccion(self, cadena, produccion):
        if produccion == '':
            return cadena == ''

        if not cadena:
            return False

        if produccion[0] in self.terminales:
            if cadena[0] == produccion[0]:
                return self.match_produccion(cadena[1:], produccion[1:])
        else:
            for prod in self.producciones[produccion[0]]:
                if self.match_produccion(cadena, prod + produccion[1:]):
                    return True

        return False'''
    
    def toPrint(self):  
        return f'G=({self.terminales},{self.no_terminales},{self.simbolo_inicial},{self.producciones})'

  #Codigo generado por copilot, se debe de revisar, su ejecucion arrojò lo siguiente, pero desborda el metodod de compraciòn de palabras:
    # {'S': ['Sab', ''], 'A': ['aA', '']}
    #{'S': ["S'", ''], 'A': ['aA', ''], "S'": ["abS'", '']} 
    def eliminar_recursion_izquierda(self):
        for A in list(self.producciones.keys()):
            producciones_A = self.producciones[A]
            recursivas = [p for p in producciones_A if p and p[0] == A]
            no_recursivas = [p for p in producciones_A if not p or p[0] != A]

            if recursivas:
                # Crear un nuevo no terminal
                nuevo_no_terminal = A + "'"
                self.no_terminales.add(nuevo_no_terminal)

                # Reemplazar las producciones de A
                self.producciones[A] = [p + nuevo_no_terminal for p in no_recursivas] + ['']

                # Agregar nuevas producciones para el nuevo no terminal
                self.producciones[nuevo_no_terminal] = [p[1:] + nuevo_no_terminal for p in recursivas] + ['']