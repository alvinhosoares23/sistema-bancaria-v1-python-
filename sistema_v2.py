class ContaBancaria:
    def __init__(self, saldo_inicial=0, limite_saque=500, max_saques=3):
        self.saldo = saldo_inicial
        self.limite_saque = limite_saque
        self.max_saques = max_saques
        self.saques_realizados = 0
        self.depositos = []
        self.saques = []

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)

    def saque(self, valor):
        if self.saldo >= valor and valor <= self.limite_saque and self.saques_realizados < self.max_saques:
            self.saldo -= valor
            self.saques.append(valor)
            self.saques_realizados += 1
            print(f"#  Saque de {valor} Realizado com sucesso")
        else:
            print("#######################################")
            print("#  Não foi possível realizar o saque. #")
            print("#  Obs(Só é permito 3 saques por dia) #")
            print("#          e Limite maximo de 500R$   #")

    def extrato(self):
        print("Extrato:")
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print('###################################')
                print(f"# Depósito: R$ {deposito:.2f}     ")
            for saque in self.saques:
                print(f"# Saque: R$ {saque:.2f}")

        print(f"# Saldo atual: R$ {self.saldo:.2f}")
        print('###################################')    

def criar_usuario():
    nome = input("Digite o nome do usuário: ")
    print("#-----------------------------------------------------#")
    print(f"#   Usuário {nome} criado com sucesso!")
    return nome


def criar_conta_corrente(usuario):
    
    print(f"#   Conta corrente criada para o usuário {usuario}.")
    print("#-----------------------------------------------------#")
    return ContaBancaria()


# Criação de usuário e conta corrente
usuario = criar_usuario()
conta = criar_conta_corrente(usuario)

# Menu interativo
while True:
    print('###################################')
    print("#     Escolha uma operação        #")
    print("#                                 #")
    print("#         1-> Depósito            #")
    print("#         2-> Saque               #")
    print("#         3-> Extrato             #")
    print("#         4-> Sair                #")
    print("#                                 #")
    print("###################################")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor_deposito = float(input("Digite o valor do depósito: "))
        conta.deposito(valor_deposito)
    elif opcao == "2":
        valor_saque = float(input("Digite o valor do saque: "))
        conta.saque(valor_saque)
    elif opcao == "3":
        conta.extrato()
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, digite uma opção válida.")