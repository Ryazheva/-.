#сортировка вставками

print("Введите последовательность чисел:")

def insertion_sort(arr):
    # Проходим по всем элементам массива начиная со второго
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Перемещаем элементы массива вперед, пока не найдем подходящее место для текущего элемента
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Вставляем текущий элемент на нужное место
        arr[j + 1] = key
#считываем ввод пользователя
numbers = list(map(int, input().strip().split()))

insertion_sort(numbers)

#вывод
print(' '.join(map(str, numbers)))
