# Function open() membutuhkan 2 argument, nama file dan mode file handling
open('filename.txt', 'x') # membuat file baru
open('filename.txt', 'r') # membaca file yg ada
open('filename.txt', 'w') # menulis konten pd file
open('filename.txt', 'a') # menambahkan konten pd file

# MEMBUAT FILE BARU
open('file.txt', 'x')
#jika nama file yg disebutkan sdh ada, maka akan muncul erroe FileExists

#MEMBACA KONTEN FILE
#simpan function dlm variable
file = open('file.txt','r')
# mengambil konten dgn .read
print(file.read())
# jika nama file yg disebutkan tdk ada, maka akan muncul erroe FileDoesNotExists

# MENULIS KONTEN KE DALAM FILE
file = open('file.txt', 'w')
# menulis konten ke dlm file
file.write("Welcome to Aeos Island, Pokemon friends!")
file.write("\n")
file.write("I am Meowth!")
file.close()
# setiap selesai nulis 
# file gak ada = dibuatin fle baru 
# file ada = konten diganti dgn yg baru ditmbhkn dgn .write

# MENAMBAHKAN KONTEN
file = open('file.txt', 'a')
# menulis konten ke dlm file
file.write("\n")
file.write("Meowth power is Fury Swipes!")
file.close()
# file gak ada = dibuatin file baru
# file ada = konten ditambhkan, tdk diganti semua





