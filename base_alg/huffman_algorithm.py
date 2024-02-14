def Frequency(text, text_set):# создание словаря вероятностей для любого кол-ва символов
    result = dict()
    for i in text_set:
        result[i] = text.count(i)/(len(text) - (len(i) - 1))
    return result

def PrintTable(result, haffman_buff):# печать таблицы
    i = 0
    sorted_result = dict(sorted(result.items()))
    sorted_haffman_buff = dict(sorted(haffman_buff.items()))

    l_i_p_i = 0

    print("i\tx(i)\t p(i)\t\tl(i)\tc(i)")
    for (key, value),(key1, value1) in zip(sorted_result.items(), sorted_haffman_buff.items()): 
        print(i, end="\t");
        i+=1
        if key.find("\n") != -1:
            for j in key:
                if j != "\n":
                    print(j, end= "")
                else:
                    print("\\n",  end= "")
            print("\t {0}".format('%.5f' % value), end="\t")
        else:
            print("{0} \t {1}".format(key, '%.5f' % value), end="\t")

        print(len(value1), end="\t")
        print(value1)
        l_i_p_i += (value * len(value1))
    
    print("Средняя длина кодового слова = ", '%.7f' % l_i_p_i)
    print("Средняя скорость = ", '%.7f' % (l_i_p_i/len(key)), end="\n\n")

        
class Node(object): # Создать класс узла
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None 
        self.rchild = None
         
class HuffmanTree(object):
    def __init__(self, text):
        self.leaves = [Node(key, value) for key, value in text.items()]
        self.Buffer = []
        self.ServiceBuffer = []
        while len(self.leaves) > 1:
            self.leaves.sort(key= lambda node: node.value, reverse=True)
            n = Node(value=(self.leaves[-1].value + self.leaves[-2].value))
            n.lchild = self.leaves.pop(-1)
            n.rchild = self.leaves.pop(-1)
            self.leaves.append(n)

        self.root = self.leaves[0]
        self.Buffer = []
        self.ServiceBuffer = ""

    def Hu_generate(self, tree, length, result):
        node = tree
        if (not node):
            return 
        elif node.name:
            buffer = ''
            self.ServiceBuffer += "1"

            for i in range(length):
                buffer += str(self.Buffer[i])

            result[node.name] = buffer
            return 

        self.Buffer.append(0)
        self.ServiceBuffer += "0"
        self.Hu_generate(node.rchild, length + 1, result)
        self.Buffer.pop()
        self.Buffer.append(1)
        self.Hu_generate(node.lchild, length + 1, result)
        self.Buffer.pop()


if __name__=='__main__':
    my_text = "НЕ_ИМЕЙ_СТО_РУБЛЕЙ,_А_ИМЕЙ_СТО_ДРУЗЕЙ."
    text_buff  = my_text.split(' ')
    my_text = "_".join(text_buff)

    text_set = sorted(set(my_text), key=my_text.index)
    text_set_in_pairs = sorted(set([my_text[i:i+2] for i in range(0, len(my_text)-1, 1)]), key=my_text.index)
    text_set_in_triples = sorted(set([my_text[i:i+3] for i in range(0, len(my_text)-2, 1)]), key=my_text.index)

    frequency_dict_1 = Frequency(my_text, text_set)
    frequency_dict_2 = Frequency(my_text, text_set_in_pairs)
    frequency_dict_3 = Frequency(my_text, text_set_in_triples)

    tree = HuffmanTree(frequency_dict_1)
    result = dict()
    tree.Hu_generate(tree.root,0 ,result)

    PrintTable(frequency_dict_1, result)

