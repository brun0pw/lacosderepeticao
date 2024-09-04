import os
os.system("cls || clear")

calorias = 2000
caloriastotais = 0 
while True:
   #variavel que pergunta ao usuario quantas horas ele estudou
   caloriasconsumidas = int(input("Quantas calorias você consumiu hoje ? "))
   #variavel que soma as horas de estudo
   caloriastotais += caloriasconsumidas
   if calorias > caloriastotais:
      print("continue seguindo a rotina")
   elif caloriastotais <= calorias:
      print("você atingiu a sua meta de calorias!")
   elif  caloriastotais > calorias :
    print("você já ultrapassou seus limites, pare agora!!")
   else: 
      print("nani")
   if caloriastotais > calorias:
        
        print(f" você comeu {caloriastotais} calorias \n o excesso de calorias foi de: {caloriastotais - calorias}")
        
        break
   