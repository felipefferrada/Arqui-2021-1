
"""
Retorna el valor numerico de la letra o caracter entregado
"""
def Valor_Num(caracter):
    mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minus = "abcdefghijklmnopqrstuvwxyz"

    if caracter in mayus:
        valor = ord(caracter) - 29
    elif caracter in minus:
        valor = ord(caracter) - 87
    elif caracter == "+":
        valor = 62
    elif caracter == "?":
        valor = 63 
    else:
        return int(caracter)

    return valor

"""
Retorna la letra o el caracter correspondiente al valor entregado
"""
def Valor_Char(num):
    equi_minus = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
        "16": "g",
        "17": "h",
        "18": "i",
        "19": "j",
        "20": "k",
        "21": "l",
        "22": "m",
        "23": "n",
        "24": "o",
        "25": "p",
        "26": "q",
        "27": "r",
        "28": "s",
        "29": "t",
        "30": "u",
        "31": "v",
        "32": "w",
        "33": "x",
        "34": "y",
        "35": "z"
    }
    equi_mayus = {
        "36": "A",
        "37": "B",
        "38": "C",
        "39": "D",
        "40": "E",
        "41": "F",
        "42": "G",
        "43": "H",
        "44": "I",
        "45": "J",
        "46": "K",
        "47": "L",
        "48": "M",
        "49": "N",
        "50": "O",
        "51": "P",
        "52": "Q",
        "53": "R",
        "54": "S",
        "55": "T",
        "56": "U",
        "57": "V",
        "58": "W",
        "59": "X",
        "60": "Y",
        "61": "Z"
    }
    equi_symbols = {
        "62": "+",
        "63": "?"
    }
    valor = str(num)

    if valor in equi_mayus:
        return equi_mayus[valor]

    elif valor in equi_minus:
        return equi_minus[valor]

    elif valor in equi_symbols:
        return equi_symbols[valor]
    else:
        return valor

"""
Transforma de base decimal a cualquier base entre 1 y 64
"""
def Decimal_a_BaseX(decimal, base):
    numero = ""
    while decimal > 0:
        residuo = decimal % base
        verdadero_caracter = Valor_Char(residuo)
        numero = verdadero_caracter + numero
        decimal = int(decimal / base)
    return numero

"""
Transforma de una base entre 1 y 64 a decimal
"""
def BaseX_a_Decimal(num, base):
    str_num = str(num)
    str_num = str_num[::-1]
    numero = 0
    count = 0

    for n in str_num:
        valor = Valor_Num(n)
        exp = base ** count
        equivalencia = exp * valor
        numero += equivalencia
        count += 1

    return numero

#print(Decimal_a_BaseX(1000, 2))
#print(BaseX_a_Decimal("1111101000", 2))

n = input("Ingrese su numero: ")
b = input("En que base se encuentra?: ")
t = input("A que base lo desea transformar?: ")

bases_posibles = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
"11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
"21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
"31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
"51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
"61", "62", "63", "64"]

if b in bases_posibles:
    if t in bases_posibles:
        if int(b) == 10:                                                    #ver si es de decimal a baseX o baseX a decimal
            numero_transformado = Decimal_a_BaseX(int(n), int(t))
            print("Su numero en base "+(t)+" es:", numero_transformado)
        else:
            numero_decimal = BaseX_a_Decimal(n, int(b))
            numero_transformado = Decimal_a_BaseX(numero_decimal, int(t))

            print("Su numero en base "+(t)+" es:", numero_transformado)
