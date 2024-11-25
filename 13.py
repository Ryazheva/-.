# Хеш-таблица 
#Дан текстовый файл с некоторым текстом на русском или английском языках произвольной длины (организовать чтение). 
# Выбрав некоторую хеш-функцию, создать хеш-таблицу с: 
#Лаба №13 “с наложением” 
 
 
class HashTable: 
    def __init__(self, size): 
        self.size = size  # Устанавливаем размер хеш-таблицы 
        self.table = [None for _ in range(size)]  # Инициализируем таблицу значениями None 
    def hash_function(self, key): 
        return sum(ord(char) for char in key) % self.size 
    def insert(self, key): 
        hash_index = self.hash_function(key)  # Вычисляем индекс для вставки ключа 
        if self.table[hash_index] is None: 
            self.table[hash_index] = key  # Если ячейка пустая, вставляем ключ 
            return 
        # Обработка коллизий с помощью квадратичного пробирования 
        i = 1 
        while self.table[hash_index] is not None: 
            new_index = (hash_index + i * i) % self.size  # Вычисляем новый индекс 
            if self.table[new_index] is None: 
                self.table[new_index] = key  # Вставляем ключ в первую пустую ячейку 
                return 
            i += 1  # Увеличиваем шаг для следующей попытки 
    def display(self): 
        # Выводим содержимое хеш-таблицы 
        for index, items in enumerate(self.table): 
            if items: 
                print(f"Index {index}: {items}")  # Печатаем индекс и значение, если оно не None 
    def save_to_file(self, filename): 
        # Сохраняем содержимое хеш-таблицы в файл 
        with open(filename, 'w', encoding='utf-8') as file: 
            for index, items in enumerate(self.table): 
                if items: 
                    file.write(f"Index {index}: {items}\n")  # Записываем индекс и значение в файл 
# Функция для заполнения хеш-таблицы из файла 
def fill_hash_table_from_file(filename, hash_table): 
    with open(filename, 'r', encoding='utf-8') as file:  # Открываем файл с кодировкой UTF-8 
        for line in file: 
            words = line.strip().split()  # Разбиваем строку на слова 
            for word in words: 
                hash_table.insert(word)  # Вставляем каждое слово в хеш-таблицу 
# Основная часть программы 
filename = "text.txt"  # Указываем имя файла 
hash_table = HashTable(30)  # Создаем хеш-таблицу с размером 30 
fill_hash_table_from_file(filename, hash_table)  # Заполняем хеш-таблицу данными из файла 
print("Содержимое хеш-таблицы:") 
hash_table.display()  # Выводим содержимое хеш-таблицы 
# Сохраняем содержимое хеш-таблицы в файл 
output_filename = "hash_table.txt" 
hash_table.save_to_file(output_filename) 
print(f"Содержимое хеш-таблицы сохранено в файл: {output_filename}")
