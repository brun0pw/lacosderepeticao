'''
Crie um programa que ajude um estudante a calcular a média de suas notas.
O programa deve permitir que o usuário insira notas de provas até que o usuário insira um valor negativo.
O programa deve calcular e exibir a média das notas inseridas.
'''
import os
os.system("cls || clear")
soma_notas = 0
contador_notas = 0


while True:

   nota = float(input("Digite uma nota : "))
   soma_notas += nota
   contador_notas += 1
   
      
   if nota < 0 or nota > 10:
         print("Nota inválida. Digite uma nota entre 0 e 10.")
       
  
   if contador_notas >= 3:
      resposta = input("deseja colocar mais uma nota: ")
      if resposta == "s":
       print("continue inserindo suas notas")
       
      else:
       media = soma_notas / contador_notas
       print(f"A média das notas é: {media:.2f}")
       break
         