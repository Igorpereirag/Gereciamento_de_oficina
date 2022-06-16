# funções e modelos

def linha(tam=50):
    return '-' * tam

def cabecalho(msg):
    print(linha())
    print(f'\033[1;93m{msg.center(50)}\033[m')  # alinha a mensagem no meio de 42 caracteres
    print(linha())

def menu(lista):
    cont = 1
    for item in lista:
        print(f'\033[1;92m[ {cont} ]\033[m - \033[1;93m{item}\033[m')
        cont += 1
    print(linha())
    while True:
        try:
            n = int(input('\033[1;37mSelecionar Opção:\033[m '))
            n = abs(n)
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite uma opção válida.\033[m')
        except KeyboardInterrupt:
            print(
                '\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            break
    opcao = n
    return opcao

def validanome():
    while True:
        try:
            nome = str(input('Nome: ')).strip()
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite uma opção válida.\033[m')
        except KeyboardInterrupt:
            print(
                '\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            break
    return nome

def validaidade():
    while True:
        try:
            idade = int(input('Idade: '))
            idade = abs(idade)
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite uma opção válida.\033[m')
        except KeyboardInterrupt:
            print(
                '\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            break
    return idade

def leiaInt(msg):
    o = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            o = True
        else:
            print("\033[0;31mDigite um numero inteiro valido\033[m")
        if o:
            break
    return valor

def escreverNovoFuncionario(lista_Funcionario):
    func = lista_Funcionario[0] + ", " + lista_Funcionario[1] + ", " + lista_Funcionario[2] + ", " + lista_Funcionario[3] + "\n"
    arquivo = open('funcionarios.txt', 'a', encoding="utf8")
    arquivo.writelines(func)
    arquivo.close()

def deletarFuncionario(numero, lista_usuarios):
    limite = len(lista_usuarios) #variavel limite vai reeber a quantidade exata de elementos na lista.
    if numero > limite:
        print("Não existe essa opção.")
    elif numero == 0 or numero == 1 or numero == 2 or numero == 3:
        print('\033[1;31mERRO! Usuário não removível.\033[m')
    else:
        lista_usuarios.pop(numero - 1) #removendo o elemento no indice exato
        del lista_usuarios[0:3] #removendo os itens dos indices 0,1,2.
        with open('funcionarios.txt', 'w', encoding="utf8") as arquivo:
            for item in lista_usuarios: #reescrevendo no arquivo .txt usuarios(fora os padrões)
                func = item[0] + ", " + item[1] + ", " + item[2] + ", " + item[3] + "\n"
                arquivo.write(func)
        #atualizarLista(user) lembrar de atualizar a variavel listaUsuarios após chamar essa função

def escreverNovoCliente(lista_Cliente):
    func = lista_Cliente[0] + ", " + lista_Cliente[1] + ", " + lista_Cliente[2] + ", " + lista_Cliente[3] + ", " + lista_Cliente[4] + ", " + lista_Cliente[5] + "\n"
    arquivo = open('clientes.txt', 'a', encoding="utf8")
    arquivo.writelines(func)
    arquivo.close()

def deletarCliente(numero, lista_clientes):
    limite = len(lista_clientes)
    if numero > limite:
        print("Não existe essa opção.")
    else:
        lista_clientes.pop(numero)
        #print(lista_clientes)
        with open('clientes.txt', 'w', encoding="utf8") as arquivo:
            for item in lista_clientes:
                func = item[0] + ", " + item[1] + ", " + item[2] + ", " + item[3] + ", " + item[4] + ", " + item[5] + "\n"
                arquivo.write(func)
        #atualizarClientes()

def escreverNovoOrcamento(lista_Orcamento):
    func = lista_Orcamento[0] + ", " + lista_Orcamento[1] + ", " + lista_Orcamento[2] + ", " + lista_Orcamento[3] + "\n"
    arquivo = open('orcamentos.txt', 'a', encoding="utf8")
    arquivo.writelines(func)
    arquivo.close()

def escreverNovaOrdem(item):
    func = item[0] + ", " + item[1] + ", " + item[2] + ", " + item[3] + "   :::::PENDENTE:::::\n"
    arquivo = open('ordens.txt', 'a', encoding="utf8")
    arquivo.writelines(func)
    arquivo.close()

def deletarOrdem(numero, lista_ordens):
    limite = len(lista_ordens)
    if numero > limite:
        print("Não existe essa opção.")
    else:
        lista_ordens.pop(numero)
        #print(lista_ordens)
        with open('ordens.txt', 'w', encoding="utf8") as arquivo:
            for item in lista_ordens:
                func = item[0] + ", " + item[1] + ", " + item[2] + ", " + item[3] + "\n"
                arquivo.write(func)

def escreverOrdemConcluida(item):
    func = item[0] + ", " + item[1] + ", " + item[2] + ", " + item[3] + "   :::::CONCLUÍDA:::::\n"
    arquivo = open('ordens.txt', 'a', encoding="utf8")
    arquivo.writelines(func)
    arquivo.close()

def deletarOrcamento(numero, lista_orcamentos):
    limite = len(lista_orcamentos)
    if numero > limite:
        print("Não existe essa opção.")
    else:
        lista_orcamentos.pop(numero)
        with open('orcamentos.txt', 'w', encoding="utf8") as arquivo:
            for item in lista_orcamentos:
                func = item[0] + ", " + item[1] + ", " + item[2] + ", " + item[3] + "\n"
                arquivo.write(func)