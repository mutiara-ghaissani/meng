#Set Characteristic: -menggunakan {}, -setiap data dipisah koma, -item tdk dpt diakses, -tdk berurut, -tdk dpt dimanipulasi

#set biasa
names = {"Kabuto", "Chansey", "Seadra"}

#set constructor
names = set(("Kabuto", "Chansey", "Seadra"))

#set itarable object
name = "Kabuto"
letters = set(name)

#krn set tdk berurut, maka masing2 itemnya pun tdk dpt diakses

names = {"Kabuto", "Chansey", "Seadra"}
print(names)

#item dlm set tdk dpt diakses
print(names[2]) #ini akan error

#manipulasi yg dpt kita lakukan dlm set hanya menambahkan dan menghapus item

names = {"Kabuto", "Chansey", "Seadra"}

#menambahkan item baru
names.add("Zapdos")

names.discard("Chansey") #jika item tdl ada, tdk akan error

names.remove("Snorlax") #jika item tidak ada, akan error

names.pop() #menghaps item scr acak


