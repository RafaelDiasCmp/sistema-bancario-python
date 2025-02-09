import os

# Função para limpar o terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir cabeçalhos com estilo
def exibir_cabecalho(titulo):
    print("\n" + "=" * 40)
    print(f"{titulo.center(40)}")
    print("=" * 40)

# Função para depositar dinheiro na conta
def depositar(conta, valores_depositados):
    while True:
        limpar_tela()
        exibir_cabecalho(" DEPÓSITO ")
        try:
            valor_depo = float(input("Digite o valor para depositar: R$ "))

            if valor_depo <= 0:
                print("\n❌ Valor inválido! Apenas números positivos são permitidos.")
            else:
                valores_depositados.append(valor_depo)
                conta += valor_depo
                print(f"\n✅ Depósito de R${valor_depo:.2f} realizado com sucesso!")

            continuar = input("\nDeseja continuar depositando? (sim/não): ").strip().lower()
            if continuar != 'sim':
                break

        except ValueError:
            print("\n❌ Entrada inválida! Digite um valor numérico.")

    return conta

# Função para exibir o extrato da conta
def exibir_extrato(conta, valores_depositados, valores_sacados):
    limpar_tela()
    exibir_cabecalho(" EXTRATO BANCÁRIO ")

    print(f"💰 Saldo atual: R$ {conta:.2f}\n")

    print("📌 Depósitos realizados:")
    if valores_depositados:
        for valor in valores_depositados:
            print(f"  ➕ R$ {valor:.2f}")
    else:
        print("  Nenhum depósito realizado.")

    print("\n📌 Saques realizados:")
    if valores_sacados:
        for valor in valores_sacados:
            print(f"  ➖ R$ {valor:.2f}")
    else:
        print("  Nenhum saque realizado.")

    print("=" * 40)
    input("\n🔘 Pressione ENTER para voltar ao menu...")

# Função para realizar saques
def realizar_saque(conta, valores_sacados, limite_saques):
    saques_realizados = len(valores_sacados)

    while True:
        limpar_tela()
        exibir_cabecalho(" SAQUE ")

        if saques_realizados >= limite_saques:
            print("\n❌ Limite de 3 saques diários atingido! Tente novamente amanhã.")
            input("\n🔘 Pressione ENTER para voltar ao menu...")
            break

        try:
            valor_saque = float(input("Digite o valor do saque: R$ "))

            if valor_saque > conta:
                print("\n❌ Saldo insuficiente!")
            elif valor_saque > 500:
                print("\n❌ Limite máximo por saque: R$ 500,00")
            else:
                valores_sacados.append(valor_saque)
                conta -= valor_saque
                saques_realizados += 1
                print(f"\n✅ Saque de R$ {valor_saque:.2f} realizado com sucesso!")

            continuar = input("\nDeseja continuar sacando? (sim/não): ").strip().lower()
            if continuar != 'sim':
                break

        except ValueError:
            print("\n❌ Entrada inválida! Digite um valor numérico.")

    return conta
