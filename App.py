import os
 
#FUNÇÕES PRINCIPAIS---------------------------------------------------

def iniciar_programa () : 
    ''' Essa função é resposável por printar a tela inicial do programa'''

    os.system('cls')
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
    ''' Essa função é resposável por printar as opções do menu e ir para o menu desejado
    
    Input : A opção escolhida no menu 
    '''
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
        opcao_invalida('')


#pequenas tarefas

def encerrar_app():
    ''' Essa função é resposável por encerrar o programa'''

    #limpar terminal
    os.system('cls')
    exit()

def voltar_para_comeco():
    ''' Essa função é resposável por voltar a tela inicial do programa'''

    input("""
                             
        Digite qualquer tecla para voltar ao início = 
    """)
    main()

def opcao_invalida(texto):
    ''' Essa função é resposável por printar uma mensagem de erro, a mensagem pode ser personalizada ou automática
    
    Input : A mensagem de erro (opcional)
    '''

    if texto == '':
        input(""" 
            Opção inválida!
        """)
    else:
        input(f""" 
            {texto}
        """)
    voltar_para_comeco()

def exibir_titulo(titulo):
    ''' Essa função é resposável por printar um título
    
    Input : Título
    '''

    os.system('cls')
    decoracao = '═' * (len(titulo))

    print(f'                {decoracao}')
    print(f'                {titulo}')
    print(f'                {decoracao}\n')

def validar_input(input):
    ''' Essa função é resposável por verificar se o input realizado está vazio
    
    Input : o input realizado pelo usuário
    '''
    
    if input == '':
        opcao_invalida('Entrada de dados vazia, favor digitar corretamente as informações!') 


#Cadastro-------------------

#lista de restaurantes
restaurantes = [{'nome':'Poletto', 'categoria':'Massas', 'status':True},
                {'nome':'Madero', 'categoria':'Massas', 'status':False}]

def cadastrar_novo_restaurante():
    ''' Essa função é resposável por criar um novo restaurante
    
    Input : Nome do restaurante e categoria do restaurante
    Output: Salva o restaurante novo na lista de restaurantes
    '''

    exibir_titulo("CADASTRO DE NOVOS RESTAURANTES")

    #entrada de dados
    nome = input('Digite o nome do restaurante = ')
    validar_input(nome)
    categoria = input('Digite a categoria = ')
    validar_input(categoria)

    #armazenamento de dados
    dados_do_restaurante = {'nome':nome, 'categoria':categoria, 'status':False}

    #salvando dados na lista
    restaurantes.append(dados_do_restaurante)

    print(f'\nO restaurante {nome} foi cadastrado com sucesso!\n')

    voltar_para_comeco()


#listar--------------------

def listar_restaurantes():
    ''' Essa função é resposável por listar todos os restaurantes'''

    exibir_titulo("LISTA DE RESTAURANTES")

    #titulo da tabela
    print(f'{'  NOME'.ljust(20)}  {'   Categoria'.ljust(20)}  {'   Status'.ljust(20)}\n')

    for restaurante in restaurantes:
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        #se o status é true printa ativo, e se for falso printa desativado
        status = 'Ativo ' if restaurante['status'] else 'Desativado'
        print(f'★ {nome.ljust(20)} ║ {categoria.ljust(20)} ║ {status.ljust(20)}')

    voltar_para_comeco()


#alterar------------------

def alterar_status_restaurante():
    ''' Essa função é resposável por alterar o status do restaurante
    
    Input : Nome do restaurante
    Output : Status do restaurante 
    '''

    exibir_titulo("ALTERAR STATUS DO RESTAURANTE")

    nome = input("Digite o nome do restaurante que deseja alterar o status = ")

    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome == restaurante['nome']:
            restaurante_encontrado = True
            #coloca o status contrario do q ja foi armazenado
            restaurante['status'] = not restaurante['status']

            status_restaurante = 'Ativo' if restaurante['status'] else 'Desativado'

            mensagem = f'\nO status do restaurante {restaurante["nome"]} foi alterado para {status_restaurante} com sucesso!\n'
            print(mensagem)
    if restaurante_encontrado == False:
        opcao_invalida('\nRestaurante não encontrado!')

    voltar_para_comeco()

    

#MAIN---------------------------------------------------


#transforma o App.py em main
def main():
    ''' Essa função é resposável pela ordem da execução do programa'''
    
    os.system('cls')
    iniciar_programa()
    printar_opcoes()
    encerrar_app()

if __name__ == '__main__':
    ''' Transforma o arquivo atual (App.py) no arquivo principal do código'''
    main()
















    