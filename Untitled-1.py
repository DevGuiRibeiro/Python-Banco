class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
      if valor > 0:
        self.saldo += valor
        print(f"Depósito de R$ {valor} realizado com sucesso!")
      else:
        print("Valor inválido para depósito.")
    def sacar(self, valor):
      if valor > 0 and valor <= self.saldo:
        self.saldo -= valor
        print(f"Saque de R$ {valor} realizado com sucesso!")
    def consultar_saldo(self):
      print(f"Saldo atual: R$ {self.saldo}")

conta = ContaBancaria()

while True:
  print("Escolha uma opção:")
  print("1. Depositar")
  print("2. Sacar")
  print("3. Sair")
  print("4. Ver Saldo")

  opcao = input("Digite o número da opção desejada: ")

  if opcao == "1":
    valor = int(input("Digite o valor a ser depositado: "))
    conta.depositar(valor)
  elif opcao == "2":
    valor = float(input("Digite o valor a ser sacado: "))
    conta.sacar(valor)
  elif opcao == "3":
    print("Saindo do programa...")
    break
  elif opcao =='4':
    conta.consultar_saldo()