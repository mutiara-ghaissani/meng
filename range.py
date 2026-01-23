# Range digunakan untuk membuat kumpulan angka
# dimulai dr angka 0 dan brtmbh 1 scr trs-mnerus dan berhenti sblm angka yg disebutkan

# Range memiliki 3 argument

# Range(stop) mendeskripsikan nilai akhir
range(10)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Range(start, stop) mendeskripsikan mulai dan akhir
range(1,10)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Range(start, stop, step) mendeskripsikan mulai, akhir, dan langkah
range(1, 10, 2)
# [1, 3, 5, 7, 9] 

# RANGE(STOP)

# menyimpan range ke dlm variable
numbers = range(10) # range(0, 10)

#untuk mengetahui isinya, gunakan list constructor
print(list(numbers))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# RANGE(START, STOP)

# menyimpan range ke dlm variable
numbers1 = range(1, 10)

print(list(numbers1))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# RANGE(START, STOP, STEP)

numbers2 = range(1, 10, 2)

print(list(numbers2))
# [1, 3, 5, 7, 9]

# diambil setiap 2 langkah

