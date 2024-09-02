import os
os.system ("cls | clear")
orcamento = int(input("Digite quanto você quer gastar: "))
total_gasto = 0.0
valor_excedente = 0

while total_gasto <= orcamento:

    gasto_diario = float(input("Digite o valor do gasto diário: "))
    saldo_restante = orcamento - total_gasto
    total_gasto += gasto_diario
    
    if total_gasto > orcamento:
        valor_excedente = total_gasto - orcamento
        print(f"Você excedeu o orçamento.")
        print(f"Total gasto: R${total_gasto}")
        print(f"Valor excedente: R${valor_excedente}")         
    elif saldo_restante == total_gasto:
        print("você não pode mais gastar")
    else:
        saldo_restante = orcamento - total_gasto 
        print(f"Você pode gastar mais {saldo_restante} reais antes de exceder o orçamento.")
    

    
  