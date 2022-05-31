print("-----------------sistema de controle oficina------------------------")

funcinarios = {}
print("*********************MENU PRINCIPAL*******************************")
#save.txt
#joao, 93407073003, 123, 1
#VARIAVEIS DE CONTROLE
l1=["ADMIN","RECEP","MEC"]
l2=[123456,123,456]
listacpf=[]
clientes=[ ]
login=str(input("DIGITE SEU USENAME:").strip().upper())
senha=int(input("DIGITE SUA SENHA:"))

if login==l1[0] and senha==l2[0]:
    print(f"seja bem vindo {l1[0]} seu cargo é de gerente")
    #while True:
    print("""
     [1]-Gerenciar funcionários (cadastrar e deletar)
     [2]-Ver ordens de serviço (Visualizar, Marcar como concluída e deletar)
     [3]-Ver clientes (Visualizar e deletar)""")
    #aqui entra as varieaveis de contrele


elif login==l1[1] and senha==l2[1]:
    print(f"seja bem vinda {l1[1]} seu cargo recepcionista ")
    #while True:
    print("""
    [1]-Cadastrar clientes (cadastrar)
    [2]-Ver orçamentos (Transformar em ordem de serviço e deletar)""")
    #aqui entra as varieaveis de contrele

elif login==l1[2] and senha==l2[2]:
    print(f"seja bem vindo {l1[2]} seu cargo é de mecanico")
    # while True:
    # aqui entra as varieaveis de contrele


