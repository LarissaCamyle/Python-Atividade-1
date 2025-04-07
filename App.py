import os

#FUNÇÕES---------------------------------------------------

def encerrar_app ():
    print("""
      
      
      Deseja sair?
      
      """)

#CÓDIGO----------------------------------------------------

print(""" 
▒█▀▀█ █▀▀ █▀▀ ▀▀█▀▀ █▀▀█ █░░█ █▀▀█ █▀▀█ █▀▀▄ ▀▀█▀▀ █▀▀ 
▒█▄▄▀ █▀▀ ▀▀█ ░░█░░ █▄▄█ █░░█ █▄▄▀ █▄▄█ █░░█ ░░█░░ █▀▀ 
▒█░▒█ ▀▀▀ ▀▀▀ ░░▀░░ ▀░░▀ ░▀▀▀ ▀░▀▀ ▀░░▀ ▀░░▀ ░░▀░░ ▀▀▀
      
      """)

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n\n')

opcao_escolhida = input('Escolha uma opção: ')

#limpa programa antes de exibir as opções
os.system('cls')

if opcao_escolhida == "1" :
    print("""======CADASTRO======
    
    
    1.
    2. Deseja sair""")

elif opcao_escolhida == "2" :
    print("""======LISTA DE RESTAURANTES======
    
    
    1.
    2. Deseja sair""")

elif opcao_escolhida == "3" : 
    print("""======ATIVAR RESTAURANTE======
    
    
    1.
    2. Deseja sair""")

elif opcao_escolhida == "4" :
    encerrar_app()