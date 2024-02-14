import math

def converToBinary(num, num_bits):
    # Конвертируем число в двоичную форму
    binary = bin(num)[2:]
    
    # Проверяем, нужно ли добавлять нули в начало строки
    if len(binary) < num_bits:
        binary = '0' * (num_bits - len(binary)) + binary
    
    # Возвращаем двоичное число
    return binary

def lz78(myText: str):
    dictionary = ['#']

    print("{:<4}|{:<17}|{:<20}|{:<25}|{:<10}".format(" Шаг", " Словарь", " Номер", " Кодовые", " Затраты"))
    print("{:<4}|{:<17}|{:<20}|{:<25}|{:<10}".format("", "", " слова(j)", " символы", " в битах"))
    print("{:-<4}|{:-<17}|{:-<20}|{:-<25}|{:-<10}".format("", "", "", "", ""))

    i = 0
    print("{:<4}|{:<17}|{:<20}|{:<25}|{:<10}".format(i, dictionary[i], "-", "-", "-"))

    i+=1

    strctr = 0
    codeLen = 0

    while strctr < len(myText):
        substr = myText[strctr]

        if substr in dictionary:
            
            for index in range(len(dictionary)-1, -1, -1):
                if dictionary[index] == substr:
                    last_index = index
                    break
            
            if strctr + 1 < len(myText):
                while substr in dictionary:
                    strctr += 1
                    substr += myText[strctr]

                if strctr != len(myText) - 1:
                    strctr -= 1

                buffstr = substr[:-1]
                
                for index in range(len(dictionary)-1, -1, -1):
                    if dictionary[index] == buffstr:
                        last_index = index
                        break
            
            code = converToBinary(last_index, math.ceil(math.log2(len(dictionary) - 1)))

            dictionary.append(substr)
            
            print("{:<4}|{:<17}|{:<20}|{:<25}|{:<10}".format(i, substr, last_index, code, len(code)))
        else:
            ascii_char = ''.join(bin(c)[2:].rjust(8, '0') for c in substr.encode('cp1251'))
            if(len(dictionary) > 1):
                code =  "0" * math.ceil(math.log2(len(dictionary) - 1)) + ascii_char
            else: 
                code = ascii_char

            dictionary.append(substr)
            if substr == "\n":
                print("{:<4}|{:<17}|{:<20}|{:<25}|{:<10}".format(i, "\\n", "0", code, len(code)))
            else:   
                print("{:<4}|{:<17}|{:<20}|{:<25}|{:<10}".format(i, dictionary[i], "0", code, len(code)))
           

        i+=1
        codeLen += len(code)
        strctr += 1
    
    print("{:-<4}|{:-<17}|{:-<20}|{:-<25}|{:-<10}".format("", "", "", "", ""), end = "\n\n")
    print("l(x) = ", codeLen)

if __name__=='__main__':
    myText = "Там ступа с Бабою Ягой идёт, бредёт сама собой.\nДва дня мы были в перестрелке. Что толку в этакой безделке? Мы ждали третий день."
    # myText = "НЕ_ИМЕЙ_СТО_РУБЛЕЙ,_А_ИМЕЙ_СТО_ДРУЗЕЙ."
    lz78(myText)