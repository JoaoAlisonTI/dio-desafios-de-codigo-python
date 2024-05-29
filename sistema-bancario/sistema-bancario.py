saldo_atual = 0.00
deposito = 0.00
saque = 0.00
contador_tentativas = 1
contador_para_extrato = 0

print("""
Bem vindo(a) ao banco PY!
Escolha a operação digitando o caractere específico:
  
D Para depósito.
S Para saque.
E Para extrato.
Q Para sair.
""")

while True:
  menu = input("\nDigite a operação: ")
  if menu == "D":
    deposito = float(input("Digite o valor a ser depositado: "))
    if deposito < 0:
      print("Somente valores positivos!")
    else:
      saldo_atual += deposito
      contador_para_extrato += 1
      print("Valor depositado com sucesso!")
  elif menu == "S":
    if contador_tentativas > 3:
      print("Você só pode realizar 3 saques diários!")
    else:
      saque = float(input("Digite o valor a ser sacado: "))
      if saque > saldo_atual:
        print("O saque é maior que o saldo atual!")
      elif saque > 500:
        print("Limite máximo de R$ 500.00 por saque!")
      else:
        saldo_atual -= saque
        contador_para_extrato += 1
        contador_tentativas += 1
        print("Valor sacado com sucesso!")
  elif menu == "E":
    if contador_para_extrato > 0:
      print(f"Valor do depósito mais recente: R$ {deposito:.2f}\nValor do saque mais recente: R$ {saque:.2f}\nValor do saldo atual: R$ {saldo_atual:.2f}")
    else:
      print("Não foram realizadas movimentações.")
  elif menu == "Q":
    break
  else:
    print("Operação inválida!!!")

print("Operação bancária finalizada!")