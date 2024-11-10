one_symbol_size_byte = 4
disk_size_mbyte = 1.44
disk_size_byte = 1.44 * 1024 * 1024

symbols = 25
lines = 50
pages = 100

books = int(disk_size_byte // (one_symbol_size_byte * symbols * lines * pages))

print("Количество книг, помещающихся на дискету:", books)
