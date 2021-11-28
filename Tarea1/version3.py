
def valorNum(caracter):
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

def valorChar(num):
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
numero: str
suBase: str
"""
def pasarADecimal(numero, suBase):
    lista = []
    for char in numero:
        lista.append(char)
    lista.reverse()

    decimal = 0
    count = 0

    for n in lista:
        valor = valorNum(n)
        exponente = int(suBase) ** count
        valorEqui = exponente * valor
        decimal += valorEqui
        count += 1

    return str(decimal)

"""
numero: str
baseObjetivo: str
"""
def pasarABaseX(numero, baseObjetivo):
    numero = int(numero)
    num = ""

    while numero > 0:
        resto = numero % int(baseObjetivo)
        valorEqui = valorChar(resto)
        num = valorEqui + num
        numero = numero // int(baseObjetivo)

    return num

def pasarNumeroABinario(numero):
    decimal = pasarADecimal(numero, "2")
    binario = pasarABaseX(decimal, "2")
    return binario

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
numero: str
suBase: str
"""
def pasarNumericaABCD(numero, suBase):
    enDecimal = pasarADecimal(numero, suBase)
    lista = []
    BCD = ""
    for char in enDecimal:
        lista.append(char)
    for x in lista:
        BCD += pasarNumeroABinario(x) 
    return BCD

"""
numero: str
baseObjetivo: str
"""
def pasarBCDANumerica(numero, baseObjetivo):
    lista = []
    for char in numero:
        lista.append(char)
    lista.reverse()
    digitoBCD = ""
    enDecimal = ""

    for indice in lista:
        digitoBCD = indice + digitoBCD

        if len(digitoBCD) == 4:
            enDecimal = pasarADecimal(digitoBCD, "2") + enDecimal
            digitoBCD = ""

    enDecimal = pasarADecimal(digitoBCD, "2") + enDecimal
    enBaseObjetivo = pasarABaseX(enDecimal, baseObjetivo)

    return enBaseObjetivo

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
numero: str
solo recibe un numero en binario
"""
def pasarNumericaAGry(numero):
    #enBinario = pasarNumeroABinario(numero)
    enBinario = numero
    if enBinario != pasarNumeroABinario(numero):
        return "Entrada Invalida"

    enGray = ""
    enGray += enBinario[0]
    count = 0
    while count < len(enBinario)-1:
        sigDigito = int(enBinario[count]) + int(enBinario[count+1])
        sigDigitoEnBinario = pasarNumeroABinario(str(sigDigito))
        lista = []
        if sigDigitoEnBinario != None:
            lista.append(sigDigitoEnBinario)
            lista.reverse()
            enGray = enGray + lista[0]
            lista = []
        count += 1

    return enGray

"""
numero: str
baseObjetivo: str
"""
def pasarGryANumerica(numero, baseObjetivo):
    enBinario = ""
    enBinario += numero[0]
    countGray = 1
    countBinario = 0
    while countGray < len(numero):
        sigDigito = str(int(enBinario[countBinario]) + int(numero[countGray]))
        if sigDigito == "2":
            sigDigito = "0"
        enBinario += sigDigito
        countGray += 1
        countBinario += 1
    enDecimal = pasarADecimal(enBinario, "2")
    enBaseObjetivo = pasarABaseX(enDecimal, baseObjetivo)

    return enBaseObjetivo

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#def pasarNumericaAED3():


#def pasarEd3ANumerica():

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(pasarBCDANumerica("10001", "10"))
print(pasarNumericaABCD("221", "3"))

print(pasarNumericaAGry("10"))
