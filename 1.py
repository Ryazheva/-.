def check_brackets(s: str) -> bool:
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for char in s:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    return not stack

def main():
    print("Введите строку:")
    input_string = input()

    if check_brackets(input_string):
        print("Строка существует")
    else:
        print("Строка не существует")

if __name__ == "__main__":
    main()
