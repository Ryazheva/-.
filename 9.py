#пирамидальная сортировка

def heapify(arr, n, i):

    largest = i  # Инициализируем largest как корень
    left = 2 * i + 1  # Левый ребенок
    right = 2 * i + 2  # Правый ребенок

    # Если левый потомок больше корня
    if left < n and arr[i] < arr[left]:
        largest = left

    # Если правый потомок больше самого большого элемента
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Если самый большой элемент не является корнем
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами корень и наибольший элемент

        # Рекурсивно применяем heapify к корню.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Перемещаем текущий корень в конец
        heapify(arr, i, 0)

print("Введите последовательность чисел:")

# Читаем ввод, разбиваем его на список строк и преобразуем в список целых чисел
numbers = list(map(int, input().strip().split()))

# Сортируем массив методом пирамидальной сортировки
heap_sort(numbers)

# Выводим отсортированный массив
print(' '.join(map(str, numbers)))
