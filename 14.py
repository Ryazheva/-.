"""
Дан текстовый файл с некоторым текстом на русском или английском языках произвольной длины (организовать чтение).
Выбрав некоторую хеш-функцию, создать хеш-таблицу с:
Лаба №14 “со списками”
Таблицу записать в результирующий файл.
"""
# Импортируем модуль регулярных выражений для поиска слов в тексте
import re


# Создаем класс хэш-таблицы
class HashTable:
    # Метод инициализации класса, который создает пустую таблицу заданного размера
    def __init__(self, size=100):
        # Устанавливаем размер таблицы
        self.size = size
        # Создаем список списков для хранения данных
        self.table = [[] for _ in range(size)]

    # Функция вычисления хэша ключа
    def hash_function(self, key):
        # Возвращает остаток от деления значения хеша ключа на размер таблицы
        return hash(key) % self.size

    # Метод вставки элемента в хэш-таблицу
    def insert(self, key):
        # Вычисляем индекс для вставки элемента
        index = self.hash_function(key)

        # Проверяем, есть ли уже такой элемент в таблице
        for item in self.table[index]:
            if item == key:
                # Если элемент найден, выходим из метода
                return
        # Добавляем новый элемент в конец списка
        self.table[index].append(key)

    # Метод отображения содержимого хэш-таблицы
    def display(self):
        # Создаем пустой список для результата
        result = []
        # Проходимся по всем спискам в таблице
        for index, items in enumerate(self.table):
            # Если список не пуст, добавляем его в результат
            if items:
                result.append(f'{index}: {items}')
        # Возвращаем результат
        return result


# Функция чтения файла
def read_file(file_path):
    # Открываем файл для чтения в режиме UTF-8
    with open(file_path, 'r', encoding='utf-8') as f:
        # Читаем содержимое файла
        text = f.read()
        # Возвращаем прочитанное содержимое
        return text


# Функция создания хэш-таблицы из текста
def create_hash_table(text):
    # Создаем объект хэш-таблицы
    hash_table = HashTable()

    # Находим все слова в тексте с помощью регулярного выражения
    words = re.findall(r'\b\w+\b', text.lower())
    # Вставляем каждое слово в хэш-таблицу
    for word in words:
        hash_table.insert(word)
    # Возвращаем заполненную хэш-таблицу
    return hash_table


# Функция записи хэш-таблицы в файл
def write_hash_table(hash_table, file_path):
    # Открываем файл для записи в режиме UTF-8
    with open(file_path, 'w', encoding='utf-8') as f:
        # Записываем каждую строку из результата отображения хэш-таблицы в файл
        for line in hash_table.display():
            f.write(line + '\n')


# Основная часть программы
if __name__ == "__main__":
    # Указываем путь к входному файлу
    input_file_path = 'text14.txt'
    # Указываем путь к выходному файлу
    output_file_path = 'hash_table14.txt'

    # Читаем текст из файла
    text = read_file(input_file_path)
    # Создаем хэш-таблицу из текста
    hash_table = create_hash_table(text)
    # Сохраняем хэш-таблицу в файл
    write_hash_table(hash_table, output_file_path)

    # Сообщение о завершении работы программы
    print("Хеш-таблица сохранена в файл hash_table14.txt")
