# Реализация класса Node
class Node:
    """ Это узел """
    def __init__(self, data, next_node=None):
        self.data = data  # тут данные
        self.next_node = next_node # тут ссылка на следующий

# Реализация класса LinkedList
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Метод для добавления узла в начало связанного списка
    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    # Метод для добавления узла в конец связанного списка
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node

    # Метод для вывода данных из связанного списка
    def print_ll(self):
        ll_string = ''
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f' {str(node.data)} ->'
            node = node.next_node

        ll_string += ' None'
        print(ll_string)

    # Метод для возвращения списка с данными, содержащимися в односвязном списке
    def to_list(self):
        ll_list = []
        node = self.head
        while node:
            ll_list.append(node.data)
            node = node.next_node
        return ll_list

    #возвращает первый найденный в LinkedList словарь с ключом id, значение которого равно переданному в метод значению. 
    def get_data_by_id(self, id_value):
        try:
            node = self.head
            while node:
                if node.data['id'] == id_value:
                    return node.data
                node = node.next_node
            return None
        except TypeError:
            print('Данные не являются словарем или в словаре нет id.')