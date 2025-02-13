import sys
sys.path.append('c:/Users/raffa/OneDrive/Desktop/sistema bancário')


from banco_v2.menu import menu, depositar, sacar, exibir_extrato, criar_cliente, criar_conta, listar_contas

from colorama import Fore, Style




def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print(f"\n{Fore.RED}Saindo do sistema... Até logo!{Style.RESET_ALL}")
            break

        else:
            print(f"{Fore.RED}@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
