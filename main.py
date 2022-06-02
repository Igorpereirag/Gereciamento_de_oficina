from lib.interface import*
cabeçalho("login do sistema")
#joao, 93407073003, 123, 1

l1=["ADMIN","RECEP","MEC"]
l2=[123456,123,456]
login=""
senha=""
r=""
while True:
  login=str(input("\033[1;36mDIGITE SEU USENAME:\033[m").strip().upper())
  senha=leiaInt("\033[1;36mDIGITE SUA SENHA:\033[m")
  if login==l1[0] and senha==l2[0] or login==l1[1] and senha==l2[1] or login==l1[2] and senha==l2[2]:
    break
  else:
    print("Login ou Senha incorretas tente novamente")

if login==l1[0] and senha==l2[0]:
    print(f"seja bem vindo {l1[0]} seu cargo é de gerente")
    r=menu(["Gerenciar funcionários (cadastrar e deletar)","Ver ordens de serviço (Visualizar, Marcar como concluída e deleta)"])
if r == 1:
      cabeçalho("Gestao dos funcionarios:")
      menu(["cadastrar funcionário","deletar funcionário"])
      nome=str(input('digite o nome:'))
      cpf=int(input('digite o cpf do funcionario:'))
      senha=int(input('digite a senha:'))
      cargo=str(input('digite o cargo:'))                

        
elif r == 2: 
      cabeçalho("ver ordem de serviço:")
      r=menu(["visualizar","marcar como concluída","deletar"])
    
              
elif login==l1[1] and senha==l2[1]:
    print(f"seja bem vinda {l1[1]} seu cargo recepcionista ")
    #while True:
    print("""
    [1]-Cadastrar clientes (cadastrar)
    [2]-Ver orçamentos (Transformar em ordem de serviço e deletar)""")
    #aqui entra as varieaveis de contrele
    r=int(input("Sua opção"))
    if r==1:
      nome=str(input("nome do cliente"))
      cpf=int(input("cpf do cliente"))
      email=str(input("email do cliente"))
      telefone=int(input("telefone do cliente"))
      endereço=str(input("Endereço DO CLEINTE"))
      placadocarro=int(input("digite a placa do carro")) 
    

elif login==l1[2] and senha==l2[2]:
    print(f"seja bem vindo {l1[2]} seu cargo é de mecanico")
    # while True:
    print('''
    [1]-Cadastrar orçamento (cadastrar)
    [2]-Ver ordens de serviço (apenas as que possuem o cpf dele)    
        ''')
   
    # aqui entra as varieaveis de contrele




