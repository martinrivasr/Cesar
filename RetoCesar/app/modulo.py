
class Alfabeto():
    mayusculas = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ")
    minusculas = list("abcdefghijklmnñopqrstuvwxyz ")

class Cesar():
    def __init__(self, mensaje:str, cifrado:int):
        self.mensaje = mensaje
        self.cifrado = cifrado

    def busca_letra(self, letra, posicion):
        nueva_letra = ''
        if letra.isupper() or letra == ' ':
            indice_letra= Alfabeto.mayusculas.index(letra)
            indice_nueva_letra = indice_letra +  posicion
            indice_nueva_letra = indice_nueva_letra % len(Alfabeto.mayusculas)
            nueva_letra = Alfabeto.mayusculas[indice_nueva_letra]
        else:
            indice_letra= Alfabeto.minusculas.index(letra)
            indice_nueva_letra = indice_letra +  posicion
            indice_nueva_letra = indice_nueva_letra % len(Alfabeto.minusculas)
            nueva_letra = Alfabeto.minusculas[indice_nueva_letra]

        return nueva_letra

    def cifra_mensaje(self):
        nuevo_mensaje = ""
        for eachletter in self.mensaje:
            nuevo_mensaje+= self.busca_letra(eachletter, self.cifrado)
        return nuevo_mensaje

    def crea_cifrador (self):
        def cifrar(self):
            return self.cifra_mensaje(self)
        return cifrar
    



