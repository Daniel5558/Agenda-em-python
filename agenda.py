agenda = {}
def adicionar_contato():
    nome = input("Digite o nome do contato que deseja adicionar :")
    tel = input("Digite o numero do telefone :")
    
    agenda[nome] = tel

def remover_contato():
    remover = input("Digite o nome do contato que deseja remover :")
    if remover in agenda:
        del agenda[remover]
    else: 
        print("Contato nao encontrado")

def buscar_contato():
    buscar = (input("Digite o nome do contato :"))
    if buscar in agenda:
        print(agenda[buscar])
    else:
        print("Contato nao encontrado")

def exibir_todos():
    for nome in agenda:
        print(f"{nome} : {agenda[nome]}")
        
def menu():
    while True:
        print("====== AGENDA =======")
        print('''
1 - Adicionar contato
2 - Remover contato
3 - Buscar contato
4 - Exibir todos
5 - Sair
        ''')
        escolha = int(input(""))
        if escolha == 1:
            adicionar_contato()
        elif escolha == 2:
            remover_contato()
        elif escolha == 3:
            buscar_contato()
        elif escolha == 4:
            exibir_todos()
        elif escolha == 5:
            print("Encerrando...")
            break
        
menu()
