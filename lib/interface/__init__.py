#funções e modelos
def linha(tam=50):
    return '-' * tam


def cabeçalho(msg):
    print(linha())
    print(f'\033[1;93m{msg.center(50)}\033[m'
          )  # alinha a mensagem no meio de 42 caracteres
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[1;36m[ {cont} ]\033[m - \033[1;93m{item}\033[m')
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
    opção = n
    return opção


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


def validasexo():
    while True:
        try:
            sexo = str(input('Sexo: [M/F] ')).strip().upper()
            while sexo == '':
                print('\033[1;31mERRO! Digite um sexo válido [M ou F].\033[m')
                sexo = str(input('Sexo: [M/F] ')).strip().upper()
            sexo = sexo[0]
            while sexo.isnumeric():
                print('\033[1;31mERRO! Digite um sexo válido [M ou F].\033[m')
                sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
            while sexo not in 'MF':
                print('\033[1;31mERRO! Digite um sexo válido [M ou F].\033[m')
                sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        except (ValueError, TypeError):
            print('\033[1;31mERRO! Digite uma opção válida.\033[m')
        except KeyboardInterrupt:
            print(
                '\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
        else:
            break
    return sexo


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
  valor=0
  while True:
    n=str(input(msg))
    if n.isnumeric():
      valor=int(n)
      o = True
    else:
      print("\033[0;31mDigite um numero inteiro valido\033[m")
      if o:
        break
  return valor

  
def lerArquivo():
    lista = []
    arquivo = open('save.txt', 'r', encoding="utf8")
    for line in arquivo:
        lista.append(line)

    arquivo.close()
    for i in lista:
        print(i)


def escreverArquivo():
    arquivo = open('save.txt', 'r', encoding="utf8")
    conteudo = arquivo.readlines()
    conteudo.append("\nNova linha")
    arquivo = open('save.txt', 'w', encoding="utf8")
    arquivo.writelines(conteudo)
    arquivo.close()


    
