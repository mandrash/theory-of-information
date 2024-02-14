import math
import os

def mon(n: int) -> str:
    unary_representation = ""
    for i in range(len(bin(n)[3:]) + 1):
        unary_representation += "1"
    unary_representation += "0"
    return unary_representation + bin(n)[3:]

def stackOfBooks(myText: str):
    asciiDict = {}
    for i in range(191):
        asciiDict[chr(i)] = i
    for i, char in enumerate('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'):
        asciiDict[char] = i + 191

    books = asciiDict.copy()

    os.system("clear")

    print("{:<8}|{:<7}|{:<17}|{:<13}|{:<18}|{:<6}".format("i", "x(i)", "Номер в ASCII", "Номер в", "с(i)-кодовое", "l(i)"))
    print("{:<8}|{:<7}|{:<17}|{:<13}|{:<18}|{:<6}".format("", "", "", "стопке книг", "слово", ""))
    print("{:-<8}|{:-<7}|{:-<17}|{:-<13}|{:-<18}|{:-<6}".format("", "", "", "", "", ""))
    codeLength = 0
    c = ""
    i = 1 
    for char in myText:
        buffAsciiNumber = books.pop(char)
        asciiCurrentChar = {char: 0}

        for key, value in books.items():
            if value <= buffAsciiNumber:
                books[key] += 1
                
        books = {**asciiCurrentChar, **books}
        monCode = mon(buffAsciiNumber)
        if(char == '\n'):
            print("{:<8}|{:<7}|{:<17}|{:<13}|{:<18}|{:<6}".format(i, "\\n", asciiDict[char], buffAsciiNumber, monCode, len(monCode)))
        else:
            print("{:<8}|{:<7}|{:<17}|{:<13}|{:<18}|{:<6}".format(i, char, asciiDict[char], buffAsciiNumber, monCode, len(monCode)))
        i += 1
        codeLength += len(monCode)
        c += monCode

    print("{:-<8}|{:-<7}|{:-<17}|{:-<13}|{:-<18}|{:-<6}".format("", "", "", "", "", ""))
    print("{:<8}|{:<7}|{:<17}|{:<13}|{:<18}|{:<6}".format("сумма", "", "", "", "", codeLength))
    print(end="\n\n")
    print("c(x) = ", c)
if __name__=='__main__':
    myText = "Там ступа с Бабою Ягой идёт, бредёт сама собой.\nДва дня мы были в перестрелке. Что толку в этакой безделке? Мы ждали третий день."

    stackOfBooks(myText)
