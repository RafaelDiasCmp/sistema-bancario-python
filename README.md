# Sistema Bancário Python

Este é um simples **Sistema Bancário** desenvolvido em **Python**. Ele permite que os usuários realizem depósitos, saques e visualizem extratos bancários, utilizando uma interface de linha de comando interativa. O programa simula a funcionalidade de um banco, permitindo que os usuários gerenciem seus saldos de maneira fácil e intuitiva.

## Funcionalidades

- **Depositar**: O usuário pode adicionar dinheiro à sua conta bancária.
- **Sacar**: O usuário pode realizar saques, com um limite de R$500 por transação e um limite diário de 3 saques.
- **Extrato**: O usuário pode visualizar o extrato bancário, com o saldo atual, depósitos realizados e saques efetuados.
- **Limpeza da tela**: A tela do terminal é limpa após cada operação para uma interface mais limpa.

## Requisitos

Para rodar o projeto, é necessário ter o Python instalado em sua máquina. O código foi desenvolvido para funcionar com versões do Python 3.x.

## Fluxo do Programa

1. **Menu Principal**: O programa exibe um menu com quatro opções:
   - **[1] 💰 DEPOSITAR**: Adicione dinheiro à sua conta.
   - **[2] 💸 SACAR**: Realize saques da sua conta (com limite diário de saques).
   - **[3] 📜 EXIBIR EXTRATO**: Visualize seu saldo atual e as transações realizadas.
   - **[4] 🚪 SAIR**: Encerre o programa.

2. **Depósitos**: O valor depositado é somado ao saldo da conta e armazenado em uma lista de depósitos realizados.

3. **Saques**: O programa permite até 3 saques por dia, com um valor máximo de R$500 por transação.

4. **Extrato**: O programa exibe o saldo atual da conta, os depósitos realizados e os saques efetuados.

