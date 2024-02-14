my_text = "Там ступа с Бабою Ягой идёт, бредёт сама собой.\nДва дня мы были в перестрелке. Что толку в этакой безделке? Мы ждали третий день."
text_buff  = my_text.split(' ')
my_text = "_".join(text_buff)

text_set = sorted(set(my_text), key=my_text.index)


print(len(my_text), end= "\n\n")

print("i\tx(i)\tN(i)\tp(x(i))")
for letter in text_set:
    print(text_set.index(letter), end= "\t")
    if letter == '\n':
        print("\\n", end= "\t")
    else:
        print(letter, end= "\t")
    print(my_text.count(letter), end= "\t")
    print ('%.5f' % (my_text.count(letter)/len(my_text)))



text_set_in_pairs = sorted(set([my_text[i:i+2] for i in range(0, len(my_text)-1, 1)]), key=my_text.index)


print(end= "\n\n")
print(len(my_text)-1, end= "\n\n")
print("i\tx(i)y(i)\tN(i)\tp(x(i)y(i))")

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
    print ('%.5f' % (my_text.count(pair_of_letters)/(len(my_text)-1)))

text_set_in_triples = sorted(set([my_text[i:i+3] for i in range(0, len(my_text)-2, 1)]), key=my_text.index)

print(end= "\n\n")
print(len(my_text)-2, end= "\n\n")
print("i\tx(i)y(i)z(i)\tN(i)\tp(x(i)y(i)z(i))")
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
    print ('%.5f' % (my_text.count(triple_of_letters)/(len(my_text)-2)))

