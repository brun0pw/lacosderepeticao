import os
os.system ("cls | clear")
numeroinicial = 2
contadordemultiplicacoes = 0
numero = int(input("Digite um número: "))
while True:
  
  contadordemultiplicacoes += 1
  resultado = numero * numeroinicial
  if resultado  < 100 :
    
   print(f"o produto final foi da multiplicação de: {numeroinicial} * {resultado} foi maior ou igual a 100")
   break