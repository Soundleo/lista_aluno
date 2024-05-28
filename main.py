# lista de aluno

import os 
import time
lista = []

while True:

    print (f'{'='*20}lsita de pessoas do curso Python{'='*20} ')
    print ('Informe a opção desejada de 1 a 7')
    print('1 - cadastrar pessoas')
    print('2 - listar pessoas cadastradas ')
    print('3 - pesquisar pelo nome da pessoa')
    print('4 - ordenar a lista por ordem alfabética')
    print('5 - atualizar o nome ')
    print('6 - Deletar o nome ')
    print('7 - sair do programa ')

    # seleção da opçao

    opcao = int(input('Informe a opção desejada:\n'))

    # executar o case
    os.system('cls')
    match opcao:
        case 1:
            nome = input('Informe o nome da criatura: ').capitalize()
            lista.append(nome)
            continue          
        case 2:
            lista.sort()
            for impressao_lista in lista:            
                print (impressao_lista)
            time.sleep(10)
            continue   
        case 3:
            nome = input('Informe qual o nome que deseja pesquisar?\n').capitalize()
            if nome in lista:
                print(f'O aluno {nome} está matriculado.' )
            else:
                print(f'O {nome} não está matriculado')
                continue
        case 4:
            lista.sort()
            for impressao_lista in lista:            
                print (impressao_lista)
            time.sleep(10)
            continue
        case 5: 
            try:
                nome = input('Informe o nome de quem vc quer alterar o nome: ').capitalize() 
                indice =lista.index(nome)
                novo_nome = input('Insira o novo nome: ').capitalize
                lista[indice] = novo_nome
                print ('Nome alterado com sucesso')
                continue
            except: 
                print(f'O {nome} não está na lista')              
            continue
        case 6:
            try:
             nome = input('Informe o nome que deseja deletar?').capitalize()
            #  indice =lista.index(nome)
             lista.remove(nome)
             print(f'Nome excluido com sucesso')
            except:
                print(f'O {nome} não está na lista')
        case 7:
            print (f'{'='*116}')
            print (f'{'='*116}')
            print (f'{'='*116}')
            print (f'{'='*50}FIM DE PROGRAMA{'='*51}')
            print (f'{'='*116}')
            print (f'{'='*116}')
            print (f'{'='*116}')
            break
        case _:
            print ('NÚmero informado errado')
            continue