#Dictionary Characteristic: -menggunakan {}, -setiap data dipisah koma, -setiap data dideskripsikan menggunakan pasangan key:value, -mengakses item menggunakan nama key

#dictionary biasa
student = {'name':'Magikarp', 'region':'Kanto'}

#dict constructor
student = dict(name= 'Magikarp', region='Kanto')

#format penulisan dict, bisa menyusun ke bawah

student = {
    'name':'Magikarp',
    'region':'Kanto',
    'age': 17,
    'active': True,
    'hobbies': [
        'swimming'
        'splash'
        'being a fish'
    ]
}

#mengakses value
print(student['age'])

#menambahkan key:value baru
student['phone'] = '892344773023'

#mengubah key:value yg ada
student['region'] = 'Paldea' 

#menghapus key:value 
#sebutkan key pd .pop()
student.pop('age')

#menghapus key:value terakhir
student.popitem()


