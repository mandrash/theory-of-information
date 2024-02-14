import math
from math import copysign, fabs, floor, isfinite, modf, ceil
from copy import deepcopy


def float_to_bin(f):
    if not isfinite(f):
        return repr(f) 

    sign = '-' * (copysign(1.0, f) < 0)
    frac, fint = modf(fabs(f))  # split on fractional, integer parts
    n, d = frac.as_integer_ratio()  # frac = numerator / denominator
    assert d & (d - 1) == 0  # power of two
    return f'{sign}{floor(fint):b}.{n:0{d.bit_length()-1}b}'

def Probability(text, text_set):# создание словаря вероятностей для любого кол-ва символов
    result = dict()
    for i in text_set:
        result[i] = text.count(i)/(len(text) - (len(i) - 1))

    return result

def Commulative_Probability(probability_dict):
    cumulative_probability = deepcopy(probability_dict)

    i = 0
    for key, value in cumulative_probability.items():
        j = 0
        buff = 0.0
        for key1, value1 in probability_dict.items():
            if (j < i):
                buff  += value1
                j += 1
            else:
                break
        cumulative_probability[key] = buff
        i+=1

    return cumulative_probability


def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip(*args)

def Arithmetic_coding(my_text, probability_dict, cumulative_probabilities_dict, n):

    print("Код: ", end="")
    buff = [''.join(i) for i in grouper(my_text, 6)]
    all_code_length = 0
    for word in buff:
        cort = [''.join(i) for i in grouper(word, n)]

        F = 0
        G = 1

        for x in cort:
            F += cumulative_probabilities_dict[x] * G
            G *= probability_dict[x]
        
        code_length = ceil(-math.log2(G)+1)
        all_code_length += code_length
        bin_code = float_to_bin(F + G/2)

        code = ""

        for i in range(0, code_length):
            for j in range(2, code_length+2):
                if j < len(bin_code):
                    code += bin_code[j]
                else:
                    code += '0'
        
        
    print(code, end="")
    print(end="\n\n")

    l_i_p_i = all_code_length/len(my_text)

    print("Длина кода = ", all_code_length)
    print("Средняя длина кодового слова = ", '%.7f' % l_i_p_i)
    print("Средняя скорость = ", '%.7f' % (all_code_length/len(buff)), end="\n\n")



if __name__=='__main__':
    my_text = "Там ступа с Бабою Ягой идёт, бредёт сама собой.\nДва дня мы были в перестрелке. Что толку в этакой безделке? Мы ждали третий день."

    number_of_spaces = (6 - len(my_text) % 6)
    my_text += ("_" * number_of_spaces)

    text_buff  = my_text.split(' ')
    my_text = "_".join(text_buff)

    text_set = sorted(set(my_text), key=my_text.index)
    text_set_in_pairs = sorted(set([my_text[i:i+2] for i in range(0, len(my_text)-1, 1)]), key=my_text.index)
    text_set_in_triples = sorted(set([my_text[i:i+3] for i in range(0, len(my_text)-2, 1)]), key=my_text.index)

    probability_dict_1 = Probability(my_text, text_set)
    probability_dict_2 = Probability(my_text, text_set_in_pairs)
    probability_dict_3 = Probability(my_text, text_set_in_triples)

    cumulative_probabilities_dict_1 = Commulative_Probability(probability_dict_1)
    cumulative_probabilities_dict_2 = Commulative_Probability(probability_dict_2)
    cumulative_probabilities_dict_3 = Commulative_Probability(probability_dict_3)

    Arithmetic_coding(my_text, probability_dict_1, cumulative_probabilities_dict_1, 1)
    Arithmetic_coding(my_text, probability_dict_2, cumulative_probabilities_dict_2, 2)
    Arithmetic_coding(my_text, probability_dict_3, cumulative_probabilities_dict_3, 3)

