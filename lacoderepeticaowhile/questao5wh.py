import os
os.system("cls || clear")

numtentativas = 0
codigopromocao = "PROMO2024"




while True :
    codigodousuario = input("DIGITE SEU CODIGO DE PROMOÇÃO: ").upper()
    
    if codigopromocao == codigodousuario:
     print("CÓDIGO ACEITO") 
     break
    else:
      print("codigo invalido")
      numtentativas += 1
     
    if numtentativas == 3:
          print("limite de tentativas alcançado\n", numtentativas)
          break