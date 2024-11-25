def calculate(expression): # РџСЂРѕСЃС‚Рѕ РїРµСЂРµРґР°С‘С‚СЃСЏ СЃР°РјРѕ РІС‹СЂР°Р¶РµРЅРёРµ, РІРѕР·РІСЂР°С‰Р°РµС‚ СЂРµР·СѓР»СЊС‚Р°С‚ РёР»Рё РѕС€РёР±РєСѓ РІ РІРёРґРµ СЃС‚СЂРѕРєРё
    try:
        return str(evaluate_expression(expression)) # Р’С‹С‡РёСЃР»РµРЅРёСЏ
    except Exception as e:
        return f"Error: {e}" # РћС‚Р»РѕРІ РѕС€РёР±РѕРє!


def evaluate_expression(expression):
    tokens = tokenize(expression) # Р Р°Р·Р±РёСЂР°РµС‚ РІС‹СЂР°Р¶РµРЅРёРµ РїРѕ "Р—Р°РїС‡Р°СЃС‚СЏРј"
    postfix = infix_to_postfix(tokens) # РџСЂРµРѕР±СЂР°Р·СѓРµС‚ РІ РїРѕСЃС‚С„РёРєСЃРЅРѕРµ РІС‹СЂР°Р¶РµРЅРёРµ (РЅРµ С‚СЂРµР±СѓРµС‚ РѕРїСЂРµРґРµР»РµРЅРёСЏ С‡РµСЂРµРґС‹ РїРѕРґСЃС‡С‘С‚РѕРІ, РѕР±СЂР°С‚РЅР°СЏ РїРѕР»СЊСЃРєР°СЏ РЅРѕС‚Р°С†РёСЏ)
    return evaluate_postfix(postfix) # РџСЂРѕСЃС‚Рѕ СЃС‡РёС‚Р°РµС‚ РїРѕР»СѓС‡РµРЅРЅРѕРµ РІС‹СЂР°Р¶РµРЅРёРµ


def tokenize(expression):
    tokens = []
    current_token = ""
    for char in expression:
        if char.isdigit() or char == '.':
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            if char != ' ':
                tokens.append(char)
    if current_token:
        tokens.append(current_token)
    return tokens


def infix_to_postfix(tokens):
    output = []
    stack = []
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2} # РЎР»РѕРІР°СЂСЊ РґР»СЏ РѕРїСЂРµРґРµР»РµРЅРёСЏ РѕРїРµСЂР°С‚РѕСЂРѕРІ (РєС‚Рѕ СЃС‚Р°СЂС€Рµ))

    for token in tokens:
        if token.replace('.', '', 1).isdigit():  # Р•СЃР»Рё СЌС‚Рѕ С‡РёСЃР»Рѕ
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence[token] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def evaluate_postfix(tokens):
    stack = []
    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            stack.append(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.append(operand1 + operand2)
            elif token == '-':
                stack.append(operand1 - operand2)
            elif token == '*':
                stack.append(operand1 * operand2)
            elif token == '/':
                stack.append(operand1 / operand2)
    return stack.pop()


expression = input("Р’РІРµРґРёС‚Рµ РІС‹СЂР°Р¶РµРЅРёРµ: ")
result = calculate(expression)
if(result[-4:] == "zero"):
    print("Р Р°Р·РґРµР»РёС‚СЊ РЅР° РЅРѕР»СЊ РЅРµР»СЊР·СЏ")
elif(result[:5] == "Error"):
    print("РќРµРєРѕСЂСЂРµРєС‚РЅРѕРµ РІС‹СЂР°Р¶РµРЅРёРµ")
else:
    print(f"Р РµР·СѓР»СЊС‚Р°С‚: {result}")
