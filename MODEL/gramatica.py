class Gramatica:
    def __init__(self, simbolos_terminales, simbolos_no_terminales, producciones, simbolo_inicial):
        self.simbolos_terminales = simbolos_terminales
        self.simbolos_no_terminales = simbolos_no_terminales
        self.producciones = producciones
        self.simbolo_inicial = simbolo_inicial

    def verificar_palabra(self, palabra):
        self.palabra = palabra
        self.indice = 0
        Pertenece = self.verificar_simbolo(self.simbolo_inicial) and self.indice == len(palabra)
        if Pertenece:
            print("\nla palabra '",palabra,"' pertenece a la gramatica:")
            print(self.__str__())
        else:
            print("\nla palabra '",palabra,"' NO pertenece a la gramatica:")
            print(self.__str__())
    
    def verificar_simbolo(self, simbolo):
        if simbolo in self.simbolos_terminales:
            if self.indice < len(self.palabra) and self.palabra[self.indice] == simbolo:
                self.indice += 1
                return True
            else:
                return False
        elif simbolo in self.simbolos_no_terminales:
            indice_guardado = self.indice
            for produccion in self.producciones[simbolo]:
                self.indice = indice_guardado  # Restaurar el índice al inicio de cada producción
                if produccion == ['']:
                    # Si la producción es una cadena vacía, solo devuelve True si no quedan más símbolos para verificar
                    if self.indice == len(self.palabra):
                        return True
                elif all(self.verificar_simbolo(s) for s in produccion):
                    return True
            self.indice = indice_guardado  # Restaurar el índice si todas las producciones fallan
        return False
    
    def tiene_recursion_izquierda(self):
        for no_terminal, producciones in self.producciones.items():
            for produccion in producciones:
                if produccion and produccion[0] == no_terminal:
                    return True
        return False
        
    def __str__(self):
        return f"\nsimbolos terminales {self.simbolos_terminales}\n simbolos no terminales {self.simbolos_no_terminales}\n producciones {self.producciones}\n simbolo inicial {self.simbolo_inicial}"