import random as rd
#declaracao de variaveis
varcredito=[]
i=0
contador=0
operacoes=[]
nconta=0
contagem=0
saldoinit=0
saldoemconta=saldoinit
#funcoes
#mudar limite
def mudarlimite(varcredito,saldo):
    global limite
    limite=(0.75*saldo)-sum(varcredito)

#verificar senha
def verificar(senha):
    verificar=0
    global contagem
    contagem=0
    sim=0
    while (sim==0):
        verificar=input("INFORME A SENHA:")
        if(verificar==senha):
            sim=sim+1
        else:
            contagem=contagem+1
        if(contagem==3):
            print("PERDEU O SEU ACESSO,MUITAS TENTATIVAS")
            exit()
#verificar conta
def conta(nconta):
    contaver=0
    sim=0
    while (sim==0):
        contaver=int(input("INFORME O NÚMERO DA CONTA:"))
        if(contaver==nconta):
            sim=sim+1
#variacao do saldo
def saldo(saldoinit,movimento,operacoes):
    i=0
    global saldoemconta
    saldoemconta=saldoinit
    if (len(operacoes)==0):
        saldoemconta=saldoinit+movimento
    else:
        while (i<len(operacoes)):
            saldoemconta=saldoemconta+operacoes[i]
            i=i+1
#verificar email
def emailver(email):
    emailverificar=0
    sim=0
    while (sim==0):
        emailverificar=(input("INFORME SEU EMAIL:"))
        if(emailverificar==email):
            sim=sim+1
        else:
            print("O EMAIL INFORMADO ESTÁ INCORRETO")





#inicio do loop
while True:
    print("MACK BANK – ESCOLHA UMA OPÇÃO\n  (1) CADASTRAR CONTA CORRENTE",
         "\n  (2) DEPOSITAR\n  (3) SACAR\n  (4) CONSULTAR SALDO\n  (5) CONSULTAR EXTRATO",
          " \n  (6) FINALIZAR\n  (7) TROCAR SENHA\n  (8) ALTERAR LIMITE")
    opcao=int(input("SUA OPÇÃO:"))
    if(opcao==1):
#cadastro da conta
        if(contador==0):
            print("MACK BANK – CADASTRO DE CONTA")
            nconta=rd.randint(1000,9999)
            print("NÚMERO DA CONTA:",nconta)
            nome=input("NOME DO CLIENTE:")
            while (len(nome)==0):
                print("NOME INVÁLIDO")
                nome=input("NOME DO CLIENTE:")
            telefone=input("TELEFONE.......:")
            while (len(telefone)==0):
                print("NÚMERO INVÁLIDO")
                telefone=input("TELEFONE.......:")
            email=input("EMAIL..........:")
            while (len(email)==0):
                print("EMAIL INVÁLIDO")
                email=input("EMAIL..........:")
            saldoinit=float(input("SALDO INICIAL...: R$"))
            while (saldoinit<1000):
                saldoinit=float(input("DIGITE UM VALOR MAIOR QUE 1000"))
            #agora funciona se verificar o saldo sem um deposito ou saque
            saldo(saldoinit,0,operacoes)
            mudarlimite(varcredito,saldoemconta)
            senha=input("SENHA............:")
            while (len(senha)!=6):
                print("SENHA INVÁLIDA")
                senha=input("SENHA DEVE CONTER 6 CARACTERES:")
            verificars=input("REPITA A SENHA...:")
            while (contador==0):
                if (verificars==senha):
                    print("CADASTRO REALIZADO!")
                    contador=1
                else:
                    print("SENHA INCORRETA,TENTE NOVAMENTE")
                    verificars=input("REPITA A SENHA...:")
        else:
             print("VOCÊ JÁ TEM CADASTRO")
    if(opcao==2):
#deposito
        if(contador==0):
            print("PRIMEIRO CRIE SUA CONTA")
        else:
            print("MACK BANK – DEPÓSITO EM CONTA")
            conta(nconta)
            print("NOME DO CLIENTE:",nome)
            depósito=float(input("VALOR DO DEPÓSITO: R$"))
            if(depósito>0):
                saldo(saldoinit,depósito,operacoes)
                operacoes.append(depósito)
                print("DEPÓSITO REALIZADO COM SUCESSO!")
            else:
                print("VALOR INVÄLIDO")
    if(opcao==3):
#saque
#se usuario nao tiver conta ou ter passado do limite de erros limita o acesso
        if(contador==0):
            print("PRIMEIRO CRIE SUA CONTA")
        else:
            if(contagem==3):
                print("NÃO TEM ACESSO À ESSE RECURSO")
            else:
                print("MACK BANK – SAQUE DA CONTA")
                conta(nconta)
                print("NOME DO CLIENTE:",nome)
                verificar(senha)
                if(contagem==3):
                    print("NÃO TEM ACESSO À ESSE RECURSO")
                    continue
                saque=float(input("VALOR DO SAQUE: R$"))
                if (saque>0):
                    if (saque>saldoemconta):
                        if(saque>saldoemconta+limite):
                            print("NÃO PODE SACAR COM O SEU SALDO ATUAL")
                            continue
                        else:
                            print("VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO")
                            operacoes.append(-saque)
                            saldo(saldoinit,-saque,operacoes)
                            varcredito.append(saque-saldoemconta)
                    else:
                        operacoes.append(-saque)
                        saldo(saldoinit,-saque,operacoes)
                else:
                    print("NÚMERO INVÁLIDO")
                    continue
                print("SAQUE REALIZADO COM SUCESSO!")

    if(opcao==4):
#consulta de saldo
#se usuario nao tiver conta ou ter passado do limite de erros limita o acesso
        if(contador==0):
            print("PRIMEIRO CRIE SUA CONTA")
        else:
            if(contagem==3):
                print("NÃO TEM ACESSO À ESSE RECURSO")
            else:
                print("MACK BANK – CONSULTA SALDO")
                conta(nconta)
                print("NOME DO CLIENTE:",nome)
                verificar(senha)
                if(contagem==3):
                    print("NÃO TEM ACESSO À ESSE RECURSO")
                    continue
                print("SALDO EM CONTA: R$",saldoemconta)
                print("LIMITE DE CRÉDITO: R$",limite)
    if(opcao==5):
#consulta de extrato
#se usuario nao tiver conta ou ter passado do limite de erros limita o acesso
        if(contador==0):
            print("PRIMEIRO CRIE SUA CONTA")
        else:
            if(contagem==3):
                print("NÃO TEM ACESSO À ESSE RECURSO")
            else:
                print("MACK BANK – EXTRATO DA CONTA")
                conta(nconta)
                print("NOME DO CLIENTE:",nome)
                verificar(senha)
                if(contagem==3):
                    print("NÃO TEM ACESSO À ESSE RECURSO")
                    continue
                print("LIMITE DE CRÉDITO: R$",limite)
                print("ÚLTIMAS OPERAÇÕES:")
                while(i<len(operacoes)):
                    if(operacoes[i]>0):
                        print("DEPÓSITO: R$",operacoes[i])
                    if(operacoes[i]<0):
                        #remover o sinal do print
                        repl=str(operacoes[i])
                        repl=repl.replace("-","")
                        print("SAQUE: R$",repl)
                    i=i+1
                print("SALDO EM CONTA: R$",saldoemconta)
                if(saldoemconta<0):
                    print("Atenção ao seu saldo!")
    if(opcao==6):
        print("MACK BANK – SOBRE\nEste programa foi desenvolvido por",
              "\nGustavo")
        break
#fim do loop
    if(opcao==7):
        if(contador==0):
            print("PRIMEIRO CRIE SUA CONTA")
        else:
            if(contagem==3):
                print("NÃO TEM ACESSO À ESSE RECURSO")
                continue
            else:
                print("MACK BANK – TROCA DE SENHA")
                conta(nconta)
                emailver(email)
                senhanova=input("DIGITE SUA NOVA SENHA:")
                while(len(senhanova)!=6):
                    print("A SENHA DEVE CONTER 6 CARACTERES")
                    senhanova=input("DIGITE SUA NOVA SENHA:")
                verificars=input("DIGITE NOVAMENTE:")
                if(verificars==senhanova):
                    print("SUA SENHA FOI MODIFICADA COM SUCESSO")
                    senha=senhanova
                else:
                    while(verificars!=senhanova):
                        print("A VERIFICAÇÃO ESTÁ INCORRETA")
                        verificars=input("DIGITE NOVAMENTE:")
                        if(verificars==senhanova):
                            print("SUA SENHA FOI MODIFICADA COM SUCESSO")
                            senha=senhanova
#troca de senha
    if(opcao==8):
        if(contador==0):
            print("PRIMEIRO CRIE SUA CONTA")
        else:
            print("MACK BANK – ALTERAÇÃO DE LIMITE")
            conta(nconta)
            verificar(senha)
            if(contagem==3):
                print("NÃO TEM ACESSO À ESSE RECURSO")
                continue
            antigolimite=limite
            mudarlimite(varcredito,saldoemconta)
            if(limite<0):
                print("VOCÊ NÃO PODE ALTERAR O LIMITE")
                limite=antigolimite
            else:
                print("LIMITE ALTERADO COM SUCESSO")
#alterar limite



