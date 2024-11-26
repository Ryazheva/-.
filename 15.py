class Node:
    # Конструктор класса Node, принимающий значение узла
    def __init__(self, key):
        # Инициализация левого потомка
        self.left = None
        # Инициализация правого потомка
        self.right = None
        # Присваивание значения узлу
        self.val = key

    # Метод обхода дерева в прямом порядке (pre-order traversal)
    def traversePreOrder(self) -> None:
        # Печать значения текущего узла
        print(self.val, end=' ')
        # Рекурсивный вызов метода для левого поддерева, если оно существует
        if self.left:
            self.left.traversePreOrder()
        # Рекурсивный вызов метода для правого поддерева, если оно существует
        if self.right:
            self.right.traversePreOrder()

    # Метод обхода дерева в ицентральном порядке(in-order traversal)
    def traverseInOrder(self) -> None:
        # Рекурсивный вызов метода для левого поддерева, если оно существует
        if self.left:
            self.left.traverseInOrder()
        # Печать значения текущего узла
        print(self.val, end=' ')
        # Рекурсивный вызов метода для правого поддерева, если оно существует
        if self.right:
            self.right.traverseInOrder()

    # Метод обхода дерева в концевом порядке (post-order traversal)
    def traversePostOrder(self) -> None:
        # Рекурсивный вызов метода для левого поддерева, если оно существует
        if self.left:
            self.left.traversePostOrder()
        # Рекурсивный вызов метода для правого поддерева, если оно существует
        if self.right:
            self.right.traversePostOrder()
        # Печать значения текущего узла
        print(self.val, end=' ')


def create_tree(string: str) -> Node:
    # Вызов функции для построения поддерева, начиная с начала строки до её конца
    return create_subtree(string, 0, len(string))


def find_right_subtree(string: str, start: int, end: int):
    # Счётчик скобок для отслеживания вложенности
    bracket_counter = -1
    # Цикл для нахождения индекса начала правой ветви
    while True:
        # Если достигли конца строки, возвращаем -1
        if start >= end:
            return -1
        # Если встретили запятую и счётчик скобок равен нулю, значит нашли начало правой ветви
        if (string[start] == ',') and (bracket_counter == 0):
            return start + 1
        # Увеличиваем счётчик при встрече открывающей скобки
        if string[start] == '(':
            bracket_counter += 1
        # Уменьшаем счётчик при встрече закрывающей скобки
        if string[start] == ')':
            bracket_counter -= 1
        # Переход к следующему символу
        start += 1


def create_subtree(string: str, start: int, end: int) -> Node:
    # Пропуск пробелов и открывающих скобок в начале строки
    while string[start] == ' ' or string[start] == '(':
        start += 1
    # Если достигли конца строки, возвращаемся без создания узла
    if start >= end:
        return

    # Формируем число из символов строки
    number = ''
    while string[start] in '1234567890':
        number += string[start]
        start += 1
        # Если достигли конца строки, создаем узел с текущим числом и возвращаем его
        if start >= end:
            return Node(int(number))

    # Создание нового узла с полученным значением
    node = Node(int(number))

    # Поиск индекса начала правой ветви
    right_subtree_index = find_right_subtree(string, start, end) - 1

    # Если не найдено начало правой ветви, выбрасывается исключение
    if right_subtree_index == -1:
        raise Exception("Wrong bracket notation string!")

    # Если правая ветвь найдена, рекурсивно строятся левое и правое поддеревья
    if right_subtree_index:
        node.left = create_subtree(string, start + 1, right_subtree_index)
        node.right = create_subtree(string, right_subtree_index + 1, end - 1)

    # Возвращение созданного узла
    return node


if __name__ == "__main__":
    # Чтение пользовательского ввода и создание бинарного дерева
    bt = create_tree(input("Введите строку с линейными скобками: ").strip())

    # Вывод заголовков и выполнение обходов дерева
    print('Прямой порядок:')
    bt.traversePreOrder()
    print("\n")

    print('Центральный порядок:')
    bt.traverseInOrder()
    print("\n")

    print('Концевой порядок:')
    bt.traversePostOrder()

"""
8(3(1,6(4,7)),10(,14(13,)))
"""
