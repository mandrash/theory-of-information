import math
from math import copysign, fabs, floor, isfinite, modf, ceil
from copy import deepcopy

def Frequency(text, text_set):# создание словаря вероятностей для любого кол-ва символов
    result = dict()
    for i in text_set:
        result[i] = text.count(i)/(len(text) - (len(i) - 1))
    
    return dict(sorted(result.items(), key= lambda item: item[1], reverse= True))
    
def float_to_bin(f):
    if not isfinite(f):
        return repr(f)  # inf nan

    sign = '-' * (copysign(1.0, f) < 0)
    frac, fint = modf(fabs(f))  # split on fractional, integer parts
    n, d = frac.as_integer_ratio()  # frac = numerator / denominator
    assert d & (d - 1) == 0  # power of two
    return f'{sign}{floor(fint):b}.{n:0{d.bit_length()-1}b}'

def Commulative_Frequency(frequency_dict):
    cumulative_frequences = list(frequency_dict.values())

    i = 0
    for x in cumulative_frequences:
        j = 0
        buff = 0.0
        for key, value in frequency_dict.items():
            if (j < i):
                buff  += value
                j += 1
            else:
                break
        cumulative_frequences[i] = buff
        i+=1
    
    return cumulative_frequences
    
def Shennon(frequency_dict, cumulative_frequences_list):

    codes = cumulative_frequences_list
    buff_cf = deepcopy(cumulative_frequences_list)

    for i in range(0, len(cumulative_frequences_list)):
        codes[i] = float_to_bin(cumulative_frequences_list[i])
    
    code_lengths = []
    for key, value in frequency_dict.items():
        code_lengths.append(ceil(-math.log2(value)))

    
    for i in range(0, len(code_lengths)):
        buff = ""
        a = codes[i]
        for j in range(2, code_lengths[i]+2):
            if j < len(a):
                buff += a[j]
            else:
                buff += '0'
        codes[i] = buff

    print("i\tx(i)\t p(i)\t\tq(i)\t\tI(x(i))\t\tl(i)\tc(i)")

    i = 0
    l_i_p_i = 0

    for key, value in frequency_dict.items():
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

        print('%.5f' % buff_cf[i], end="\t\t")
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

    frequency_dict_1 = Frequency(my_text, text_set)
    frequency_dict_2 = Frequency(my_text, text_set_in_pairs)
    frequency_dict_3 = Frequency(my_text, text_set_in_triples)

    cumulative_frequences_list_1 = Commulative_Frequency(frequency_dict_1)
    cumulative_frequences_list_2 = Commulative_Frequency(frequency_dict_2)
    cumulative_frequences_list_3 = Commulative_Frequency(frequency_dict_3)
    
    Shennon(frequency_dict_1, cumulative_frequences_list_1)
    Shennon(frequency_dict_2, cumulative_frequences_list_2)
    Shennon(frequency_dict_3, cumulative_frequences_list_3)
    