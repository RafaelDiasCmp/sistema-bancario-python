import textwrap
from colorama import Fore, Back, Style
from banco_v2.banco_poo import Cliente, PessoaFisica, ContaCorrente, Deposito, Saque



def imprimir_titulo(titulo):
    """Função para imprimir títulos com borda"""
    print(f"{Fore.GREEN}{Back.BLACK}{Style.BRIGHT}")
    print("=" * (len(titulo) + 4))
    print(f"  {titulo}")
    print("=" * (len(titulo) + 4))
    print(Style.RESET_ALL)

def menu():
    menu = f"""
    {Fore.YELLOW}{Style.BRIGHT}=============== MENU ================
    {Fore.CYAN}[d]{Style.RESET_ALL}\tDepositar
    {Fore.CYAN}[s]{Style.RESET_ALL}\tSacar
    {Fore.CYAN}[e]{Style.RESET_ALL}\tExtrato
    {Fore.CYAN}[nc]{Style.RESET_ALL}\tNova conta
    {Fore.CYAN}[lc]{Style.RESET_ALL}\tListar contas
    {Fore.CYAN}[nu]{Style.RESET_ALL}\tNovo usuário
    {Fore.RED}[q]{Style.RESET_ALL}\tSair
    {Fore.YELLOW}===================================={Style.RESET_ALL}
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print(f"{Fore.RED}@@@ Cliente não possui conta! @@@{Style.RESET_ALL}")
        return
    return cliente.contas[0]


def depositar(clientes):
    cpf = input(f"{Fore.MAGENTA}Informe o CPF do cliente: {Style.RESET_ALL}")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f"{Fore.RED}@@@ Cliente não encontrado! @@@{Style.RESET_ALL}")
        return

    valor = float(input(f"{Fore.MAGENTA}Informe o valor do depósito: {Style.RESET_ALL}"))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input(f"{Fore.MAGENTA}Informe o CPF do cliente: {Style.RESET_ALL}")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f"{Fore.RED}@@@ Cliente não encontrado! @@@{Style.RESET_ALL}")
        return

    valor = float(input(f"{Fore.MAGENTA}Informe o valor do saque: {Style.RESET_ALL}"))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input(f"{Fore.MAGENTA}Informe o CPF do cliente: {Style.RESET_ALL}")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f"{Fore.RED}@@@ Cliente não encontrado! @@@{Style.RESET_ALL}")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    imprimir_titulo("EXTRATO")

    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{Fore.YELLOW}{transacao['tipo']}:{Style.RESET_ALL}\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\n{Fore.GREEN}Saldo:\n\tR$ {conta.saldo:.2f}{Style.RESET_ALL}")
    print("=" * 50)


def criar_cliente(clientes):
    cpf = input(f"{Fore.MAGENTA}Informe o CPF (somente número): {Style.RESET_ALL}")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print(f"{Fore.RED}@@@ Já existe cliente com esse CPF! @@@{Style.RESET_ALL}")
        return

    nome = input(f"{Fore.MAGENTA}Informe o nome completo: {Style.RESET_ALL}")
    data_nascimento = input(f"{Fore.MAGENTA}Informe a data de nascimento (dd-mm-aaaa): {Style.RESET_ALL}")
    endereco = input(f"{Fore.MAGENTA}Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): {Style.RESET_ALL}")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print(f"{Fore.GREEN}=== Cliente criado com sucesso! ==={Style.RESET_ALL}")


def criar_conta(numero_conta, clientes, contas):
    cpf = input(f"{Fore.MAGENTA}Informe o CPF do cliente: {Style.RESET_ALL}")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print(f"{Fore.RED}@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@{Style.RESET_ALL}")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print(f"{Fore.GREEN}=== Conta criada com sucesso! ==={Style.RESET_ALL}")


def listar_contas(contas):
    imprimir_titulo("LISTA DE CONTAS")

    for conta in contas:
        print("=" * 50)
        print(f"{Fore.CYAN}{Style.BRIGHT}{str(conta)}{Style.RESET_ALL}")
    print("=" * 50)
