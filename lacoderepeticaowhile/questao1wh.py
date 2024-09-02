import os
os.system("cls || clear")

contador = 0
while True:
  numero = int(input("Digite um numero:"))
  if numero < 0:
     contador += 1
    
  else :
     break
print(f"você imprimiu {contador} números negativos")