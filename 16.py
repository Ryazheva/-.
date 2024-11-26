class TreeNode:
    # Представление узла бинарного дерева
    def __init__(self, value):
        self.value = value  # Значение узла
        self.left = None  # Левый дочерний узел
        self.right = None  # Правый дочерний узел


def build_tree(s):
    # Построение бинарного дерева из линейно-скобочной записи
    stack = []  # Стек для хранения узлов
    index = 0  # Индекс текущего символа в строке
    n = len(s)  # Длина входной строки

    while index < n:
        char = s[index]  # Текущий символ

        if char.isdigit():  # Если символ - цифра
            # Читаем полное число
            start = index
            while index < n and s[index].isdigit():
                index += 1
            value = int(s[start:index])  # Преобразуем строку в число
            node = TreeNode(value)  # Создаем узел
            stack.append(node)  # Добавляем узел в стек

        elif char == '(':  # Если встречаем открывающую скобку
            index += 1  # Пропускаем '('
            continue  # Переходим к следующему символу

        elif char == ',':  # Если встречаем запятую
            index += 1  # Пропускаем ','
            continue  # Переходим к следующему символу

        elif char == ')':  # Если встречаем закрывающую скобку
            index += 1  # Пропускаем ')'
            right = stack.pop() if stack else None  # Правый ребенок
            left = stack.pop() if stack else None  # Левый ребенок
            node = stack.pop() if stack else None  # Узел, к которому добавляем детей
            if node:  # Если узел существует
                node.left = left  # Устанавливаем левого ребенка
                node.right = right  # Устанавливаем правого ребенка
                stack.append(node)  # Возвращаем узел обратно в стек
            continue

        index += 1  # Переход к следующему символу

    return stack[0] if stack else None  # Возвращаем корень дерева


def iterative_pre_order(node):
    # Не рекурсивный прямой обход дерева с использованием стека
    if not node:
        return

    stack = [node]  # Инициализируем стек с корнем
    result = []  # Список для хранения значений узлов

    while stack:  # Пока стек не пуст
        current = stack.pop()  # Извлекаем узел из стека
        result.append(current.value)  # Добавляем значение узла в список

        # Сначала добавляем правого ребенка, затем левого, чтобы левый ребенок был на вершине стека
        if current.right:
            stack.append(current.right)  # Добавляем правого ребенка в стек
        if current.left:
            stack.append(current.left)  # Добавляем левого ребенка в стек

    print(" ".join(map(str, result)))  # Выводим значения узлов в одну строку


# Использование 
if __name__ == "__main__":
    input_string = input("Введите линейно-скобочную запись для построения бинарного дерева: ")  # Ввод с клавиатуры
    tree_root = build_tree(input_string)  # Строим дерево из строки
    iterative_pre_order(tree_root)  # Выполняем не рекурсивный прямой обход
    
"""
8(3(1,6(4,7)),10(,14(13,)))
"""
