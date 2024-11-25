# Функция для вычисления выражения
def calculate(expression):
    # Пробуем вычислить выражение
    try:
        # Возвращаем результат вычислений в виде строки
        return str(evaluate_expression(expression))
        # Если возникает ошибка, возвращаем сообщение об ошибке
    except Exception as e:
        return f"Error: {e}"


# Функция для оценки выражения
def evaluate_expression(expression):
    # Разбиваем выражение на токены
    tokens = tokenize(expression)
    # Преобразуем инфиксную запись в постфиксную
    postfix = infix_to_postfix(tokens)
    # Вычисляем значение выражения в постфиксной записи
    return evaluate_postfix(postfix)


# Функция для разбиения выражения на токены
def tokenize(expression):
    # Создаем пустой список для хранения токенов
    tokens = []
    # Переменная для временного хранения текущего токена
    current_token = ""
    # Проходимся по каждому символу в выражении
    for char in expression:
        # Проверяем, является ли текущий символ цифрой или точкой
        if char.isdigit() or char == '.':
            # Добавляем символ к текущему токену
            current_token += char
        else:
            # Если текущий токен не пуст, добавляем его в список токенов
            if current_token:
                tokens.append(current_token)
                # Сбрасываем текущий токен
                current_token = ""
            # Если текущий символ не пробел, добавляем его в список токенов
            if char != ' ':
                tokens.append(char)
    # Если после цикла остался непустой токен, добавляем его в список токенов
    if current_token:
        tokens.append(current_token)
    # Возвращаем список токенов
    return tokens


# Функция для преобразования инфиксного выражения в постфиксное
def infix_to_postfix(tokens):
    # Создаем пустой список для хранения результата
    output = []
    # Создаем стек для операций
    stack = []
    # Устанавливаем приоритет операций
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    # Проходимся по каждому токену
    for token in tokens:
        # Если токен - число, добавляем его в выходной список
        if token.replace('.', '', 1).isdigit():
            output.append(token)
        # Если токен - открывающая скобка, помещаем её в стек
        elif token == '(':
            stack.append(token)
        # Если токен - закрывающая скобка, выталкиваем все операции до первой открытой скобки
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            # Убираем открытую скобку из стека
            stack.pop()
        # Для всех остальных символов (операций)
        else:
            # Пока стек не пуст и последний элемент стека имеет больший или равный приоритет,
            # чем текущий токен, выталкиваем элементы из стека в выходной список
            while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
                output.append(stack.pop())
            # Помещаем операцию в стек
            stack.append(token)

    # Выталкиваем оставшиеся элементы из стека в выходной список
    while stack:
        output.append(stack.pop())

    # Возвращаем преобразованное выражение
    return output


# Функция для вычисления значения выражения в постфиксной форме
def evaluate_postfix(tokens):
    # Создаем стек для хранения промежуточных результатов
    stack = []
    # Проходимся по каждому токену
    for token in tokens:
        # Если токен - число, конвертируем его в float и помещаем в стек
        if token.replace('.', '', 1).isdigit():
            stack.append(float(token))
        else:
            # Извлекаем два последних числа из стека
            operand2 = stack.pop()
            operand1 = stack.pop()
            # Выполняем соответствующую операцию и помещаем результат обратно в стек
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)

            elif token == '/':
                stack.append(operand1 / operand2)
            # Возвращаем итоговый результат
    return stack.pop()

# Запрашиваем у пользователя ввод выражения
expression = input("Введите выражение: ")
# Вычисляем результат
result = calculate(expression)
# Обрабатываем возможные ошибки и выводим результат
if result[-4:] == "zero":
    print("Разделить на ноль нельзя")
elif result[:5] == "Error":
    print("Некорректное выражение")
else:
    print(f"Результат: {result}")

