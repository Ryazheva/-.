
""" 
В бинарном дереве поиска для каждого узла выполняются следующие условия: 
1. Левое поддерево узла содержит только узлы с значениями меньше, чем значение самого узла. 
2. Правое поддерево узла содержит только узлы с значениями больше, чем значение самого узла. 
"""

class TreeNode:
    """Класс для представления узла бинарного дерева."""

    def __init__(self, value):
        self.value = value  # Значение узла 
        self.left = None  # Левый дочерний узел 
        self.right = None  # Правый дочерний узел 


def build_tree(s):
    """Строит бинарное дерево из линейно-скобочной записи."""
    stack = []  # Стек для хранения узлов 
    index = 0  # Индекс текущего символа в строке 
    n = len(s)  # Длина входной строки 

    while index < n:
        char = s[index]  # Текущий символ 

        if char.isdigit() or (char == '-' and index + 1 < n and s[index + 1].isdigit()):
            # Если символ - цифра или отрицательное число 
            start = index
            while index < n and (s[index].isdigit() or s[index] == '-'):
                index += 1
            value = int(s[start:index])  # Преобразуем строку в число 
            node = TreeNode(value)  # Создаем узел 
            stack.append(node)  # Добавляем узел в стек 

        elif char == '(':  # Если встречаем открывающую скобку 
            index += 1
            continue  # Переходим к следующему символу 

        elif char == ',':  # Если встречаем запятую 
            index += 1
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


def pre_order(node):
    """Не рекурсивный прямой обход дерева с использованием стека."""
    if not node:
        return ""

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

    return " ".join(map(str, result))  # Возвращаем значения узлов в виде строки 


def insert(node, value):
    """Добавляет узел с заданным значением в бинарное дерево."""
    if node is None:
        return TreeNode(value)

    if value < node.value:
        node.left = insert(node.left, value)  # Рекурсивно добавляем в левое поддерево 
    else:
        node.right = insert(node.right, value)  # Рекурсивно добавляем в правое поддерево 

    return node


def delete(node, value):
    """Удаляет узел с заданным значением из бинарного дерева."""
    if node is None:
        return node

    if value < node.value:
        node.left = delete(node.left, value)  # Рекурсивно удаляем из левого поддерева 
    elif value > node.value:
        node.right = delete(node.right, value)  # Рекурсивно удаляем из правого поддерева 
    else:
        # Узел с единственным ребенком или без детей 
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

            # Узел с двумя детьми: получаем наименьший узел из правого поддерева
        min_larger_node = node.right
        while min_larger_node.left is not None:
            min_larger_node = min_larger_node.left
        node.value = min_larger_node.value  # Сохраняем его значение 
        node.right = delete(node.right, min_larger_node.value) # Удаляем узел с его значением
        return node


def print_tree(node):
    """Выводит бинарное дерево в линейно-скобочной записи."""
    if node is None:
        return ""

    left = print_tree(node.left)
    right = print_tree(node.right)

    return f"{node.value}({left},{right})" if left or right else str(node.value)


def main():
    """Основная функция для взаимодействия с пользователем."""
    input_string = input("Введите линейно-скобочную запись для построения бинарного дерева: ")
    tree_root = build_tree(input_string)  # Строим дерево из строки 

    while True:
        print("\nМеню:")
        print("1. Добавить узел")
        print("2. Удалить узел")
        print("3. Поиск узла")
        print("4. Вывести дерево")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            value = int(input("Введите значение для добавления: "))
            tree_root = insert(tree_root, value)
            print("Дерево после добавления узла:")
            print(pre_order(tree_root))

        elif choice == '2':
            value = int(input("Введите значение для удаления: "))
            tree_root = delete(tree_root, value)
            print("Дерево после удаления узла:")
            print(pre_order(tree_root))

        elif choice == '3':
            value = int(input("Введите значение для поиска: "))
            found = pre_order(tree_root).split()
            if str(value) in found:
                print(f"Узел {value} найден.")
            else:
                print(f"Узел {value} не найден.")

        elif choice == '4':
            print("Дерево в линейно-скобочной записи:")
            print(print_tree(tree_root))

        elif choice == '5':
            print("Финальное дерево в линейно-скобочной записи:")
            print(print_tree(tree_root))
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()

"""
8(3(1,6(4,7)),10(,14(13,)))
"""
