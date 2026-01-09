#Tuple Characteristic: -menggunakan (), -setiapa data dipisah koma, -tdk dpt dimanipulasi

#tuple biasa
names = ("Bulbasaur", "Gengar", "Exeggutor")

#membuat tuple dgn tuple constructor
names = tuple(("Bulbasaur", "Gengar", "Exeggutor"))

#membuat tuple dr Itarable Object
name = "Bulbasaur"
letters = tuple(name)

#indexing

names = ("Bulbasaur", "Gengar", "Exeggutor")

print(names[1])

#tuple dpt dimanipulasi dgn cara mengkonversikannya trlbh dahulu ke dlm bntk list menggunakan list constructor
#stlh itu dikembalikan ld ke dlm bntk tuplr menggunakan tuplr constructor

names = ("Mew", "Gengar", "Exeggutor")

#konversi ke dlm list
names_list = list(names)

#manipulasi
names_list.append("Dodrio")
names_list[0] = "Mewtwo"
names_list.remove("Gengar")

#konversi ke dlm tuple
names = tuple(names_list)

