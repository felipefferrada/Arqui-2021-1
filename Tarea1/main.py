
basesNumericas = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
"11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
"21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
"31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
"51", "52", "53", "54", "55", "56", "57", "58", "59", "60",
"61", "62", "63", "64"]

basesCodigos = ["bcd", "gry", "ed3", "jsn", "par", "pbt", "ham"]

"""
retorna el valor numerico de un caracter
"""
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

"""
retorna caracter correspondiente a un valor numerico
"""
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
pasa un numero en base numerica a decimal
"""
def pasarADecimal(numero, suBase):
    lista = []
    for char in numero:
        lista.append(char)
    lista.reverse()

    decimal = 0
    count = 0

    if suBase == "1":
        for x in lista:
            decimal += 1
    else:
        for n in lista:
            valor = valorNum(n)

            if valor >= int(suBase) and suBase != "1":
                return "Entrada Invalida"
            
            exponente = int(suBase) ** count
            valorEqui = exponente * valor
            decimal += valorEqui
            count += 1

    return str(decimal)


"""
numero: str
baseObjetivo: str
pasa un numero de base 10 a cualquier base 
"""
def pasarABaseX(numero, baseObjetivo):
    numero = int(numero)
    num = ""


    while numero > 0:
        if baseObjetivo == "1":
            num += "1"
            numero -= 1
        else:
            resto = numero % int(baseObjetivo)
            valorEqui = valorChar(resto)
            num = valorEqui + num
            numero = numero // int(baseObjetivo)

    return num

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
numero: str
suBase: str
pasa de una base numerica a BCD
"""
def pasarNumericaABCD(numero, suBase):
    enDecimal = pasarADecimal(numero, suBase)
    lista = []
    BCD = ""
    for char in enDecimal:
        lista.append(char)
    for x in lista:
        BCD = BCD + pasarABaseX(x, "2") 
    return BCD

"""
numero: str
baseObjetivo: str
pasa de base BCD a una numerica
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
    if "Entrada Invalida" in enDecimal:
        return "Entrada Invalida"
    enBaseObjetivo = pasarABaseX(enDecimal, baseObjetivo)

    return enBaseObjetivo

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
numero: str
suBase: str
pasa de una base numerica a Gray
"""
def pasarNumericaAGry(numero, suBase):

    enDecimal = pasarADecimal(numero, suBase)
    enBinario = pasarABaseX(enDecimal, "2")

    enGray = ""
    enGray += enBinario[0]
    count = 0

    for char in enBinario:
        if count == 0:
            count += 1
            continue
        else:
            suma = str(int(enBinario[count]) + int(enBinario[count-1]))
            if suma == "2":
                enGray += "0"
                count += 1
            else:    
                enGray += suma
                count += 1

    return enGray

"""
numero: str
baseObjetivo: str
pasa de base Gray a una numerica
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
    if "Entrada Invalida" in enDecimal:
        return "Entrada Invalida"
    enBaseObjetivo = pasarABaseX(enDecimal, baseObjetivo)

    return enBaseObjetivo

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
numero: str
suBase: str
pasa de una base numerica a Exceso de 3
"""
def pasarNumericaAED3(numero, suBase):
    enDecimal = pasarADecimal(numero, suBase)
    enED3 = ""
    for char in enDecimal:
        sumar3 = str(int(char) + 3)
        enBCD = pasarNumericaABCD(sumar3, "10")
        enED3 += enBCD

    return enED3

"""
numero: str
suBase: str
pasa de base Exceso de 3 a una numerica
"""
def pasarEd3ANumerica(numero, baseObjetivo):
    lista = []
    for char in numero:
        lista.append(char)
    lista.reverse()
    enDecimal = ""
    digito = ""

    for elemento in lista:
        digito = elemento + digito
        if len(digito) == 4:
            enDecimal3 = pasarADecimal(digito, "2")
            restar3 = str(int(enDecimal3) - 3)
            enDecimal = restar3 + enDecimal
            digito = ""

    enDecimal3 = pasarADecimal(digito, "2")
    if "Entrada Invalida" in enDecimal3:
        return "Entrada Invalida"
    restar3 = str(int(enDecimal3) - 3)
    enDecimal = restar3 + enDecimal

    enBaseObjetivo = pasarABaseX(enDecimal, baseObjetivo)

    return enBaseObjetivo

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
numero: str
suBase: str
pasa de una base numerica a Paridad
"""
def pasarNumericaAPar(numero, suBase):
    enDecimal = pasarADecimal(numero, suBase)
    enBinario = pasarABaseX(enDecimal, "2")
    count = 0
    for char in enBinario:
        if char == "1":
            count += 1

    if count % 2 == 0:
        return "1"
    else:
        return "0"

"""
numero: str
baseObjetivo: str
pasa de base Paridad a una numerica
"""
def pasarParANumerica(numero, baseObjetivo):
    enBinario = numero[:-1]
    enDecimal = pasarADecimal(enBinario, "2")
    if "Entrada Invalida" in enDecimal:
        return "Entrada Invalida"
    enBaseObjetivo = pasarABaseX(enDecimal, baseObjetivo)

    return enBaseObjetivo

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
numero: str
suBase: str
pasa de una base numerica a codigo Johnson
"""
def pasarNumericaAJhsn(numero, suBase):
    enDecimal = int(pasarADecimal(numero, suBase))
    cantidadBits = int(int(enDecimal) / 2) + 1
    lista = []
    enJohnson = ""
    while cantidadBits > 0:
        lista.append("0")
        cantidadBits = cantidadBits - 1

    count = len(lista) - 1
    flag = 0
    while enDecimal > 0:
        if flag == 0:
            lista[count] = "1"
        else:
            lista[count] = "0"

        if count == 0:
            count = len(lista)
            flag = 1

        count -= 1
        enDecimal -= 1

    for x in lista:
        enJohnson += x

    return enJohnson

"""
numero: str
baseObjetivo: str
pasa de codigo Johnson a una base numerica
"""
def pasaJhsnANumerica(numero, baseObjetivo):
    enDecimal = "0"
    enBaseObjetivo = ""
    enJohnson = pasarNumericaAJhsn(enDecimal, "10")

    while enJohnson != numero:
        enDecimal = str(int(enDecimal) + 1)
        enJohnson = pasarNumericaAJhsn(enDecimal, "10")

    enBaseObjetivo = pasarABaseX(enDecimal, baseObjetivo)

    return enBaseObjetivo

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
numero: str
suBase: str
pasa de una base numerica a PentaBit
"""
def pasarNumericaAPtb(numero, suBase):
    enDecimal = pasarADecimal(numero, suBase)
    enBinario = pasarABaseX(enDecimal, "2")

    if len(enBinario) % 5 == 0:
        return "1"
    else:
        return "0"

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
el programa corre hasta que se le ingresa por consola el caracter "-"
"""

entrada = input()
while entrada != "-":

    listaEntrada = entrada.split(" ")

    n_numero = listaEntrada[0]
    b_baseEntrada = listaEntrada[1]
    t_baseATransformar = listaEntrada[2]

#Cambio entre bases numericas LISTOOOOOOOOOO
    if b_baseEntrada in basesNumericas and t_baseATransformar in basesNumericas:

        decimal = pasarADecimal(n_numero, b_baseEntrada)

        if decimal == "Entrada Invalida":
            print(decimal)
            
        elif int(decimal) not in range(1, 1001):
            print("Entrada Invalida")

        elif int(b_baseEntrada) not in range(1, 65):
            print("Entrada Invalida")

        elif int(t_baseATransformar) not in range(1, 65):
            print("Entrada Invalida")

        else:

            if b_baseEntrada == "10":
                transformado = pasarABaseX(n_numero, t_baseATransformar)
                print("Base "+t_baseATransformar+": "+transformado)

            else:
                enDecimal = pasarADecimal(n_numero, b_baseEntrada)
                transformado = pasarABaseX(enDecimal, t_baseATransformar)
                print("Base "+t_baseATransformar+": "+transformado)


    elif b_baseEntrada in basesNumericas and t_baseATransformar in basesCodigos:

        decimal = pasarADecimal(n_numero, b_baseEntrada)

        if decimal == "Entrada Invalida":
            print("Entrada Invalida")

        elif int(decimal) not in range(1, 1001):
            print("Entrada Invalida")

        elif int(b_baseEntrada) not in range(1, 65):
            print("Entrada Invalida")
        
        else:
            if t_baseATransformar == "bcd":
                enBCD = pasarNumericaABCD(n_numero, b_baseEntrada)
                print("Codigo BCD: "+enBCD)

            elif t_baseATransformar == "gry":
                enGray = pasarNumericaAGry(n_numero, b_baseEntrada)
                posicion = pasarADecimal(enGray, "2")
                print("Codigo Gray: "+enGray)

            elif t_baseATransformar == "ed3":
                enED3 = pasarNumericaAED3(n_numero, b_baseEntrada)
                print("Codigo Exceso de 3: "+enED3)

            elif t_baseATransformar == "jsn":
                enJohnson = pasarNumericaAJhsn(n_numero, b_baseEntrada)
                print("Codigo Johnson: "+enJohnson)

            elif t_baseATransformar == "par":
                enPar = pasarNumericaAPar(n_numero, b_baseEntrada)
                print("Codigo PARIDAD: "+enPar)

            elif t_baseATransformar == "pbt":
                enPbt = pasarNumericaAPtb(n_numero, b_baseEntrada)
                print("Codigo PentaBit: "+enPbt)


    elif b_baseEntrada in basesCodigos and t_baseATransformar in basesNumericas:

        decimal = pasarADecimal(n_numero, "2")

        if decimal == "Entrada Invalida":
            print("Entrada Invalida")

        else:
            enBinario = pasarABaseX(decimal, "2")

            if enBinario != n_numero:
                print("Entrada Invalida")
    
            elif int(t_baseATransformar) not in range(1, 65):
                print("Entrada Invalida")

            else:
                if b_baseEntrada == "bcd":
                    noEnBCD = pasarBCDANumerica(n_numero, t_baseATransformar)
                    print("Base "+t_baseATransformar+": "+noEnBCD)

                elif b_baseEntrada == "gry":
                    noEnGray = pasarGryANumerica(n_numero, t_baseATransformar)
                    print("Base "+t_baseATransformar+": "+noEnGray)

                elif b_baseEntrada == "ed3":
                    noEnED3 = pasarEd3ANumerica(n_numero, t_baseATransformar)
                    print("Base "+t_baseATransformar+": "+noEnED3)

                elif b_baseEntrada == "jsn":
                    noEnJohnson = pasaJhsnANumerica(n_numero, t_baseATransformar)
                    print("Base "+t_baseATransformar+": "+noEnJohnson)

                elif b_baseEntrada == "par":
                    noEnPar = pasarParANumerica(n_numero, t_baseATransformar)
                    print("Base "+t_baseATransformar+": "+noEnPar)


    elif b_baseEntrada in basesCodigos and t_baseATransformar in basesCodigos:

        if b_baseEntrada == "bcd":
            noEnBCD = pasarBCDANumerica(n_numero, "10")

            if noEnBCD == "Entrada Invalida":
                print("Entrada Invalida")

            else:
                if t_baseATransformar == "bcd":

                    enBCD = pasarNumericaABCD(noEnBCD, "10")
                    print("Codigo BCD: "+enBCD)

                elif t_baseATransformar == "gry":

                    enGray = pasarNumericaAGry(noEnBCD, "10")
                    print("Codigo Gray: "+enGray)

                elif t_baseATransformar == "ed3":
                    enEd3 = pasarNumericaAED3(noEnBCD, "10")
                    print("Codigo Exceso de 3: "+enEd3)

                elif t_baseATransformar == "jsn":
                    enJohnson = pasarNumericaAJhsn(noEnBCD, "10")
                    print("Codigo Johnson: "+enJohnson)

                elif t_baseATransformar == "pbt":
                    enPbt = pasarNumericaAPtb(noEnBCD, "10")
                    print("Codigo PentaBit: "+enPbt)

                elif t_baseATransformar == "par":
                    enPar = pasarNumericaAPar(noEnBCD, "10")
                    print("Codigo Paridad: "+enPar)

                elif t_baseATransformar == "ham":
                    print("Codigo Hamming: ")

        elif b_baseEntrada == "gry":
            noEnGray = pasarGryANumerica(n_numero, "10")

            if noEnGray == "Entrada Invalida":
                print("Entrada Invalida")
                
            else:
                if t_baseATransformar == "bcd":
                    enBCD = pasarNumericaABCD(noEnGray, "10")
                    print("Codigo BCD: "+enBCD)

                elif t_baseATransformar == "gry":
                    enGray = pasarNumericaAGry(noEnGray, "10")
                    print("Codigo Gray: "+enGray)

                elif t_baseATransformar == "ed3":
                    enEd3 = pasarNumericaAED3(noEnGray, "10")
                    print("Codigo Exceso de 3: "+enEd3)

                elif t_baseATransformar == "jsn":
                    enJohnson = pasarNumericaAJhsn(noEnGray, "10")
                    print("Codigo Johnson: "+enJohnson)

                elif t_baseATransformar == "par":
                    enPar = pasarNumericaAPar(noEnGray, "10")
                    print("Codigo Paridad: "+enPar)

                elif t_baseATransformar == "pbt":
                    enPbt = pasarNumericaAPtb(noEnGray, "10")
                    print("Codigo PentaBit: "+enPbt)

                elif t_baseATransformar == "ham":
                    print("Codigo Hamming: ")

        elif b_baseEntrada == "ed3":
            noEnEd3 = pasarEd3ANumerica(n_numero, "10")

            if noEnEd3 == "Entrada Invalida":
                print("Entrada Invalida")
                
            else:
                if t_baseATransformar == "bcd":
                    enBCD = pasarNumericaABCD(noEnEd3, "10")
                    print("Codigo BCD: "+enBCD)

                elif t_baseATransformar == "gry":
                    enGray = pasarNumericaAGry(noEnEd3, "10")
                    print("Codigo Gray: "+enGray)

                elif t_baseATransformar == "ed3": 
                    enEd3 = pasarNumericaAED3(noEnEd3, "10")
                    print("Codigo Exceso de 3: "+enEd3)

                elif t_baseATransformar == "jsn":
                    enJohnson = pasarNumericaAJhsn(noEnEd3, "10")
                    print("Codigo Johnson: "+enJohnson)

                elif t_baseATransformar == "par":
                    enPar = pasarNumericaAPar(noEnEd3, "10")
                    print("Codigo Paridad: "+enPar)

                elif t_baseATransformar == "pbt":
                    enPbt = pasarNumericaAPtb(noEnEd3, "10")
                    print("Codigo PentaBit: "+enPbt)

                elif t_baseATransformar == "ham":
                    print("Codigo Hamming: ")

        elif b_baseEntrada == "jsn":
            noEnJohnson = pasaJhsnANumerica(n_numero, "10")

            if noEnJohnson == "Entrada Invalida":
                print("Entrada Invalida")
                
            else:
                if t_baseATransformar == "bcd":
                    enBCD = pasarNumericaABCD(noEnJohnson, "10")
                    print("Codigo BCD: "+enBCD)

                elif t_baseATransformar == "gry":
                    enGray = pasarNumericaAGry(noEnJohnson, "10")
                    print("Codigo Gray: "+enGray)

                elif t_baseATransformar == "ed3":
                    enEd3 = pasarNumericaAED3(noEnJohnson, "10")
                    print("Codigo Exceso de 3: "+enEd3)

                elif t_baseATransformar == "jsn":
                    enJohnson = pasarNumericaAJhsn(noEnJohnson, "10")
                    print("Codigo Johnson: "+enJohnson)

                elif t_baseATransformar == "par":
                    enPar = pasarNumericaAPar(noEnJohnson, "10")
                    print("Codigo Paridad: "+enPar)

                elif t_baseATransformar == "pbt":
                    enPbt = pasarNumericaAPtb(noEnJohnson, "10")
                    print("Codigo PentaBit: "+enPbt)

                elif t_baseATransformar == "ham":
                    print("Codigo Hamming: ")

        elif b_baseEntrada == "par":
            noEnPar = pasarParANumerica(n_numero, "10")

            if noEnPar == "Entrada Invalida":
                print("Entrada Invalida")
                
            else:
                if t_baseATransformar == "bcd":
                    enBCD = pasarNumericaABCD(noEnPar, "10")
                    print("Codigo BCD: "+enBCD)

                elif t_baseATransformar == "gry":
                    enGray = pasarNumericaAGry(noEnPar, "10")
                    print("Codigo Gray: "+enGray)

                elif t_baseATransformar == "ed3":
                    enEd3 = pasarNumericaAED3(noEnPar, "10")
                    print("Codigo Exceso de 3: "+enEd3)

                elif t_baseATransformar == "jsn":
                    enJohnson = pasarNumericaAJhsn(noEnPar, "10")
                    print("Codigo Johnson: "+enJohnson)

                elif t_baseATransformar == "par":
                    enPar = pasarNumericaAPar(noEnPar, "10")
                    print("Codigo Paridad: "+enPar)

                elif t_baseATransformar == "pbt":
                    enPbt = pasarNumericaAPtb(noEnPar, "10")
                    print("Codigo PentaBit: "+enPbt)

                elif t_baseATransformar == "ham":
                    print("Codigo Hamming: ")

        elif b_baseEntrada == "pbt":
            print("Codigo    ")

        elif b_baseEntrada == "ham":
            print("Codigo    ")

        else:
            print("Entrada Invalida")


    else:
        print("Entrada Invalida")

    entrada = input()
