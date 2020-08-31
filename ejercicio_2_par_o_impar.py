numero = int(input("escribe un numero "))
mod = numero % 2 
mod4 = numero % 4 
if mod == 0 and mod4 == 0:
    print("el numero es multiplo de 2 y 4")
elif mod == 0 and mod4 != 0:
        print("el numero solo es multiplo de 2")
else : 
        print("es un numero impar")
