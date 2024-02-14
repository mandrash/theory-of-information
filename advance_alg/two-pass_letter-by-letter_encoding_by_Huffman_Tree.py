import math

def Frequency(text, text_set):# создание словаря вероятностей для любого кол-ва символов
    result = dict()
    for i in text_set:
        result[i] = text.count(i)/(len(text) - (len(i) - 1))
    return result
        
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

    def Hu_generate(self, tree, length, result):
        node = tree
        if (not node):
            return 
        elif node.name:
            buffer = ''
            for i in range(length):
                buffer += str(self.Buffer[i])

            result[node.name] = buffer
            return 

        self.Buffer.append(1)
        self.Hu_generate(node.rchild, length + 1, result)
        self.Buffer.pop()
        self.Buffer.append(0)
        self.Hu_generate(node.lchild, length + 1, result)
        self.Buffer.pop()

    def Hu_sort(self, root):
        sorted_leaves = dict()

        def traverse(node):
            if node.name is None:
                sorted_leaves[node] = max(traverse(node.lchild) + 1, traverse(node.rchild) + 1)
                return sorted_leaves[node]
            else:
                sorted_leaves[node] = 0
                return sorted_leaves[node]

        traverse(root)

        def bfs(root):
            queue = [root]
            visited = set() 
            prev_level_nodes = []
            while queue:
                current_level_nodes = []
                current_level_size = len(queue)
                for i in range(current_level_size):
                    node = queue.pop(0)
                    if node not in visited:
                        visited.add(node)
                        current_level_nodes.append(node)
                        if node.lchild:
                            queue.append(node.lchild)
                        if node.rchild:
                            queue.append(node.rchild)
                sorted_nodes = sorted(current_level_nodes, key=lambda n: (sorted_leaves[n], -n.value))
                prev_level_nodes = sorted(prev_level_nodes, key=lambda n: (sorted_leaves[n], -n.value))


                j = 0
                for node in prev_level_nodes:
                    if node.name is None:
                            node.lchild = sorted_nodes[j]
                            j+=1
                            node.rchild = sorted_nodes[j]
                            j+=1
                prev_level_nodes = current_level_nodes
        bfs(root)

def print_huffman_table(text):
    freq_dict = Frequency(text, set(text))
    huffman = HuffmanTree(freq_dict)
    result= dict()
    
    huffman.Hu_sort(huffman.root)
    huffman.Hu_generate(huffman.root, 0, result)
    

    # print("Character\tFrequency\tCode")
    # for char in result.keys():
    #     if char == "\n":
    #         print(f"\\n\t\t{freq_dict[char]:.5f}\t\t{result[char]}")
    #     else:
    #         print(f"{char}\t\t{freq_dict[char]:.5f}\t\t{result[char]}")

    print("--------|---------------|---------------|---------------|---------------|---------------")
    print(" Ярус\t| Общее \t| Число    \t| Диапазон   \t| Затраты в\t| Комбинации для")
    print("     \t| число \t| концевых \t| значений ni\t| битах    \t| концевых")
    print("     \t| вершин\t| вершин ni\t|            \t|          \t| вершин")
    print("--------|---------------|---------------|---------------|---------------|---------------")
    
    def bfs(root):
        bit_sum = 0
        comb_sum = 0
        ascii_symb_count = 256
        queue = [root]
        visited = set()
        cur_top = 0
        while queue:
            current_level_nodes = []
            current_level_size = len(queue)
            cur_named_nodes = 0
            for i in range(current_level_size):
                node = queue.pop(0)
                if node not in visited:
                    visited.add(node)
                    current_level_nodes.append(node)
                    if node.name != None:
                        cur_named_nodes += 1
                    if node.lchild:
                        queue.append(node.lchild)
                    if node.rchild:
                        queue.append(node.rchild)
            
            print(" ",cur_top,"\t|", " ",current_level_size, '\t\t|', " ",cur_named_nodes, '\t\t|',' 0..',current_level_size,'\t\t|', sep='', end='')
            
            named_nodes_comb = None
            if cur_named_nodes > 0:
                named_nodes_comb = math.ceil(math.log2(math.comb(ascii_symb_count,cur_named_nodes)))
                ascii_symb_count -= cur_named_nodes
                comb_sum += named_nodes_comb

            bit = math.ceil(math.log2(current_level_size + 1))
            if named_nodes_comb:
                print(" ",bit,"\t\t|", " ",named_nodes_comb)
            else:
                print(" ",bit,"\t\t|")

            bit_sum += bit
            cur_top+=1
        print("--------|---------------|---------------|---------------|---------------|---------------")
        print("Всего\t|              \t|             \t|            \t|", bit_sum,"          \t| ", comb_sum)
        print("--------|---------------|---------------|---------------|---------------|---------------")

        l1 = bit_sum + comb_sum
        print("\n\n")
        c2 = ""
        print("c2(x) = ", end = '')
        for i in my_text:
            code = result.get(i)
            print(code, end="")
            c2 += code
        print("\n\n")
        print("l1(x) = ", bit_sum, " + ", comb_sum, " = ", l1)
        print("l2(x) = ", len(c2))
        print("l(x) = l1(x) + l2(x) = ", l1 + len(c2))

    bfs(huffman.root)

if __name__=='__main__':
    my_text = "Там ступа с Бабою Ягой идёт, бредёт сама собой.\nДва дня мы были в перестрелке. Что толку в этакой безделке? Мы ждали третий день."
    my_text = "_".join(my_text.split(' '))
    print_huffman_table(my_text)
