''' Um grande banco nos contratou para desenvolver o seu novo sistema> Esse banco deseja modernizar suas operações e paara isso escolhe a linguagem python. Para sua primeira versão do sistema devemos implementar apenas 3 operacoes: depósito, saque e extrato
'''

usuario = input('digite seu nome completo: ')

mensagem = '''Olá {}, seja bem vindo(a) ao nosso banco, estou aqui para ajuda-lo(a)!.'''.format(usuario.title())
print(mensagem)


menu = '''
[1] - Extrato
[2] - Saque
[3] - Deposito
[4] - Sair
'''
saldo = 0
limite = 1000
extrato = ''
numero_saques = 0
limite_saque = 5


while True:

    opcoes = int(input('digite uma opcao: '+ (menu)))

    if opcoes == 3:

        valor = float(input('digite o valor que deseja depositar: '))

        if valor > 0:
            saldo += valor
            extrato = f'Deposito: R$ {valor:.2f}\n'
        
        else:
            print('Operação falhou! Valor digitado é invalido')


    elif opcoes == 2:
        valor = float(input('digite o valor a sacar: '))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saque

        if excedeu_saldo:
            print('Operacao falhou! Valor excede o saldo')
        elif excedeu_limite:
            print('Operacao falhou! O valor excedeu o limite ')
        elif excedeu_saques:
            print('Operacao falhou! Seu limite de saques foi excedido')
        
        elif valor > 0:
            saldo -= valor
            extrato = f'Saque R${valor:.2f}\n'
            numero_saques +=1
    
        else:
            print('opção invalida')

    elif opcoes == 1:
        print('\n==============Extrato==============')
        #if/else tenario
        print('Não foram feitas transições'if not extrato else extrato)
        print('\n====================================')
    
    elif opcoes == 4:
       break

    else:
        print('opcao invalida! Por favor tente novamente')






print('Obrigado por utilizar nossos serviços')




       


        
