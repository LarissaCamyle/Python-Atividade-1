import os
 
#FUNÇÕES PRINCIPAIS---------------------------------------------------

def iniciar_programa () :  
    print(""" 
    ▒█▀▀█ █▀▀ █▀▀ ▀▀█▀▀ █▀▀█ █░░█ █▀▀█ █▀▀█ █▀▀▄ ▀▀█▀▀ █▀▀ 
    ▒█▄▄▀ █▀▀ ▀▀█ ░░█░░ █▄▄█ █░░█ █▄▄▀ █▄▄█ █░░█ ░░█░░ █▀▀ 
    ▒█░▒█ ▀▀▀ ▀▀▀ ░░▀░░ ▀░░▀ ░▀▀▀ ▀░▀▀ ▀░░▀ ▀░░▀ ░░▀░░ ▀▀▀
        
        """)

    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n\n')

def printar_opcoes():
    opcao_escolhida = input('Escolha uma opção: ')

    if opcao_escolhida == "1" :
        cadastrar_novo_restaurante()
    elif opcao_escolhida == "2" :
        listar_restaurantes()
    elif opcao_escolhida == "3" : 
        alterar_status_restaurante()
    elif opcao_escolhida == "4" :
        encerrar_app()
    else:
        opcao_invalida()


#pequenas tarefas

def encerrar_app ():
    #limpar terminal
    os.system('cls')
    exit()

def voltar_para_comeco():
    input("""                   
        Digite qualquer tecla para voltar ao início = 
    """)
    main()

def opcao_invalida():
    input(""" 
        Opção inválida!
    """)
    voltar_para_comeco()

def exibir_titulo(titulo):
    os.system('cls')
    decoracao = '═' * (len(titulo))

    print(f'                {decoracao}')
    print(f'                {titulo}')
    print(f'                {decoracao}\n')


#Cadastro-------------------

#lista de restaurantes
restaurantes = [{'nome':'Poletto', 'categoria':'Massas', 'status':True},
                {'nome':'Madero', 'categoria':'Massas', 'status':False}]

def cadastrar_novo_restaurante():
    exibir_titulo("CADASTRO DE NOVOS RESTAURANTES")

    #entrada de dados
    nome = input('Digite o nome do restaurante = ')
    categoria = input('Digite a categoria = ')

    #armazenamento de dados
    dados_do_restaurante = {'nome':nome, 'categoria':categoria, 'status':False}

    #salvando dados na lista
    restaurantes.append(dados_do_restaurante)

    print(f'\nO restaurante {nome} foi cadastrado com sucesso!\n')

    voltar_para_comeco()


#listar--------------------

def listar_restaurantes():
    exibir_titulo("LISTA DE RESTAURANTES")

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        #se o status é true printa ativo, e se for falso printa desativado
        status = 'Ativo ' if restaurante['status'] else 'Desativado'
        print(f'NOME = {nome}\nCATEGORIA = {categoria}\nSTATUS = {status}\n\n')

    voltar_para_comeco()


#alterar------------------

def alterar_status_restaurante():
    exibir_titulo("ALTERAR STATUS DO RESTAURANTE")

    nome = input("Digite o nome do restaurante que deseja alterar o status = ")

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome == restaurante['nome']:
            restaurante_encontrado = True
            #coloca o status contrario do q ja foi armazenado
            restaurante['status'] = not restaurante['status']
            if restaurante['status']:
                mensagem = f'\nO status do restaurante {restaurante["nome"]} foi alterado com sucesso!\n'
            else:
                mensagem = f'\nO status do restaurante {restaurante["nome"]} não foi alterado!\n'
            print(mensagem)
        else:
            opcao_invalida()

    voltar_para_comeco()

    

#MAIN---------------------------------------------------


#transforma o App.py em main
def main():
    os.system('cls')
    iniciar_programa()
    printar_opcoes()
    encerrar_app()

if __name__ == '__main__':
    main()
















    