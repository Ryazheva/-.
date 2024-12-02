# Хеш-таблица 
#Дан текстовый файл с некоторым текстом на русском или английском языках произвольной длины (организовать чтение). 
# Выбрав некоторую хеш-функцию, создать хеш-таблицу с: 
#Лаба №13 “с наложением” 
 
 # Класс для реализации хэш-таблицы
class HashTable:
    # Конструктор класса, который инициализирует размер таблицы и создает список пустых ячеек
    def __init__(self, size):
        # Устанавливаем размер хэш-таблицы
        self.size = size
        # Создаем список из `size` элементов, каждый элемент которого равен None
        self.table = [None for _ in range(size)]

    # Функция для вычисления хэша строки
    def hash_function(self, key):
        # Возвращает сумму ASCII-кодов символов строки, взятую по модулю размера таблицы
        return sum(ord(char) for char in key) % self.size

    # Метод для вставки ключа в таблицу
    def insert(self, key):
        # Вычисляем индекс для ключа с помощью функции хэширования
        hash_index = self.hash_function(key)
        
        # Если ячейка с этим индексом свободна, помещаем ключ туда
        if self.table[hash_index] is None:
            self.table[hash_index] = key
            return

        # В противном случае начинаем линейный поиск свободной ячейки
        i = 1
        while self.table[hash_index] is not None:
            # Рассчитываем новый индекс с использованием квадратичной пробировки
            new_index = (hash_index + i * i) % self.size
            
            # Если находим свободную ячейку, вставляем ключ и выходим из цикла
            if self.table[new_index] is None:
                self.table[new_index] = key
                return
            i += 1

    # Метод для отображения содержимого хэш-таблицы
    def display(self):
        # Проходимся по всем элементам списка и выводим заполненные ячейки
        for index, items in enumerate(self.table):
            if items:
                print(f"Index {index}: {items}")

    # Метод для сохранения содержимого хэш-таблицы в файл
    def save_to_file(self, filename):
        # Открываем файл для записи
        with open(filename, 'w', encoding='utf-8') as file:
            # Проходимся по всем элементам списка и записываем заполненные ячейки в файл
            for index, items in enumerate(self.table):
                if items:
                    file.write(f"Index {index}: {items}\n")

# Функция для заполнения хэш-таблицы данными из файла
def fill_hash_table_from_file(filename, hash_table):
    # Открываем файл для чтения
    with open(filename, 'r', encoding='utf-8') as file:
        # Читаем каждую строку файла
        for line in file:
            # Разбиваем строку на отдельные слова
            words = line.strip().split()
            # Добавляем каждое слово в хэш-таблицу
            for word in words:
                hash_table.insert(word)

# Имя файла с исходными данными
filename = "text.txt"
# Создаем объект хэш-таблицы размером 30
hash_table = HashTable(30)
# Заполняем хэш-таблицу словами из файла
fill_hash_table_from_file(filename, hash_table)
# Выводим содержимое хэш-таблицы на экран
print("Содержимое хеш-таблицы:")
hash_table.display()

# Имя файла для сохранения данных
output_filename = "hash_table.txt"
# Сохраняем содержимое хэш-таблицы в файл
hash_table.save_to_file(output_filename)
# Сообщение о сохранении данных
print(f"Содержимое хеш-таблицы сохранено в файл: {output_filename}")
