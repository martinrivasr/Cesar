
'''
Esta Clase recibe un valor entrero y lo convierte en un número romano.
El valor máximo es de 89'999,999
'''
# Definición del diccionario elementos
elementos = {
    "1": "I",
    "5": "V",
    "10": "X",
    "50": "L",
    "100": "C",
    "500": "D",
    "1000": "M",
    "5000": "V°",
    "10000": "X°",
    "50000": "L°",
    "100000": "C°",
    "500000": "D°",
    "1000000": "M°",
    "5000000": "V°°",
    "10000000": "X°°",
    "50000000": "L°°"
}
valor_maximo = 89999999

# Clase para convertir números a romanos
class RomanNumber:
    
    def __init__(self, valor):
        if isinstance(valor, int):
            if valor > valor_maximo:
                self.entero = None
                self.romano = None
                print(f"Error: El valor '{valor}' máximo permitido es 89'999,999.")
            else:
                self.entero = valor
                self.romano = self.arabigo_a_romano()
        elif isinstance(valor, str) and self.esromano(valor):
            self.romano = valor
            self.entero = self.romano_a_arabigo(valor)
        else:
            self.entero = None
            self.romano = None
            print(f"Error: El valor '{valor}' no es un número entero ni un número romano válido.")
    
    
    def __str__(self):
        return f"El número {self.entero} en arabigo es {self.romano}"
    
    def __repr__(self) -> str:
        return f"Número(Arabigo = '{self.entero}', Romano = '{self.romano}')"

    def __add__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.value + other.value)
        elif isinstance(other, (int, float)):
            return RomanNumber(self.value + round(other))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.value - other.value)
        elif isinstance(other, (int, float)):
            return RomanNumber(self.value - round(other))
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.value * other.value)
        elif isinstance(other, (int, float)):
            return RomanNumber(self.value * round(other))
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, RomanNumber):
            return RomanNumber(self.value // other.value)
        elif isinstance(other, (int, float)):
            return RomanNumber(self.value // round(other))
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, RomanNumber):
            return self.value == other.value
        elif isinstance(other, (int, float)):
            return self.value == round(other)
        return NotImplemented

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, RomanNumber):
            return self.value < other.value
        elif isinstance(other, (int, float)):
            return self.value < round(other)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, RomanNumber):
            return self.value <= other.value
        elif isinstance(other, (int, float)):
            return self.value <= round(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, RomanNumber):
            return self.value > other.value
        elif isinstance(other, (int, float)):
            return self.value > round(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, RomanNumber):
            return self.value >= other.value
        elif isinstance(other, (int, float)):
            return self.value >= round(other)
        return NotImplemented

    def valida_dato(self, valor):
        try:
            int(valor)
            return True
        except ValueError:
            return False
    
    def esromano(self, valor):
        valor_str = str(valor)
        diccionario_invertido = {v: k for k, v in elementos.items()}
        for char in valor_str:
            if char not in  diccionario_invertido:
                return False
        return True
            
        

    def buscar_clave_valor(self, diccionario, base_buscada): 
        posicion = 0
        for clave, valor in diccionario.items(): 
            if clave == str(base_buscada):
                return clave, valor, posicion
            posicion += 1
        return None, None, None

    def cambia_num(self, base, inicio):
        nuevo_numero = ""
        clave, valor_asociado, posicion = self.buscar_clave_valor(elementos, base)
        
        if clave is None:
            return nuevo_numero  # Si no se encuentra la clave, devolver lista vacía
        
        valor_asociado1 = list(elementos.items())[posicion + 1][1]
        if int(clave) < 10000000:
            valor_asociado2 = list(elementos.items())[posicion + 2][1]
        
        if inicio in [1, 2, 3]:
            for _ in range(inicio):
                nuevo_numero += valor_asociado
        elif inicio == 4:
            nuevo_numero += valor_asociado + valor_asociado1
        elif inicio == 5:
            nuevo_numero += valor_asociado1
        elif inicio in [6, 7, 8]:
            nuevo_numero += valor_asociado1
            for _ in range(inicio - 5):
                nuevo_numero += valor_asociado
        elif inicio == 9:
            nuevo_numero += valor_asociado + valor_asociado2
        
        return nuevo_numero

    def arabigo_a_romano(self):
        if self.entero is None:
            return ""
        
        valor_str = str(self.entero)  # Convertimos el valor a cadena
        nuevo_numero = ""
        
        for posicion in range(len(valor_str)):
            exponente = len(valor_str) - posicion - 1
            elemento = int(valor_str[posicion]) * (10 ** exponente)
            if elemento != 0:
                elemento_base = elemento // int(valor_str[posicion])
                elemento_inicio = elemento // elemento_base
                nuevo_numero += self.cambia_num(str(elemento_base), elemento_inicio)
        
        return nuevo_numero
    
    def romano_a_arabigo(self,valor):
        if valor  is None:
            return 0
     
        valor_str = str(valor)
        longitud = len(valor_str)
        numero_entero = 0
        elemento_actual = ''
        elemento_siguiente = ''
        diccionario_invertido = {v: k for k, v in elementos.items()}
        elementos_rev = dict(reversed(list(diccionario_invertido.items())))
        posicion = 0
        while  posicion < longitud:
            elemento_actual = valor_str[posicion]
            clave_act, valor_asociado_act, posicion_act = self.buscar_clave_valor(elementos_rev, str(elemento_actual))
            if posicion < (longitud- 1):
                elemento_siguiente = valor_str[posicion + 1]
                clave_sig, valor_asociado_sig, posicion_sig = self.buscar_clave_valor(elementos_rev, str(elemento_siguiente))
            else:
                posicion_sig = posicion_act

            if int(posicion_act) <= int(posicion_sig):
                numero_entero += int(valor_asociado_act)
                posicion += 1
            else:
                numero_entero += int(valor_asociado_sig) - int(valor_asociado_act)
                posicion += 2
                
        return numero_entero
    