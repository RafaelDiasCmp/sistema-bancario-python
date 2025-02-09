from banco import limpar_tela, exibir_cabecalho, depositar, exibir_extrato, realizar_saque

def programa_principal():
    conta = 0
    valores_depositados = []
    valores_sacados = []
    LIMITE_SAQUES_DIARIOS = 3  # Limite máximo de saques por dia

    while True:
        limpar_tela()
        exibir_cabecalho(" 🏦 BANCO PYTHON ")

        print("[1] 💰 DEPOSITAR")
        print("[2] 💸 SACAR")
        print("[3] 📜 EXIBIR EXTRATO")
        print("[4] 🚪 SAIR")
        print("=" * 40)

        opcao = input("\nEscolha uma opção: ")

        if opcao == '1':
            conta = depositar(conta, valores_depositados)
        elif opcao == '2':
            conta = realizar_saque(conta, valores_sacados, LIMITE_SAQUES_DIARIOS)
        elif opcao == '3':
            exibir_extrato(conta, valores_depositados, valores_sacados)
        elif opcao == '4':
            limpar_tela()
            exibir_cabecalho(" OBRIGADO POR USAR O BANCO PYTHON! ")
            print("\n👋 Até a próxima!\n")
            break
        else:
            print("\n❌ Opção inválida! Escolha uma opção entre 1 e 4.")

# Executa o programa
if __name__ == "__main__":
    programa_principal()
