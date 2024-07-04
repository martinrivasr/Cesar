from cesar import *

def test_cifra_mensaje():
    assert cifra_mensaje ("H",3) == "K" 
    assert cifra_mensaje("ZigZag",3) == "BLJBDJ"
    assert cifra_mensaje(" ",1) == "A"


    encriptador = crea_cifrador(3)
    assert encriptador("ZigZag") == "BLJBDJ"

