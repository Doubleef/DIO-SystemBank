import datetime


class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.depositos = []
        self.saques = []
        self.limite_saques_diarios = 3
        self.saques_hoje = 0
        self.data_ultimo_saque = None

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            self.extrato.append(f"Depósito: +R$ {valor:.2f}")
            print(f"Você depositou R$ {valor:.2f}")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        hoje = datetime.date.today()

        if self.data_ultimo_saque != hoje:
            self.saques_hoje = 0
            self.data_ultimo_saque = hoje

        if self.saques_hoje >= self.limite_saques_diarios:
            print("Você atingiu o limite diário de 3 saques.")
        elif valor > 500:
            print("O limite máximo por saque é de R$ 500,00.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor > 0:
            self.saldo -= valor
            self.saques.append(valor)
            self.extrato.append(f"Saque: -R$ {valor:.2f}")
            self.saques_hoje += 1
            print(f"Você sacou R$ {valor:.2f}")
        else:
            print("Valor de saque inválido!")

    def mostrar_extrato(self):
        print("\nExtrato:")
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            if self.depositos:
                print("\nDepósitos realizados:")
                for deposito in self.depositos:
                    print(f"Depósito de: R$ {deposito:.2f}")
            if self.saques:
                print("\nSaques realizados:")
                for saque in self.saques:
                    print(f"Saque de: R$ {saque:.2f}")

        # Exibir saldo final
        print(f"\nSaldo atual: R$ {self.saldo:.2f}")


# Exemplo de uso:
conta = Banco()

while True:
    print("\nEscolha uma operação:")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Ver Extrato")
    print("4. Sair")

    opcao = input("Digite o número da operação: ")

    if opcao == "1":
        valor_deposito = float(input("Digite o valor a depositar: "))
        conta.depositar(valor_deposito)
    elif opcao == "2":
        valor_saque = float(input("Digite o valor a sacar: "))
        conta.sacar(valor_saque)
    elif opcao == "3":
        conta.mostrar_extrato()
    elif opcao == "4":
        print("Encerrando o sistema bancário.")
        break
    else:
        print("Opção inválida, tente novamente.")
