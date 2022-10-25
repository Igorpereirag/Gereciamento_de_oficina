from lib.interface import *

user = [["ADMIN", "12345", "1"], ["RECEP", "123", "2"], ["MEC", "456", "3"]]
lista_usuarios = []
clientes = []
orcamentos = []
ordens = []


def atualizarLista(user1):
    global lista_usuarios
    lista_usuarios[:] = []  # limpar a lista com as informações antigas
    for j in user1:
        lista_usuarios.append(j)  # recebe itens da lista user
    with open('funcionarios.txt', 'r', encoding="utf8") as arquivo:
        for linha in arquivo:
            apagar = linha.strip("\n")  # apaga o '\n'
            format_text = apagar.split(
                ", ")  # cria uma lista por linha com indices dividos pela ','
            lista_usuarios.append(format_text)
        # print(lista_usuarios)


atualizarLista(user)


def atualizarClientes():
    global clientes
    clientes[:] = []  # limpar a lista com as informações antigas
    with open('clientes.txt', 'r', encoding="utf8") as arquivo:
        for linha in arquivo:
            apagar = linha.strip("\n")
            format_text = apagar.split(", ")
            clientes.append(format_text)
        # print(clientes)


atualizarClientes()


def atualizarOrcamentos():
    global orcamentos
    orcamentos[:] = []  # limpar a lista com as informações antigas
    with open('orcamentos.txt', 'r', encoding="utf8") as arquivo:
        for linha in arquivo:
            apagar = linha.strip("\n")
            format_text = apagar.split(", ")
            orcamentos.append(format_text)
        # print(ordens)


atualizarOrcamentos()


def atualizarOrdens():
    global ordens
    ordens[:] = []  # limpar a lista com as informações antigas
    with open('ordens.txt', 'r', encoding="utf8") as arquivo:
        for linha in arquivo:
            apagar = linha.strip("\n")
            format_text = apagar.split(", ")
            ordens.append(format_text)
        # print(ordens)


atualizarOrdens()


def atualizarOrcamentos():
    global orcamentos
    orcamentos[:] = []
    with open('orcamentos.txt', 'r', encoding="utf8") as arquivo:
        for linha in arquivo:
            apagar = linha.strip("\n")
            format_text = apagar.split(", ")
            orcamentos.append(format_text)
        # print(ordens)


atualizarOrcamentos()
# TELA DE LOGIN ------------------------------------------------------------OK
cabecalho("login do sistema")
while True:
    atualizarLista(user)  # atualizar lista
    login = input("\033[1;92mDIGITE SEU USERNAME:\033[m").strip().upper()
    senha = input("\033[1;92mDIGITE SUA SENHA:\033[m").strip().upper()
    for i in lista_usuarios:
        if login == i[0] and senha == i[1]:

            # 1 - TELA DO ADMIN -------------------------------------------------------OK
            while True:
                if i[2] == '1':
                    cabecalho(f"SEJA BEM VINDO {i[0]}")
                    r = menu([
                        "Gerenciar/Editar funcionários", "Ver ordens de serviço",
                        "visualizar clientes", "deletar clientes",
                        "voltar para tela incial"
                    ])
                    if r == 5:
                        cabecalho("Login Do Sistema")
                        break

                    # 1.1 - TELA GERENCIAR FUNCIONÁRIOS ---------------------------------------OK
                    elif r == 1:
                        while True:
                            cabecalho("Gestao dos funcionarios:")
                            r = menu([
                                "cadastrar funcionário", "editar funcionário", "deletar funcionário",
                                "Voltar"
                            ])

                            if r == 4:
                                break
                            # 1.1.1 - CADASTRAR FUNCIONÁRIO -------------------------------------------OK
                            elif r == 1:  # -> cadastrar funcionário
                                while True:
                                    funcionario = []
                                    funcionario.append(
                                        input(
                                            "digite o username do novo funcionário: ").strip().upper())
                                    if funcionario[0] == "0":
                                      break
                                    funcionario.append(
                                        input("digite sua senha: ").strip().
                                            upper())
                                    print("Selecione o cargo do funcionario:")
                                    var = menu(
                                        ["admin", "recepcionista", "mecanico"])
                                    var = str(var)
                                    funcionario.append(var)
                                    cpf = input(
                                        'digite o cpf do funcionario: ')
                                    funcionario.append(cpf)
                                    escreverNovoFuncionario(funcionario)
                                    atualizarLista(user)  # atualizando a lista
                                    print(
                                        "\033[1;92mUsuario cadastrado com sucesso!\033[m"
                                    )
                                    break

                            # 1.1.2 - TELA EDITAR FUNCIONÁRIO ----------------------------------------OK
                            elif r == 2:
                                while True:
                                    teste = len(lista_usuarios)
                                    # mostrando todas as ordens como um menu:
                                    if teste != 0 and teste > 3:
                                        cabecalho("editar funcionarios")
                                        m = menu([
                                            "Escolher funcionário",
                                            "voltar"])
                                        if m == 2:
                                            break
                                        elif m == 1:
                                            #mostrar lista de usuários:
                                            for c, f in enumerate(lista_usuarios):
                                                print(f"{c + 1}\t -\t{f}\t")

                                            num = int(input("Digite a posição do funcionário que deseja editar.\n"))
                                            editarFuncionario(num, lista_usuarios)
                                            atualizarLista(user)

                                    else:
                                        print("Não há funcináros registrados ainda.")
                                        break


                            # 1.1.3 - TELA DELETAR FUNCIONÁRIO ----------------------------------------OK
                            elif r == 3:
                                while True:
                                    cabecalho("Deletar funcionarios")
                                    r = menu([
                                        "Digitar qual funcionario deseja deletar",
                                        "voltar"
                                    ])
                                    if r == 2:
                                        break
                                    # 1.1.2.1 - TELA DIGITAR FUNCIONÁRIO PARA DELETAR -------------------------OK
                                    if r == 1:
                                        for c, f in enumerate(lista_usuarios):
                                            print(f"{c + 1}\t -\t{f}\t")

                                        numero = int(
                                            input(
                                                "Digite o numero do funcionáro para deletar:\n"))
                                        deletarFuncionario(
                                            numero, lista_usuarios
                                        )  # removendo funcionário:
                                        atualizarLista(user)
                                        print("Funcionário deletado com sucesso.")

                    # 1.2 - TELA - VER ORDENS DE SERVIÇO ----------------------------------------OK
                    elif r == 2:
                        while True:
                            cabecalho("Ordens de serviços")
                            r = menu([
                                "visualizar", "marca como concluida",
                                "Deletar", "voltar"
                            ])

                            #  VOLTAR A TELA "BEM VINDO ADMIN"
                            if r == 4:  # -> voltar para 'TELA DO ADMIN'(1)
                                break

                            # 1.2.1 - VISUALIZAR SERVIÇOS ------------------------------------------OK
                            elif r == 1:
                                cabecalho("Visualizar")
                                teste = len(ordens)
                                if teste != 0:
                                    for n, c in enumerate(ordens):
                                        print(
                                            f" {n + 1} \t -\t CPF DO CLIENTE: {c[0]} \t -\t CPF DO MECÂNICO: {c[1]} \t -\t VALOR(R$): {c[2]} \t -\t SERVIÇO: {c[3]} \n"
                                        )
                                else:
                                    print("Não há ordens de serviço ainda..")

                            # 1.2.2 - MARCAR CONCLUIDAS ---------------------------------------------OK
                            elif r == 2:
                                cabecalho("Marcar Concluídas")
                                teste = len(ordens)
                                # mostrando todas as ordens como um menu:
                                if teste != 0:
                                    for n, c in enumerate(ordens):
                                        print(
                                            f" {n + 1} \t -\t CPF DO CLIENTE: {c[0]} \t -\t CPF DO MECÂNICO: {c[1]} \t -\t VALOR(R$): {c[2]} \t -\t SERVIÇO: {c[3]} \n"
                                        )

                                    posicao = int(
                                        input(
                                            "digite a posição da ordem para marcar-la como concluída:\n"
                                        ))
                                    if posicao == 0 or posicao > teste:
                                        print("Digite uma posição válida.")
                                    else:
                                        status = [
                                        ]  # criando uma lista com informação de status respectiva aos itens da lista de ordens.
                                        for item in ordens:
                                            status.append(
                                                "pendente"
                                            )  # 1º toda a lista vai receber um "pendente" na quantidade de itend em ordens.
                                            # print(status)

                                        status.pop(
                                            posicao - 1
                                        )  # removendo o status do elemento pela posição exata do indice
                                        status.insert(
                                            posicao - 1, "finalizada"
                                        )  # adicionando o status "finalizada" na posição que tinha sido removida
                                        # print(status)
                                        item = ordens[posicao - 1]
                                        print(
                                            f":::::CONCLUÍDA::::: {posicao} \t -\t CPF DO CLIENTE: {item[0]} \t -\t CPF DO MECÂNICO: {item[1]} \t -\t VALOR(R$): {item[2]} \t -\t SERVIÇO: {item[3]}\n"
                                        )
                                        escreverOrdemConcluida(item)
                                        atualizarOrdens()
                                else:
                                    print("Não há ordens de serviço ainda..")

                            # 1.2.3 - DELETAR -------------------------------------------------------
                            elif r == 3:
                                cabecalho("Deletar Ordem")
                                teste = len(ordens)
                                if teste != 0:
                                    for n, c in enumerate(ordens):
                                        print(
                                            f" {n + 1} \t -\t CPF DO CLIENTE: {c[0]} \t -\t CPF DO MECÂNICO: {c[1]} \t -\t VALOR(R$): {c[2]} \t -\t SERVIÇO: {c[3]} \n"
                                        )
                                    numero = int(
                                        input(
                                            "Digite o numero da ordem para deletar:\n"
                                        ))
                                    if numero == 0 or numero > teste:
                                        print("Digite uma posição valida.")
                                        break
                                    deletarOrdem(numero,
                                                 ordens)  # removendo ordem
                                    atualizarOrdens()
                                else:
                                    print("Não há ordens de serviço ainda..")

                    # 1.3 - VIZUALIZAR CLIENTES ---------------------------------------------
                    elif r == 3:
                        while True:
                            teste = len(clientes)
                            if teste > 0:
                                cabecalho("Lista de clientes")
                                for n, c in enumerate(clientes):
                                    print(
                                        f" {n + 1} \t -\t NOME: {c[0]} \t -\t CPF: {c[1]} \t -\t EMAIL: {c[2]} \t -\t TELEFONE: {c[3]} \t -\t ENDEREÇO: {c[4]} \t -\t PLACA: {c[5]}\n"
                                    )
                                break

                            else:
                                print("Não há clientes cadastrados ainda...")
                                break
                        # 1.4 - TELA DELETAR CLIENTE -------------------------------------------
                    elif r == 4:
                        while True:
                            teste = len(clientes)
                            if teste != 0:
                                cabecalho("Deletar clientes")
                                for n, c in enumerate(clientes):
                                    print(
                                        f" {n + 1} \t -\t NOME: {c[0]} \t -\t CPF: {c[1]} \t -\t EMAIL: {c[2]} \t -\t TELEFONE: {c[3]} \t -\t ENDEREÇO: {c[4]} \t -\t PLACA: {c[5]}\n"
                                    )
                                r = menu([
                                    "Digitar qual cliente deseja deletar",
                                    "voltar.\n"
                                ])

                                if r == 1:
                                    numero = int(
                                        input(
                                            "Digite o numero do funcionáro para deletar:\n"
                                        ))
                                    if numero == 0 or numero > teste:
                                        print("Digite uma posição valida.")
                                        break
                                    deletarCliente(
                                        numero, clientes)  # removendo cliente:
                                    atualizarClientes()
                                    print("Cliente deletado com sucesso!")
                                if r == 2:
                                    break
                            else:
                                print("Não há clientes cadastrados ainda...")
                                break

                # LOGIN DO RECEPCIONISTA
                elif i[2] == '2':
                    # 2 - TELA DO RECEPCIONISTA -------------------------------------------OK
                    cabecalho(f"Seja bem vindo(a) {i[0]}")
                    r = menu([
                        "Cadastrar clientes",
                        "Ver orçamentos (Transformar em ordem de serviço e deletar",
                        "visualizar clientes", "editar cliente", "voltar para tela inicial"
                    ])

                    # VOLTAR PARA LOGIN NO SISTEMA
                    if r == 5:
                        cabecalho("Login Do Sistema")
                        break

                    # 2.1 - TELA CADASTRAR CLIENTE ----------------------------------------OK
                    elif r == 1:
                        while True:
                            r = menu([
                                "Cadastrar clientes",
                                "voltar para tela do recepcionista"
                            ])
                            if r == 1:
                                Cliente = []
                                Cliente.append(str(input("nome do cliente: ")))
                                if Cliente[0] == "0":
                                  break
                                Cliente.append(str(input("cpf do cliente: ")))
                                Cliente.append(input("email do cliente: "))
                                Cliente.append(
                                    str(input("telefone do cliente: ")))
                                Cliente.append(
                                    str(input("Endereço do cliente: ")))
                                Cliente.append(
                                    str(input("digite a placa do carro: ")))
                                clientes.append(Cliente)
                                escreverNovoCliente(Cliente)
                                atualizarClientes()
                                print(
                                    "\033[1;92mCliente cadastrado com sucesso!!\033[m"
                                )

                            if r == 2:
                                break

                    # 2.2 - TELA VER ORÇAMENTO ---------------------------------------------OK
                    elif r == 2:
                        while True:
                            cabecalho("Ordem de serviços")
                            teste = len(orcamentos)
                            if teste != 0:
                                for n, c in enumerate(orcamentos):
                                    print(
                                        f" {n + 1} \t -\t CPF DO CLIENTE: {c[0]} \t -\t CPF DO MECÂNICO: {c[1]} \t -\t VALOR(R$): {c[2]} \t -\t SERVIÇO: {c[3]} \n"
                                    )

                                # voltar
                                q = menu([
                                    "Transformar em ordem de serviço", "voltar"
                                ])
                                if q == 2:
                                    break
                                # Transformando em ordem de serviço
                                elif q == 1:
                                    num = input(
                                        "Digite a posição do orçamento para transforma-lo em ordem de serviço:\n"
                                    )
                                    num = int(num)
                                    item = orcamentos[num - 1]
                                    print(
                                        f"Orçamento {num} do cliente {item[0]} foi alterado para Ordem de Serviço"
                                    )
                                    escreverNovaOrdem(item)
                                    atualizarOrdens()
                                    deletarOrcamento(num - 1, orcamentos)
                                    atualizarOrcamentos()
                                    break
                                else:
                                    break
                            else:
                                print(
                                    "Não há orçamentos cadastrados ainda. Aguarde até que o mecânico introduza"
                                )
                                break

                    # 2.3 - TELA VISUALIZAR CLIENTES ---------------------------------------OK

                    elif r == 3:
                        while True:
                            teste = len(clientes)
                            if teste != 0:
                                cabecalho("Lista de clientes")
                                atualizarClientes()
                                for n, item in enumerate(clientes):
                                    print(f" {n + 1} \t -\t NOME: {item[0]} \t -\t CPF: {item[1]} \t -\t EMAIL: {item[2]} \t -\t TELEFONE: {item[3]} \t -\t ENDEREÇO: {item[4]} \t -\t PLACA: {item[5]}")
                                q = menu(["voltar"])
                                if q == 1:
                                    break
                            else:
                                print("Não há clientes cadastrados ainda...")
                                break

                    # 2.4 - TELA EDITAR CLIENTES ---------------------------------------OK

                    elif r == 4:
                        while True:
                            teste = len(clientes)
                            if teste != 0:
                                cabecalho("editar clientes")
                                m = menu([
                                    "Escolher cliente",
                                    "voltar"])
                                if m == 2:
                                    break
                                elif m == 1:
                                    # mostrar lista de clientes:
                                    for c, f in enumerate(clientes):
                                        print(f"{c + 1}\t -\t{f}\t")

                                    num = int(input("Digite a posição do cliente para editá-lo.\n"))
                                    editarClientes(num, clientes)
                                    atualizarClientes()

                            else:
                                print("Não há clientes registrados ainda.")
                                break

                # LOGIN DO MECÂNICO
                elif i[2] == "3":
                    # 3 - TELA DO MECÂNICO -------------------------------------------OK
                    cabecalho(f"seja bem vindo {i[0]}")
                    r = menu([
                        "Cadastrar orçamento (cadastrar)",
                        "Ver ordens de serviço (apenas as que possuem o cpf dele)",
                        "voltar para tela inicial"
                    ])
                    # VOLTAR
                    if r == 3:
                        cabecalho("Login Do Sistema")
                        break

                    # 3.1 - TELA CADASTRAR ORÇAMENTO -----------------------------------OK
                    elif r == 1:
                        while True:
                            teste = len(clientes)
                            if teste != 0:
                                cabecalho("cadastrar orçamento")
                                # Vai mostrar os clientes para que possa fazer o orçamento pegando o cpf o cliente
                                atualizarClientes()
                                for n, item in enumerate(clientes):
                                    print(
                                        f" {n + 1} \t -\t NOME: {item[0]} \t -\t CPF: {item[1]} \t -\t EMAIL: {item[2]} \t -\t TELEFONE: {item[3]} \t -\t ENDEREÇO: {item[4]} \t -\t PLACA: {item[5]}\n")

                                l = menu([
                                    "coninuar para cadastar orçamento",
                                    "voltar"
                                ])
                                # VOLTAR
                                if l == 2:
                                    break

                                if l == 1:
                                    Orcamento = []
                                    Orcamento.append(
                                        input("Digite o CPF do cliente:\n"))
                                    Orcamento.append(
                                        input("Digite o CPF do Mecânico:\n"))
                                    Orcamento.append(
                                        input("Digite o valor do serviço:\n"))
                                    Orcamento.append(
                                        input("Digite o Serviço:\n"))
                                    orcamentos.append(Orcamento)
                                    escreverNovoOrcamento(Orcamento)
                                    atualizarOrcamentos()
                                    print(
                                        "\033[1;92mCliente cadastrado com sucesso!!\033[m"
                                    )
                                    break
                            else:
                                print("Não há clientes cadastrados ainda...")
                                break

                    # 3.2 - TELA - VER ORDENS DE SERVIÇO ------------------------------------OK
                    if r == 2:

                        cabecalho("ordens de serviços no seu CPF:")
                        if login == "MEC":  # se for usuario MEC padrão não vai haver cpf agregado a ele.
                            print("Não há CPF agregado a este perfil.")
                        else:  # criando uma nova lista para manipula-lá sem afetar a principal
                            lista_usuarios2 = []
                            for item in lista_usuarios:
                                lista_usuarios2.append(item)
                            del lista_usuarios2[0:3]  # removendo os primeiros 3 indices
                            for c in lista_usuarios2:
                                if login == c[0] and senha == c[1]:  # confirmar por nome e seha que é ele mesmo
                                    cpf = c[3]  # OK
                                    for j in ordens:
                                        if j[1] == cpf:  # se o cpf na ordem de servico for igual ao cpf do mêcanico
                                            print(j)  # print a ordem de serviço em j
                                            lista_usuarios2[:] = []
                                            