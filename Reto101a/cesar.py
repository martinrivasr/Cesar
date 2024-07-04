alfabeto = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ ")

def busca_letra(letra, posicion):
    indice_letra= alfabeto.index(letra.upper ())
    indice_nueva_letra = indice_letra +  posicion
    indice_nueva_letra = indice_nueva_letra % len(alfabeto)
    return alfabeto[indice_nueva_letra]

def cifra_mensaje(mensaje, cifrado):
    nuevo_mensaje = ""
    for eachletter in mensaje:
        nuevo_mensaje+= busca_letra(eachletter, cifrado)
    return nuevo_mensaje

def crea_cifrador (cifrado):
    def cifrar(mensaje):
        nuevo_mensaje = ""
        for eachletter in mensaje:
            nuevo_mensaje +=  busca_letra(eachletter, cifrado)
        return nuevo_mensaje
    return cifrar
    



