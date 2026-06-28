import json

agenda = {}

def salvar_agenda():
    with open("agenda.json", "w") as arquivo:
        json.dump(agenda, arquivo)

def carregar_agenda():
    global agenda
    try:
        with open("agenda.json", "r") as arquivo:
            agenda = json.load(arquivo)
    except FileNotFoundError:
        agenda = {}
        
def adicionar_contato():
    nome = input("Digite o nome do contato que deseja adicionar :")
    if nome in agenda:
            while True:
                substituir = input(          
'''
Nome ja Existente na agenda !!
Deseja Substituir o telefone ? (s/n)
                                    ''')        
                if substituir == "s" or substituir == "n":
                    break
            
                else:
                    print("Resposta inválida! Digite apenas 's' ou 'n'.")
    
            if substituir == "s":
                tel = input("Digite o numero do telefone:")
                print(f"Seu Contato {nome}, Teve O Numero Alterado Para {tel}")
                agenda[nome] = tel
                salvar_agenda()
            elif substituir == "n":
                print("Inclusão Encerrada")
                return
            
    else:
        tel = input("Digite o numero do telefone novo :")
        agenda[nome] = tel
        print(f"O Contato {nome}, Foi Adicionado Com Sucesso !!")
        salvar_agenda()
         
    

def remover_contato():
    remover = input("Digite o nome do contato que deseja remover :")
    if remover in agenda:
        del agenda[remover]
        print(f"Contato {remover}, Excluido Com Sucesso !!")
        salvar_agenda()
    else: 
        print("Contato nao encontrado")

    

def buscar_contato():
    buscar = (input("Digite o nome do contato :"))
    if buscar in agenda:
        print(f"{buscar} : {agenda[buscar]}")
    else:
        print("Contato nao encontrado")

def exibir_todos():
    if not agenda:
        print("Sua Agenda Esta vazia, Adicione Contatos Para listar")
    else:
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
        
        try:
            escolha = int(input("Digite uma opção :"))
            
        except ValueError:
            print("Digite apenas números, por favor!")
            continue     
         
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
        else:
            print("Numero Invalido Digite Opções Entre 1 e 5 !!")
            continue

carregar_agenda()  
menu()


