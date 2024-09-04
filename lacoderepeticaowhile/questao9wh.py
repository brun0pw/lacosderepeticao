import os
os.system("cls || clear")

soma = 0
contador = 0
while True:
    numero = int(input("escolha o número: "))
    if  numero % 2 != 0 :
     soma += numero 
     contador += 1
     if soma > 200:
        
        print(f" você digitou {contador} números ímpares \n a soma dos números foi de : {soma}")
        
        break
    else:
     print("só aceitamos números ímpares")
    