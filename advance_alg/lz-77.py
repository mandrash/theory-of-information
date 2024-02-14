import math

def mon(n: int) -> str:
    unary_representation = ""
    for i in range(len(bin(n)[3:]) + 1):
        unary_representation += "1"
    unary_representation += "0"
    return unary_representation + bin(n)[3:]

def converToBinary(num, num_bits):
    # Конвертируем число в двоичную форму
    binary = bin(num)[2:]
    
    # Проверяем, нужно ли добавлять нули в начало строки
    if len(binary) < num_bits:
        binary = '0' * (num_bits - len(binary)) + binary
    
    # Возвращаем двоичное число
    return binary

def lz77(myText: str):


    print("{:<3}|{:<4}|{:<17}|{:<11}|{:<17}|{:<25}|{:<10}".format("i", "Флаг", "Словарь", "d", "l", "Кодовая", " Затраты"))
    print("{:<3}|{:<4}|{:<17}|{:<11}|{:<17}|{:<25}|{:<10}".format("", "", "", "", "", "последовательность", " в битах"))
    print("{:-<3}|{:-<4}|{:-<17}|{:-<11}|{:-<17}|{:-<25}|{:-<10}".format("", "", "", "", "", "", ""))

    codeLength = 0
    dictW = ""
    ctr = 1
    i = 0
    while i < len(myText):
        substr = myText[i]
        flag = 0
        if substr in dictW:
            flag = 1
            if i + 1 < len(myText):
                while(substr+myText[i + 1] in dictW):
                    i += 1 
                    substr += myText[i] 


            last_occurrence = dictW.rfind(substr)

            x = 0
            if len(substr) > 1:
                x = 1

            numberOfDigits = math.ceil(math.log2(len(dictW) + x))

            buffD = str(len(dictW) - last_occurrence - 1) + "(" + str(len(dictW) + x) + ")"
            
            monoton = mon(len(substr))
            code = str(flag) + converToBinary((len(dictW) - last_occurrence - 1), numberOfDigits) + monoton[1:]

            dictW += substr[0]
            print("{:<3}|{:<4}|{:<17}|{:<11}|{:<17}|{:<25}|{:<10}".format(ctr, flag, substr, buffD, len(substr), code, len(code)))
            dictW += substr[1:]
        else: 

            ascii_char = ''.join(bin(c)[2:].rjust(8, '0') for c in substr.encode('cp1251'))
            code = str(flag) + ascii_char
            if substr == "\n":
                print("{:<3}|{:<4}|{:<17}|{:<11}|{:<17}|{:<25}|{:<10}".format(ctr, flag, "\\n", "-", "0", code, len(code)))
            else:   
                print("{:<3}|{:<4}|{:<17}|{:<11}|{:<17}|{:<25}|{:<10}".format(ctr, flag, substr, "-", "0", code, len(code)))
            dictW += substr

        codeLength += len(code)
        ctr += 1
        i += 1
    print("{:-<3}|{:-<4}|{:-<17}|{:-<11}|{:-<17}|{:-<25}|{:-<10}".format("", "", "", "", "", "", ""), end = "\n\n")

    print("l(x) = ", codeLength)

if __name__=='__main__':
    myText = "Там ступа с Бабою Ягой идёт, бредёт сама собой.\nДва дня мы были в перестрелке. Что толку в этакой безделке? Мы ждали третий день."
    # myText = "НЕ_ИМЕЙ_СТО_РУБЛЕЙ,_А_ИМЕЙ_СТО_ДРУЗЕЙ."
    lz77(myText)