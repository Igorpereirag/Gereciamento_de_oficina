from lib.interface import*
cabeçalho("login do sistema")
#joao, 93407073003, 123, 1

l1=["ADMIN","RECEP","MEC"]
l2=[123456,123,456]
login=""
senha=""
r=""

while True:
  login=str(input("\033[1;92mDIGITE SEU USENAME:\033[m").strip().upper())
  senha=leiaInt("\033[1;92mDIGITE SUA SENHA:\033[m")
  if login==l1[0] and senha==l2[0] or login==l1[1] and senha==l2[1] or login==l1[2] and senha==l2[2]:
    while True:
      if login==l1[0] and senha==l2[0]:
        cabeçalho(f"SEJA BEM VINDO {l1[0]}")
        r=menu(["Gerenciar funcionários (cadastrar e deletar)","Ver ordens de serviço(Visualizar, Marcar como concluída e deleta)","visualiza clientes","voltar para tela incial"])
        if r==4:
          cabeçalho("Login Do Sistema")
          break
        while True:
          if r == 1:
            cabeçalho("Gestao dos funcionarios:")
            r=menu(["cadastrar funcionário","deletar funcionário","Voltar"])
            if r==1:
              while True:
                r=1
                l1.append(str(input('digite o nome:')))
                cpf=int(input('digite o cpf do funcionario:'))
                l2.append(int(input('digite a senha:')))
                cargo=str(input('digite o cargo:'))
                print("\033[1;92mUsuario cadastrado com sucesso\033[m")
                if r==1:
                  break 
            if r == 2: 
              cabeçalho("Deletar funcionarios")
              for c,f in enumerate(l1):
               print(f"{c + 1}\t -\t{f}\t")
              r=menu(["Digite qual funcionario deseja deletar"])
               
            elif r==3:         
                break        
      elif login==l1[1] and senha==l2[1]:
        print(f"seja bem vinda {l1[1]} seu cargo recepcionista ")
        while True:
          r=menu(["Cadastrar clientes (cadastrar)","Ver orçamentos (Transformar em ordem de serviço e deletar"])
          if r==1:
            nome=str(input("nome do cliente"))
            cpf=int(input("cpf do cliente"))
            email=str(input("email do cliente"))
            telefone=int(input("telefone do cliente"))
            endereço=str(input("Endereço DO CLEINTE"))
            placadocarro=int(input("digite a placa do carro")) 
























        
               
        
  else:
    print("\033[1;31mLogin ou Senha incorretos! Tente novamente.\033[m")

    
              









  