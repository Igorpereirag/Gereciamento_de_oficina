from lib.interface import *

user = [["ADMIN", "12345", "1"], ["RECEP", "123", "2"], ["MEC", "456", "3"]]
lista_usuarios = []
clientes = []
ordens = []

def atualizarLista(user1):
    global lista_usuarios
    lista_usuarios[:] = []  # limpar a lista com as informações antigas
    for j in user1:
        lista_usuarios.append(j)  # recebe itens da lista user
    with open('save.txt', 'r', encoding="utf8") as arquivo:
        for linha in arquivo:
            apagar = linha.strip("\n")  # apaga o '\n'
            format_text = apagar.split(", ") #cria uma lista por linha com indices dividos pela ','
            lista_usuarios.append(format_text)
        #print(lista_usuarios)
atualizarLista(user)

def atualizarClientes():
    global clientes
    clientes[:] = []  # limpar a lista com as informações antigas
    with open('clientes.txt', 'r', encoding="utf8") as arquivo:
        for linha in arquivo:
            apagar = linha.strip("\n")
            format_text = apagar.split(", ")
            clientes.append(format_text)
        #print(clientes)
atualizarClientes()

def atualizarOrdens():
    global ordens
    ordens[:] = []  # limpar a lista com as informações antigas
    with open('ordens.txt', 'r', encoding="utf8") as arquivo:
        for linha in arquivo:
            apagar = linha.strip("\n")
            format_text = apagar.split(", ")
            ordens.append(format_text)
        #print(ordens)
atualizarOrdens()

# TELA DE LOGIN ----------------------------------------------------------OK
cabecalho("login do sistema")
while True:
    atualizarLista(user)  # atualizar lista
    login = input("\033[1;92mDIGITE SEU USERNAME:\033[m").strip().upper()
    senha = input("\033[1;92mDIGITE SUA SENHA:\033[m").strip().upper()
    for i in lista_usuarios:
        if login == i[0] and senha == i[1]:
            while True:

# 1 - TELA DO ADMIN -------------------------------------------------------OK
                if i[2] == '1':
                    cabecalho(f"SEJA BEM VINDO {i[0]}")
                    r = menu(["Gerenciar funcionários", "Ver ordens de serviço", "visualizar clientes","voltar para tela incial"])
                    if r == 4:
                        cabecalho("Login Do Sistema")
                        break

# 1.1 - TELA GERENCIAR FUNCIONÁRIOS ---------------------------------------OK
                    elif r == 1:
                        while True:
                            cabecalho("Gestao dos funcionarios:")
                            r = menu(["cadastrar funcionário", "deletar funcionário", "Voltar"])

# 1.1.1 - CADASTRAR FUNCIONÁRIO -------------------------------------------OK
                            if r == 1:  # -> cadastrar funcionário
                                while True:
                                    r = 1
                                    funcionario = []
                                    funcionario.append(input("digite o username do novo funcionário: ").strip().upper())
                                    funcionario.append(input("digite sua senha: ").strip().upper())
                                    print("Selecione o cargo do funcionario:")
                                    r = menu(["admin", "recepcionista", "mecanico"])
                                    r = str(r)
                                    funcionario.append(r)
                                    cpf = input('digite o cpf do funcionario: ')
                                    funcionario.append(cpf)
                                    escreverNovoFuncionario(funcionario)
                                    atualizarLista(user)  #atualizando a lista
                                    print("\033[1;92mUsuario cadastrado com sucesso!\033[m")
                                    break

# 1.1.2 - TELA DELETAR FUNCIONÁRIO ----------------------------------------OK
                            elif r == 2:
                                cabecalho("Deletar funcionarios")
                                r = menu(["Digitar qual funcionario deseja deletar", "voltar"])

# 1.1.2.1 - TELA DIGITAR FUNCIONÁRIO PARA DELETAR -------------------------OK
                                if r == 1:
                                    for c, f in enumerate(lista_usuarios):
                                        # 'c' == índice | e 'f' == item
                                        print(f"{c + 1}\t -\t{f}\t")
                                    numero = int(input("Digite o numero do funcionáro para deletar:\n"))

                                    deletarFuncionario(numero, lista_usuarios) # removendo funcionário:
                                    atualizarLista(user)

                                # -> voltar para tela 'DELETAR FUNCIONÁRIO(1.1.2)'
                                if r == 2:
                                    break
                            # -> voltar para 'TELA DO ADMIN'(1)
                            elif r == 3:
                                break

# 1.2 - TELA ORDENS DE SERVIÇO -------------------------------------------OK
                    elif r == 2:
                        while True:
                            cabecalho(" Ordens de serviços")
                            r = menu(["visualizar", "marca como concluida", "Deletar", "voltar"])

# 1.2.1 - VIZUALIZAR ORDENS ----------------------------------------------OK
                            if r == 1:
                                for n, i in enumerate(ordens):
                                    print(
                                      f" {n + 1} \t -\t CPF DO CLIENTE: {i[0]} \t -\t CPF DO MECÂNICO: {i[1]} \t -\t VALOR(R$): {i[2]} \t -\t SERVIÇO: {i[3]} \n")

# 1.2.2 - MARCAR CONCLUIDAS ----------------------------------------------

                            elif r == 2:
                                pass

# 1.2.3 - DELETAR -------------------------------------------------------OK
                            elif r == 3:
                                cabecalho("Deletar Ordem")
                                while True:
                                    for n, i in enumerate(ordens):
                                        print(
                                            f" {n + 1} \t -\t CPF DO CLIENTE: {i[0]} \t -\t CPF DO MECÂNICO: {i[1]} \t -\t VALOR(R$): {i[2]} \t -\t SERVIÇO: {i[3]} \n")
                                    numero = int(input("Digite o numero da ordem para deletar:\n"))
                                    #removendo ordem:
                                    deletarOrdem(numero, ordens)
                                    atualizarOrdens
# 1.2.4 - VOLTAR --------------------------------------------------------
                            elif r == 4:  # -> voltar para 'TELA DO ADMIN'(1)
                                break


# 1.2 - VIZUALIZAR CLIENTES ---------------------------------------------OK
                    elif r == 3:
                        while True:
                            cabecalho("Lista de clientes")
                            for n, i in enumerate(clientes):
                                print(
                                    f" {n+1} \t -\t NOME: {i[0]} \t -\t CPF: {i[1]} \t -\t EMAIL: {i[2]} \t -\t TELEFONE: {i[3]} \t -\t ENDEREÇO: {i[4]} \t -\t PLACA: {i[5]}\n")
                            r = menu(["Digitar qual cliente deseja deletar", "voltar.\n"])

# 1.2.1 - TELA DELETAR CLIENTE ------------------------------------------OK
                            if r == 1:
                                numero = int(input("Digite o numero do funcionáro para deletar:\n"))
                                deletarCliente(numero, clientes) # removendo cliente:
                                atualizarClientes()

                            # -> voltar para tela
                            if r == 2:
                                break

# 1.3.2 - VOLTAR -------------------------------------------------------
                            elif r == 2:  # -> voltar para 'TELA DO ADMIN'(1)
                                break


                # LOGIN DO RECEPCIONISTA
                elif i[2] == '2':

# 2 - TELA DO RECEPCIONISTA -------------------------------------------OK
                    cabecalho(f"Seja bem vindo(a) {i[0]}")
                    r = menu(["Cadastrar clientes", "Ver orçamentos (Transformar em ordem de serviço e deletar", "visualizar clientes", "voltar para tela inicial"])

                    #VOLTAR PARA LOGIN NO SISTEMA
                    if r == 4:
                        cabecalho("Login Do Sistema")
                        break

# 2.1 - TELA CADASTRAR CLIENTE ----------------------------------------OK
                    if r == 1:
                        while True:
                            r = menu(["Cadastrar clientes", "voltar para tela do recepcionista"])
                            if r == 1:

                                Cliente = []
                                Cliente.append(str(input("nome do cliente: ")))
                                Cliente.append(str(input("cpf do cliente: ")))
                                Cliente.append(input("email do cliente: "))
                                Cliente.append(str(input("telefone do cliente: ")))
                                Cliente.append(str(input("Endereço do cliente: ")))
                                Cliente.append(str(input("digite a placa do carro: ")))
                                clientes.append(Cliente)

                                escreverNovoCliente(Cliente)
                                atualizarClientes()
                                print("\033[1;92mCliente cadastrado com sucesso!!\033[m")

                            if r == 2:
                                break

#2.2 - TELA VER ORÇAMENTO ---------------------------------------------
                    elif r == 2:
                        while True:  # -> ver orçamentos (Transformar em ordem de serviço e deletar
                            cabecalho("Ordem de serviços")
                            # mostrar orçamentos
                            r = menu(["voltar"])
                            if r == 1:
                                break

#2.3 - TELA VISUALIZAR CLIENTES ---------------------------------------
                    elif r == 3:
                        while True:
                            cabecalho("Lista de clientes")
                            r = menu(["Ver Lista","voltar"])
                            if r == 1:
                                atualizarClientes()
                                for n, i in enumerate(clientes):
                                    print(
                                        f" {n+1} \t -\t NOME: {i[0]} \t -\t CPF: {i[1]} \t -\t EMAIL: {i[2]} \t -\t TELEFONE: {i[3]} \t -\t ENDEREÇO: {i[4]} \t -\t PLACA: {i[5]}\n")

                            r = menu(["voltar"]) #HELP! NÃO CONSIGO VOLTAR PARA O MENU RECEPCIONISTA!
                            if r == 2:
                                break


                # LOGIN DO MECÂNICO
                elif i[2] == "3":
# 3 - TELA DO MECÂNICO -------------------------------------------OK!
                    cabecalho(f"seja bem vindo {i[0]}")
                    r = menu(
                        ["Cadastrar orçamento (cadastrar)", "Ver ordens de serviço (apenas as que possuem o cpf dele)",
                         "voltar para tela inicial"])
                    #VOLTAR
                    if r == 3:
                        cabecalho("LOGIN DO SISTEMA")
                        break

# 3.1 - TELA CADASTRAR ORÇAMENTO -----------------------------------
                    elif r == 1:
                        while True:
                            cabecalho("cadastrar orçamento")
                            r = menu(["coninuar para cadastar orçamento", "voltar"])

                            if r == 1:
                                Ordem = []
                                Ordem.append(input("Digite o CPF do cliente:\n"))
                                Ordem.append(input("Digite o CPF do Mecânico:\n"))
                                Ordem.append(input("Digite o valor do serviço:\n"))
                                Ordem.append(input("Digite o Serviço:\n"))
                                ordens.append(Ordem)

                                escreverNovaOrdem(Ordem)
                                atualizarOrdens()
                            print("\033[1;92mCliente cadastrado com sucesso!!\033[m")

# 3.2 - TELA VER ORDENS DE SERVIÇO -------------------------------OK!
                    if r == 2:
                        while True:
                            cabecalho("ordens de serviços no seu CPF:")
                            for i in lista_usuarios:
                                if i[0] == login and i[1] == senha:
                                        cpf = i[3]
                                        controle = 0
                                        for id in ordens:
                                            controle += 1
                                            if id[1] == cpf:
                                                p = ordens[controle-1]
                                                print(p)

                else:
                    print("\033[1;31mLogin ou Senha incorretos! Tente novamente.\033[m")