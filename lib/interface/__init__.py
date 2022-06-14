# funções e modelos

def linha(tam=50):
    return '-' * tam



def cabecalho(msg):
    print(linha())
    print(f'\033[1;93m{msg.center(50)}\033[m'
          )  # alinha a mensagem no meio de 42 caracteres
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
    arquivo = open('save.txt', 'a', encoding="utf8")
    arquivo.writelines(func)
    arquivo.close()



def deletarFuncionario(numero, lista_usuarios):
    limite = len(lista_usuarios)
    if numero >= limite + 1:
        print("Não existe essa opção.")
    elif numero == 1 or numero == 2 or numero == 3:
        print('\033[1;31mERRO! Este usuário não pode ser removido.\033[m')
    else:
        lista_usuarios.pop(numero - 1)
        del lista_usuarios[0:3]
        print(lista_usuarios)
        with open('save.txt', 'w', encoding="utf8") as arquivo:
            for item in lista_usuarios:
                func = item[0] + ", " + item[1] + ", " + item[2] + ", " + item[3] + "\n"
                arquivo.write(func)
        #atualizarLista(user)



def escreverNovoCliente(lista_Cliente):
    func = lista_Cliente[0] + ", " + lista_Cliente[1] + ", " + lista_Cliente[2] + ", " + lista_Cliente[3] + ", " + lista_Cliente[4] + ", " + lista_Cliente[5] + "\n"
    arquivo = open('clientes.txt', 'a', encoding="utf8")
    arquivo.writelines(func)
    arquivo.close()



def deletarCliente(numero, lista_clientes):
    limite = len(lista_clientes)
    if numero >= limite + 1:
        print("Não existe essa opção.")
    else:
        lista_clientes.pop(numero - 1)
        print(lista_clientes)
        with open('clientes.txt', 'w', encoding="utf8") as arquivo:
            for item in lista_clientes:
                func = item[0] + ", " + item[1] + ", " + item[2] + ", " + item[3] + ", " + item[4] + ", " + item[5] + "\n"
                arquivo.write(func)
        #atualizarClientes()



def escreverNovaOrdem(lista_Ordem):
    func = lista_Ordem[0] + ", " + lista_Ordem[1] + ", " + lista_Ordem[2] + ", " + lista_Ordem[3] + "\n"
    arquivo = open('ordens.txt', 'a', encoding="utf8")
    arquivo.writelines(func)
    arquivo.close()



def deletarOrdem(numero, lista_ordens):
    limite = len(lista_ordens)
    if numero >= limite + 1:
        print("Não existe essa opção.")
    else:
        lista_ordens.pop(numero - 1)
        print(lista_ordens)
        with open('ordens.txt', 'w', encoding="utf8") as arquivo:
            for item in lista_ordens:
                func = lista_ordens[0] + ", " + lista_ordens[1] + ", " + lista_ordens[2] + ", " + lista_ordens[3] + "\n"
                arquivo.write(func)