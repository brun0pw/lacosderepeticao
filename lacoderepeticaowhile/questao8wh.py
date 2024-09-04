import os
os.system ("cls | clear")
''''' Crie um programa para ajudar o usuário a acompanhar suas metas de estudo.
 O usuário define uma meta de horas de estudo e o programa deve permitir que o usuário insira o número de horas estudadas até que o total atinja ou exceda a meta.
 O programa deve  exibir o total de horas estudadas e o valor excedente.
Dica: Utilize um laço while para somar as horas de estudo até atingir a meta.'''

#variavel que diz quantas horas a pessoa deseja estudar
horasdesejadas = int(input("Quantas horas você deseja estudar? "))
horastotaisdestudos = 0 
while True:
   #variavel que pergunta ao usuario quantas horas ele estudou
   horasestudadas = int(input("Quantas horas você estudou hoje ? "))
   #variavel que soma as horas de estudo
   horastotaisdestudos += horasestudadas
   if horasdesejadas > horastotaisdestudos:
      print("continue estudando")
   elif horastotaisdestudos <= horasdesejadas:
      print("você atingiu sua meta, continue estudando")
   elif  horastotaisdestudos > horasdesejadas :
    print("você já ultrapassou seus limites, mais continue")
   else: 
      print("nani")
   

