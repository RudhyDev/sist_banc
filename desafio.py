def menu():
    print("""
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    => """)

def depositar(saldo, extrato_conta):
    try:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato_conta += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato_conta

def sacar(saldo, limite, numero_saques, LIMITE_SAQUES, extrato_conta):
    try:
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato_conta += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    except ValueError:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, numero_saques, extrato_conta

def extrato(saldo, extrato_conta):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_conta else extrato_conta)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    saldo = 0
    limite = 500
    extrato_conta = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        menu()
        opcao = input()

        if opcao == "d":
            saldo, extrato_conta = depositar(saldo, extrato_conta)
        elif opcao == "s":
            saldo, numero_saques, extrato_conta = sacar(saldo, limite, numero_saques, LIMITE_SAQUES, extrato_conta)
        elif opcao == "e":
            extrato(saldo, extrato_conta)
        elif opcao == "q":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()