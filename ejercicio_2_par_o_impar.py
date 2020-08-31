numero = int(input("escribe el numero de la cuenta "))
check = int(input("escribe el total de clientes a distribuir el total de la cuenta "))
mod = numero % check
div = (numero / check)
div1 = str(div)
if mod == 0:
    print("la cuenta es  " + div1)
else : 
        print("la cuenta no se puede dividir en partes iguales")
