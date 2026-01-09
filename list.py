#lict characteristic: -menggunakan [], -setiap data dipisah dgn koma, -dapat dimanipulasi tmbh,kurang, ubah, hapus)

#membuat list dgn biasa
names = ["Vulpix", "Vaporeon", "Charizard"]

#membuat list dgn list constructor
names = list(("Vulpix", "Vaporeon", "Charizard"))

#membuat list dr Itarable Object
name = "Vulpix"
letters = list(name)

#cara mengakses satu item dr kumpulam data-->indexing(pemanggilan nomor urutan dr data tumpukan)
#urutan mulai dr 0
#           0           1           2
names = ["Vulpix", "Vaporeon", "Charizard"]

#mengakses item
print(names[2])
#output: Charizard

names = ["Vulpix", "Vaporeon", "Charizard"]

#menambahkan item baru
names.append("Oshawott")

#mengubah item
names[0] = "Alolan Vulpix"

#menghapus item
names.remove("Vaporeon")




