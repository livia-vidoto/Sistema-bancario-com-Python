menu = """\n
Seja bem vindo ao PyPag!!!
================ MENU ================
[1] depositar
[2] sacar
[3] extrato
[x] sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input('Informe o valor do depósito: '))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
            print('Operação realizada com sucesso!!')
        else:
            print('Operação inválida! Tente novamente.')
    
    elif opcao == "2":
        valor = float(input('Informe o valor do saque: '))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if valor <= 0:
            print('Operação falhou! O valor informado é inválido.')
        elif excedeu_saldo:
            print('Erro!! Você não tem saldo suficiente para esta operação.')
        elif excedeu_limite:
            print(f'Erro!! O valor do saque é maior do que {limite}.')
        elif excedeu_saques:
            print('Erro!! Você só pode realizar três saques diários.')
        else:
            saldo -= valor
            extrato += (f'Saque: $ {valor:.2f}\n')
            numero_saques += 1

    elif opcao == "3":
        print('----------------------------------------\n')
        print('EXTRATO')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: $ {saldo:.2f}')
        print('----------------------------------------')

    elif opcao == "x":
        print('O PyPag agradece sua preferência!')
        print()
        break

    else:
        print('Operação inválida! Tente novamente.')
