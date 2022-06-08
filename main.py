from lib.interface import *

user = [["ADMIN", "12345", "1"], ["RECEP", "123", "2"], ["MEC", "456", "3"]]
clientes = []

#TELA DE LOGIN -------------------------------------------------------
cabecalho("login do sistema")
while True: #adicionar mensagem de 'Login incorreto, tente novamente.''
    login = str(input("\033[1;92mDIGITE SEU USENAME:\033[m").strip().upper())
    senha = str(input("\033[1;92mDIGITE SUA SENHA:\033[m").strip().upper())
    for i in user:
        if login == i[0] and senha == i[1]:
            while True:
              
#1 - TELA DO ADMIN --------------------------------------------------
                if i[2] == '1':  
                    cabecalho(f"SEJA BEM VINDO {i[0]}")
                    r = menu(["Gerenciar funcionários", "Ver ordens de serviço", "visualizar clientes",
                              "voltar para tela incial"])
                    if r == 4:
                        cabecalho("Login Do Sistema")
                        break

#1.1 - TELA GERENCIAR FUNCIONÁRIOS ---------------------------------------
                    elif r == 1:
                        while True:
                            cabecalho("Gestao dos funcionarios:")
                            r = menu(["cadastrar funcionário", "deletar funcionário", "Voltar"])

#1.1.1 - CADASTRAR FUNCIONÁRIO --------------------------------------
                            if r == 1:# -> cadastrar funcionário
                                while True:
                                    r = 1
                                    funcionario = []
                                    funcionario.append(str(input("digite seu username").strip().upper())) #do novo funcionário ou do ADMIN?
                                    funcionario.append(str(input("digite sua senha").strip().upper()))
                                    print("Selecione o cargo do funcionario")
                                    r = menu(["admin", "recepcionista", "mecanico"])
                                    r = str(r)
                                    funcionario.append(r)
                                    user.append(funcionario)
                                    cpf = int(input('digite o cpf do funcionario:'))
                                    #user.append(funcionario) lista user recebendo duas vezes o mesmo funcionário
                                    print("\033[1;92mUsuario cadastrado com sucesso\033[m")
                                    break

#               1.1.2 - TELA DELETAR FUNCIONÁRIO - MELHORAR---------------------
                            elif r == 2: #-> deletar funcionário
                                cabecalho("Deletar funcionarios")
                                r = menu(["Digitar qual funcionario deseja deletar", "voltar"])
#                       1.1.2.1 - DIGITAR FUNCIONÁRIO ----------------
                                if r == 1: #-> digitar qual funcionario deseja deletar
                                    for c, f in enumerate(user):
                                        # 'c' == índice | e 'f' == item
                                        print(f"{c + 1}\t -\t{f}\t")
                                    print("Digite o numero do funcionáro para deletar:\n.")
                                    #removendo funcionário:


                                #VOLTAR
                                if r ==2: #-> voltar para tela 'DELETAR FUNCIONÁRIO(1.1.2)'
                                    break

#               1.1.3 - VOLTAR ---------------------------------------
                            elif r == 3:# -> voltar para 'TELA DO ADMIN'(1)
                                break

#       1.2 - TELA ORDENS DE SERVIÇO ---------------------------------
                    elif r == 2:
                        while True:
                            cabecalho(" Ordens de serviços")
                            r = menu(["visualizar", "marca como concluida", "Deletar", "voltar"])

#               1.2.1 - VIZUALIZAR ORDENS ----------------------------
                            if r == 1: #-> visualizar
                                pass

#               1.2.2 - MARCAR CONCLUIDAS ----------------------------

                            elif r == 2: #-> marca como concluida
                                pass

#               1.2.3 - DELETAR --------------------------------------
                            elif r == 3: #-> deletar
                                pass

#               1.2.4 - VOLTAR ---------------------------------------
                            elif r == 4: #-> voltar para 'TELA DO ADMIN'(1)
                                break

#       1.3 - VIZUALIZAR CLIENTES ------------------------------------
                    elif r == 3:
                        while True: #-> visualizar clientes
                            cabecalho("Lista de clientes")
                            print(f"{clientes}")
                            r = menu(["deletar","voltar"])
#                1.3.1 - DELETAR -------------------------------------
                            if r == 1: #-> deletar cliente
                                pass
#                1.3.2 - VOLTAR --------------------------------------
                            elif r == 2: #-> voltar para 'TELA DO ADMIN'(1)
                                break

                #LOGIN DO RECEPCIONISTA
                elif i[2] == '2':

# 2 - TELA DO RECEPCIONISTA -------------------------------------------
                    cabecalho(f"Seja bem vindo(a) {i[0]}")
                    r = menu(["Cadastrar clientes", "Ver orçamentos (Transformar em ordem de serviço e deletar",
                              "visualiza clientes", "voltar para tela inicial"])
                    if r == 4:#-> Voltar a tela inicial
                        cabecalho("Login Do Sistema")
                        break
                    if r == 1: #-> cadastrar clientes
                        while True:
                            if r == 1:
                                # adicionar a opção voltar
                                cliente = []
                                cliente.append(str(input("nome do cliente")))
                                cliente.append(int(input("cpf do cliente")))
                                cliente.append(input("email do cliente"))
                                cliente.append(int(input("telefone do cliente")))
                                cliente.append(str(input("Endereço DO CLEINTE")))
                                cliente.append(str(input("digite a placa do carro")))
                                clientes.append(cliente)
                                print("\033[1;92mCliente cadastrado com sucesso!!\033[m")
                                if r == 1:
                                    break
                    elif r == 2:
                        while True:#-> ver orçamentos (Transformar em ordem de serviço e deletar
                            cabecalho("Ordem de serviços")
                            #mostrar orçamentos
                            r = menu(["voltar"])
                            if r == 1:
                                break
                    elif r == 3: #-> visualizar clientes
                        while True:
                            cabecalho("Lista de clientes")
                            print(f"{clientes}")
                            r = menu(["voltar"])
                            if r == 1:
                                break

                #LOGIN DO MECÂNICO
                elif i[2] == "3":
# 3 - TELA DO MECÂNICO -------------------------------------------
                    cabecalho(f"seja bem vindo {i[0]}")
                    r = menu(
                        ["Cadastrar orçamento (cadastrar)", "Ver ordens de serviço (apenas as que possuem o cpf dele)",
                         "voltar para tela inicial"])
                    if r == 3:
                        cabecalho("LOGIN DO SISTEMA")
                        break
                    elif r == 1:
                        while True:
                            cabecalho("cadastrar orçamento")
                            r = menu(["voltar"])
                            if r == 1:
                                break

                    elif r == 2:
                        while True:
                            cabecalho("ordens de serviços")
                            r = menu(["voltar"])
                            if r == 1:
                                break

                else:
                    print("\033[1;31mLogin ou Senha incorretos! Tente novamente.\033[m")
