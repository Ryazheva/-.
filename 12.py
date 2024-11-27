import heapq  # Импорт модуля heapq для работы с кучей
import os     # Импорт модуля os для работы с файловой системой
import tempfile  # Импорт модуля tempfile для работы с временными файлами

def sort_and_save_chunk(numbers):
    """
    Сортирует массив чисел и сохраняет его в временном файле.

    :param numbers: Массив чисел для сортировки и сохранения.
    :return: Имя временного файла, содержащего отсортированные числа.
    """
    # Сортируем массив чисел
    numbers.sort()

    # Создаём временный файл для записи чисел
    temp_file = tempfile.NamedTemporaryFile(delete=False, mode='w+', newline='')

    with open(temp_file.name, 'w') as f:
        # Записываем каждое число в файл с новой строкой
        for number in numbers:
            f.write(f"{number}\n")

    # Возвращаем имя временного файла
    return temp_file.name

def external_sort(file_path, chunk_size):
    """
    Осуществляет внешнюю сортировку файла с числами.

    :param file_path: Путь к исходному файлу с числами.
    :param chunk_size: Размер блока данных для чтения и сортировки.
    :return: None
    """
    temp_files = []

    with open(file_path, 'r') as f:
        # Чтение файла по частям (чанкам)
        chunk = []
        for line in f:
            # Преобразование строки в число и добавление в чанк
            number = int(line.strip())
            chunk.append(number)

            # Если размер чанка достиг максимального размера, сортируем и сохраняем его
            if len(chunk) >= chunk_size:
                temp_file = sort_and_save_chunk(chunk)
                temp_files.append(temp_file)
                chunk = []

        # Сохранение последнего неполного чанка, если он есть
        if chunk:
            temp_file = sort_and_save_chunk(chunk)
            temp_files.append(temp_file)

    # Объединение отсортированных временных файлов в один результирующий файл
    with open('sorted_output.txt', 'w') as output_file:
        # Используем функцию слияния файлов
        sorted_numbers = merge_files(temp_files)
        for number in sorted_numbers:
            output_file.write(f"{number}\n")

    # Удаление временных файлов
    for temp_file in temp_files:
        os.remove(temp_file)

def merge_files(file_list):
    """
    Сливает несколько отсортированных файлов в один поток.

    :param file_list: Список имен файлов для слияния.
    :return: Генератор, который последовательно выдаёт числа из объединённых файлов.
    """
    # Инициализируем кучу для хранения минимальных элементов из каждого файла
    min_heap = []

    # Открываем все файлы одновременно
    file_iters = [open(file) for file in file_list]

    # Читаем первую строку из каждого файла и помещаем в кучу
    for i, file_iter in enumerate(file_iters):
        line = file_iter.readline()
        if line:
            heapq.heappush(min_heap, (int(line.strip()), i, file_iter))

    # До тех пор, пока куча не пуста, извлекаем минимальный элемент и читаем следующую строку из соответствующего файла
    while min_heap:
        value, idx, file_iter = heapq.heappop(min_heap)
        yield value
        next_line = file_iter.readline()
        if next_line:
            heapq.heappush(min_heap, (int(next_line.strip()), idx, file_iter))

    # Закрываем все открытые файлы
    for file_iter in file_iters:
        file_iter.close()

# Пример использования

if __name__ == "__main__":
    input_file = "input_numbers.txt"  # Исходный файл с числами
    chunk_size = 100                  # Размер чанка для внешней сортировки
    external_sort(input_file, chunk_size)  # Запуск внешней сортировки
