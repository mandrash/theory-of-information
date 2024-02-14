import math
from math import copysign, fabs, floor, isfinite, modf, ceil
from copy import deepcopy


def Probability(text, text_set):# создание словаря вероятностей для любого кол-ва символов
    result = dict()
    for i in text_set:
        result[i] = text.count(i)/(len(text) - (len(i) - 1))

    return result

def float_to_bin(f):
    if not isfinite(f):
        return repr(f)  # inf nan

    sign = '-' * (copysign(1.0, f) < 0)
    frac, fint = modf(fabs(f))  # split on fractional, integer parts
    n, d = frac.as_integer_ratio()  # frac = numerator / denominator
    assert d & (d - 1) == 0  # power of two
    return f'{sign}{floor(fint):b}.{n:0{d.bit_length()-1}b}'

def Commulative_Probability(probability_dict):
    cumulative_probability = list(probability_dict.values())

    i = 0
    for x in cumulative_probability:
        j = 0
        buff = 0.0
        for key, value in probability_dict.items():
            if (j < i):
                buff  += value
                j += 1
            else:
                break
        cumulative_probability[i] = buff
        i+=1

    return cumulative_probability

def Auxiliary_Probability(probability_dict, cumulative_probability_list):
    auxiliary_probabilities = list()
    i = 0 
    for key, value in probability_dict.items():
        auxiliary_probabilities.append(cumulative_probability_list[i]+(value/2))
        i+=1

    return auxiliary_probabilities

def Gilbert_Moore(probability_dict, cumulative_probability_list, auxiliary_probabilities_list):
    code_lengths = []
    for key, value in probability_dict.items():
        code_lengths.append(ceil(-math.log2(value)+1))

    codes = []
    buff_aux = deepcopy(auxiliary_probabilities_list)
    for i in range(0, len(auxiliary_probabilities_list)):
        codes.append(float_to_bin(auxiliary_probabilities_list[i]))

    for i in range(0, len(code_lengths)):
        buff = ""
        a = codes[i]
        for j in range(2, code_lengths[i]+2):
            if j < len(a):
                buff += a[j]
            else:
                buff += '0'
        codes[i] = buff


    print("i\tx(i)\t p(i)\t\tq(i)\t\taux(i)\t\tI(x(i))\t\tl(i)\tc(i)", end="\n\n")

    i = 0
    l_i_p_i = 0

    for key, value in probability_dict.items():
        print(i, end="\t");
        if key.find("\n") != -1:
            for j in key:
                if j != "\n":
                    print(j, end= "")
                else:
                    print("\\n",  end= "")
            print("\t {0}".format('%.5f' % value), end="\t")
        else:
            print("{0} \t {1}".format(key, '%.5f' % value), end="\t")
            
        print('%.5f' % cumulative_probability_list[i], end="\t\t")
        print('%.5f' % buff_aux[i], end="\t\t")
        print('%.5f' % -math.log2(value), end="\t\t")
        print(code_lengths[i], end="\t")
        print(codes[i], end= "\n\n")

        l_i_p_i += (value * code_lengths[i])
        i+=1
    
    print("Средняя длина кодового слова = ", '%.7f' % l_i_p_i)
    print("Средняя скорость = ", '%.7f' % (l_i_p_i/len(key)), end="\n\n")
if __name__=='__main__':
    my_text = "Там ступа с Бабою Ягой идёт, бредёт сама собой.\nДва дня мы были в перестрелке. Что толку в этакой безделке? Мы ждали третий день."
    text_buff  = my_text.split(' ')
    my_text = "_".join(text_buff)

    text_set = sorted(set(my_text), key=my_text.index)
    text_set_in_pairs = sorted(set([my_text[i:i+2] for i in range(0, len(my_text)-1, 1)]), key=my_text.index)
    text_set_in_triples = sorted(set([my_text[i:i+3] for i in range(0, len(my_text)-2, 1)]), key=my_text.index)

    probability_dict_1 = Probability(my_text, text_set)
    probability_dict_2 = Probability(my_text, text_set_in_pairs)
    probability_dict_3 = Probability(my_text, text_set_in_triples)

    cumulative_probabilities_list_1 = Commulative_Probability(probability_dict_1)
    cumulative_probabilities_list_2 = Commulative_Probability(probability_dict_2)
    cumulative_probabilities_list_3 = Commulative_Probability(probability_dict_3)
    
    auxiliary_probabilities_list_1 = Auxiliary_Probability(probability_dict_1, cumulative_probabilities_list_1)
    auxiliary_probabilities_list_2 = Auxiliary_Probability(probability_dict_2, cumulative_probabilities_list_2)
    auxiliary_probabilities_list_3 = Auxiliary_Probability(probability_dict_3, cumulative_probabilities_list_3)

    Gilbert_Moore(probability_dict_1, cumulative_probabilities_list_1, auxiliary_probabilities_list_1)
    Gilbert_Moore(probability_dict_2, cumulative_probabilities_list_2, auxiliary_probabilities_list_2)
    Gilbert_Moore(probability_dict_3, cumulative_probabilities_list_3, auxiliary_probabilities_list_3)