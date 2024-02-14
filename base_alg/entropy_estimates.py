import math

my_text = "Там ступа с Бабою Ягой идёт, бредёт сама собой.\nДва дня мы были в перестрелке. Что толку в этакой безделке? Мы ждали третий день."

text_buff  = my_text.split(' ')
my_text = "_".join(text_buff)

text_set = sorted(set(my_text), key=my_text.index)

print(len(my_text), end= "\n\n")
 
print("i\tx(i)\tN(i)\tp(x(i))\t\tI(x(i))\t\tp(x(i))*I(x(i))")

h_x = 0

for letter in text_set:
    print(text_set.index(letter), end= "\t")
    if letter == '\n':
        print("\\n", end= "\t")
    else:
        print(letter, end= "\t")

    print(my_text.count(letter), end= "\t")

    p_x = my_text.count(letter)/len(my_text)
    print ('%.5f' % p_x, end= '\t\t')

    i_p_x = -math.log2(p_x);
    print('%.5f' % i_p_x, end= '\t\t')

    p_x_i_x = p_x * i_p_x
    print('%.5f' % p_x_i_x, end="\n\n")
    h_x += p_x_i_x


print("n = 1")
print("1) H(X^1) = H(X) = {}".format('%.5f' % h_x))
print("2) H_1(X) = H(X)/1 = {}".format('%.5f' % (h_x/1)))
print("3) H(X|X^0) = H(X) = {}".format('%.5f' % (h_x)))


text_set_in_pairs = sorted(set([my_text[i:i+2] for i in range(0, len(my_text)-1, 1)]), key=my_text.index)


print(end= "\n\n")
print(len(my_text)-1, end= "\n\n")
print("i\tx(i)y(i)\tN(i)\tp(x(i)y(i))\tI(x(i)y(i))\tp(x(i)y(i))*I(x(i)y(i))")

h_xy = 0

for pair_of_letters in text_set_in_pairs:
    print(text_set_in_pairs.index(pair_of_letters), end= "\t")
    if pair_of_letters.find("\n") != -1:
        for letter in pair_of_letters:
            if letter != "\n":
                print(letter, end= "")
            else:
                print("\\n",  end= "")
        print(end= "\t\t")
    else:
        print(pair_of_letters, end= "\t\t")

    print(my_text.count(pair_of_letters), end= "\t")

    p_xy = my_text.count(pair_of_letters)/(len(my_text)-1)
    print ('%.5f' % p_xy, end= "\t\t")

    i_p_xy = -math.log2(p_xy);
    print('%.5f' % i_p_xy, end= '\t\t')

    p_xy_i_xy = p_xy * i_p_xy
    print('%.5f' % p_xy_i_xy, end="\n\n")

    h_xy += p_xy_i_xy

print("n = 2")
print("1) H(X^2) = {}".format('%.5f' % h_xy))
print("2) H_2(X) = H(X^2)/2 = {}".format('%.5f' % (h_xy/2)))
print("3) H(X|X) = H(X^2) - H(X) = {}".format('%.5f' % (h_xy - h_x)))

text_set_in_triples = sorted(set([my_text[i:i+3] for i in range(0, len(my_text)-2, 1)]), key=my_text.index)

print(end= "\n\n")
print(len(my_text)-2, end= "\n\n")
print("i\tx(i)y(i)z(i)\tN(i)\tp(x(i)y(i)z(i))\tI(x(i)y(i)z(i))\tp(x(i)y(i)z(i))*I(x(i)y(i)z(i))")

h_xyz = 0

for triple_of_letters in text_set_in_triples:
    print(text_set_in_triples.index(triple_of_letters), end= "\t")

    if triple_of_letters.find("\n") != -1:
        for letter in triple_of_letters:
            if letter != "\n":
                print(letter, end= "")
            else:
                print("\\n",  end= "")
        print(end= "\t\t")
    else:
        print(triple_of_letters, end= "\t\t")

    print(my_text.count(triple_of_letters), end= "\t")

    p_xyz = my_text.count(triple_of_letters)/(len(my_text)-2)
    print ('%.5f' % p_xyz, end= "\t\t")

    i_p_xyz = -math.log2(p_xyz);
    print('%.5f' % i_p_xyz, end= "\t\t")

    p_xyz_i_xyz = p_xyz * i_p_xyz
    print('%.5f' % p_xyz_i_xyz, end="\n\n")

    h_xyz += p_xyz_i_xyz

print("n = 3")
print("1) H(X^3) = {}".format('%.5f' % h_xyz))
print("2) H_3(X) = H(X^3)/3 = {}".format('%.5f' % (h_xyz/3)))
print("3) H(X|X^2) = H(X^3) - H(X|X) - H(X) = {}".format('%.5f' % (h_xyz - (h_xy - h_x) - h_x)))


