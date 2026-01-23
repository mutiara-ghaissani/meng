# Slicing mrpkn mekanisme ubtuk mengambil satu item dr sbeuah data dl bntk iterable object (list, tuple, dsb)
# menghasilkan sebuah list, krn yg diambil adlh kumpulan  item, bukan hanya 1 item

# list[:stop]
# list[start:stop]
# list[start:stop:step]
# ini semua sama aja kyk range fungsi nya

numbers = list(range(2, 21, 2))
# [2, 4, 6, ..., 16, 18, 20]

print(numbers[:5])
# output: [2, 4, 6, 8, 10]

print(numbers[2:6])
# output: [6, 8, 10, 12]

print(numbers[2:8:3])
# output: [6, 12]