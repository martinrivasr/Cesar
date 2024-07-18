from app.modulo import *

def test_cifra_mensaje():
    assert Cesar.cifra_mensaje ("H",3) == "K" 
    assert Cesar.cifra_mensaje ("ZigZag",3) == "BljBdj"
    assert Cesar.cifra_mensaje("BLJBDJ",-3) == "ZIGZAG" 
    assert Cesar.cifra_mensaje(" ",1) == "A"


    encriptador = Cesar.crea_cifrador(3)
    assert encriptador("ZigZag") == "BLJBDJ"


    # Crear una instancia de Cesar
cesar = Cesar("Hola Mundo", 3)

# Obtener el cifrador
cifrador = cesar.crea_cifrador()

# Usar el cifrador para cifrar el mensaje
mensaje_cifrado = cifrador()
print(mensaje_cifrado)  # Debería imprimir el mensaje cifrado


def test_cifrado():
    mensaje = "Hola Mundo"
    cifrado = 3
    cesar = Cesar(mensaje, cifrado)
    mensaje_cifrado = cesar.cifra_mensaje()
    print(mensaje_cifrado)