# FUNCTION

def sayHello():
    print("Welcome")

# menjalankan function
sayHello()

# menggunakan kata kunci return
def sayHello():
    return "Welcome"

print(sayHello())

# FUNCTION ARGUMENTS

def sayHello(name):
    return "Welcome" + name

#hrs dgn argumen
print(sayHello(" Zeraora"))

# menambahkan argument lebih dr satu
def addition(num1, num2):
    result = num1 + num2
    print(num1, "+", num2, "=", result)

addition(15, 16)

# FUNCTION DEFAULT ARGUMENTS

# saat sebuah function memiliki argument, maka sattt  memanggil function trsbt, kita wajib menyertakan argument 
# klo nggak nanti error

# def sayHello(name):
    #return "Welcome" + name

#print(sayHello())

# menerapkan default argument yg sdh memiliki argument bawaan
def sayHello(name=""):
    return "Welcome" + name

print(sayHello())

# FUNCTION KEYWORD ARGUMENTS

def fullname(fname, lname=""):
    return fname + " " + lname

print(fullname(lname="Vulpix", fname="Alolan"))

# *args 
# (argument yg menampung banyak masukan tnp hrs ditent. brp jmlh argumentnya) 
# (Arbitary arguments)

def addition(*numbers):
    result = 0

    for n in numbers:
        result += n

    return result

# **kwargs 
# (keyword beserta argument dlm function dpt digunakan sebanyak2nya) 
# (Arbitary Keyword Arguments)

def fullname(**kwargs):
    values = kwargs.values()
    print("".join(values))

fullname(a="Jolteon ", b="Vaporeon ", c="Flareon")







