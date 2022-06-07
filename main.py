from lib.interface import*
cabeçalho("login do sistema")
user=[["ADMIN","12345","1"],["RECEP","123","2"],["MEC","456","3"]]
clientes=[]
while True:
  login = str(input("\033[1;92mDIGITE SEU USENAME:\033[m").strip().upper())
  senha = str(input("\033[1;92mDIGITE SUA SENHA:\033[m").strip().upper())
  for i in user:
    if login == i[0] and senha == i[1]:
      while True:
        if i[2] == '1':
          cabeçalho(f"SEJA BEM VINDO {i[0]}")
          r=menu(["Gerenciar funcionários","Ver ordens de serviço","visualiza clientes","voltar para tela incial"])
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
                  funcionario = []
                  funcionario.append(str(input("digite seu username")))
                  funcionario.append(str(input("digite sua senha")))
                  funcionario.append(str(input("digite seu cargo")))
                  user.append(funcionario)
                  cpf=int(input('digite o cpf do funcionario:'))
                  user.append(funcionario)
                  print("\033[1;92mUsuario cadastrado com sucesso\033[m")
                  if r==1:
                    break 
              if r == 2: 
                cabeçalho("Deletar funcionarios")
                for c,f in enumerate(user):
                  print(f"{c + 1}\t -\t{f}\t")
                r=menu(["Digite qual funcionario deseja deletar","voltar"])
                if r==2:
                  break
              if r==3:
                break
                
            if r==2:
              cabeçalho(" Ordens de serviços")
              r=menu(["visualizar","marca como concluida","Deletar","voltar"])
              if r==1:
                pass
              if r==2:
                pass
            
              if r==3:
                  pass
            
              if r==4:
                  break
            if r==3:
              cabeçalho("Lista de clientes")
              print(f"{clientes}")
              r=menu(["voltar"])
              if r==1:
                break
        if i[2] == '2':
          cabeçalho(f"Seja bem vindo(a) {i[0]}")
          r=menu(["Cadastrar clientes","Ver orçamentos (Transformar em ordem de serviço e deletar","visualiza clientes", "voltar para tela inicial"])
          if r==4:
            cabeçalho("Login Do Sistema")
            break
          if r ==1:  
            while True:
              if r==1:
                cliente=[]
                cliente.append(str(input("nome do cliente")))
                cliente.append(int(input("cpf do cliente")))
                cliente.append(input("email do cliente"))
                cliente.append(int(input("telefone do cliente")))
                cliente.append(str(input("Endereço DO CLEINTE")))
                cliente.append(str(input("digite a placa do carro")))
                clientes.append(cliente)
                print("\033[1;92mCliente cadastrado com sucesso!!\033[m")
                if r==1:
                  break
          if r==2:
            while True:
              cabeçalho("Ordem de serviços")
              r=menu(["voltar"])
              if r==1:
                break
          if r==3:
            while True:
              cabeçalho("Lista de clientes")
              print(f"{clientes}")
              r=menu(["voltar"])
              if r==1:
                break
          if r==4:
            break
                  
        elif i[2]== "3":
          cabeçalho(f"seja bem vindo {i[0]}")
          r=menu(["Cadastrar orçamento (cadastrar)","Ver ordens de serviço (apenas as que possuem o cpf dele)", "voltar para tela inicial"])
          if r==3:
            cabeçalho("LOGIN DO SISTEMA")
            break
          if r==1:
            while True:
              cabeçalho("cadastrar orçamento")
              r=menu(["voltar"])
              if r==1:
                break
          
          if r==2:
            while True:
              cabeçalho("ordens de serviços")
              r=menu(["voltar"])
              if r==1:
                break
          











    
        else:
          print("\033[1;31mLogin ou Senha incorretos! Tente novamente.\033[m")
      















    
              









  