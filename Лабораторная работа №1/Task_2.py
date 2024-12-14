SHEETS = 100
STRINGS = 50
SYMBOLS = 25
MEMORY = 1.44
BYTES_OF_SYMBOL = 4

count_of_symbols = SHEETS * STRINGS * SYMBOLS
memory_in_bytes = MEMORY * 1024 * 1024

books = memory_in_bytes // (count_of_symbols * BYTES_OF_SYMBOL)
books = int(books)

print("Количество книг, помещающихся на дискету:", books)
