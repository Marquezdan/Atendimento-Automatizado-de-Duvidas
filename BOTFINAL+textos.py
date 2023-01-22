##################################################################
##            Formação Análise de Dados Senac/Resilia           ##
##            Atendimento Automatizado de Dúvidas               ##
##            Grupo: Confia no Processo                         ##
##   Integrantes: Daniel, Cássio, Joice, Maria Luiza e Cesar    ##
##################################################################

lista0 = ["1 : Duvidas sobre a conta; ","2 : Duvidas sobre o cartão; ", "3 : Duvidas sobre emprestimo; ","4 : Sair" ]
lista1_1 = ["1: Conta corrente;" , "2: Conta poupança;" , "3: Esqueci minha senha; " , "4: Retornar ao menu anterior"]
lista2_1 = ["1: Cancelar cartão;" , "2: Gerar cartão virtual;" , "3: Solicitar de cartão ; " , "4: Retornar ao menu anterior"]
lista3_1 = ["1: Consignado ;" , "2: Emprestimo com garantia ;" , "3: Simulação ; " , "4: Retornar ao menu anterior"]
lista_final = [ "1: Sair;" , "2: retornar ao menu de inicio"]

print ("Seja bem vindo ao Trust Bank.")
##nome = str.title(input("Nos diga seu nome para darmos continuidade ao atendimento: "))

def final (e):
    
    if e == 1:
        return (" ")
        
    elif e == 2:
        return(" ")
    else:
        return ("Opção inválida")

def meio1 (b):
  
    if b == 1:
        return ("Acesse o link a seguir e siga o passo a passo para criar sua conta corrente: www.trustbank.com.br/site/conta-corrente/")
    elif b == 2:
        return ("Acesse o link a seguir e siga o passo a passo para criar sua conta poupança: www.trustbank.com.br/site/conta-poupanca/")
    elif b == 3 :
        return ("Uma mensagem com o passo a passo para recuperar a senha e o código de mudança de senha foi enviado para o seu e-mail.")
    elif b ==4:
        return (" ")
    else:
        return("Opção inválida")

def meio2 (c):
    if c == 1:
        return ("Entre em contato conosco pelo número 0800 070 3636 para cancelar o cartão. ")
    elif c == 2:
        return ("Baixe o nosso aplicativo https://play.google.com/store/apps/trustbank e acessa a sua conta, logo depois, selecione gerar cartão virtual")
    elif c == 3 :
        return ("Seu pedido foi registrado na nossa base de dados, enviaremos um email para comprovar a solicitação")
    elif c ==4:
        return(" ")
    else:
        return("Opção inválida")

def meio3 (d):
    if d == 1:
        return ("O empréstimo consignado é aquele tipo de empréstimo que você solicita e passa a ter o valor das parcelas cobrado direto na folha de pagamento, para mais informações acesse: www.trustbank.com.br/site/emprestimo-consignado/ ")
    elif d == 2:
        return ("O crédito com garantia é uma modalidade de empréstimo na qual o cliente oferece um bem à instituição para, assim, tomar o crédito. Por oferecer um bem como garantia de pagamento do empréstimo, a transação é considerada de menor risco, para mais informações acesse: www.trustbank.com.br/site/emprestimo-com-garantia/")
    elif d == 3 :
        return ("Para fazer uma simulação de emprestimo acesse a opção simulação no aplicativo ou no site: www.trustbank.com.br/site/simular-emprestimo/")
    elif d ==4:
        return (" ")
    else:
        return("Opção inválida")



def start (a):
    if a == 4:
        return (" ")
    elif a >=5:
        return("Opção inválida")
    else:
        return (" ")

opção = 5
opção1 = 5
opção2 = 5
opção3 = 5
opção4 = 3


while opção >=5 or opção1 ==4 or opção2==4 or opção3 == 4 or opção4==2 :
    for l in lista0:
        print(l)    
    print ("*" * 99)

    opção = int(input("Selecione a opção desejada: "))
    print(start(opção))

    if opção ==1:
        opção1 =5
        while opção1>4:
            print ("*" * 99) 
            for a in range(len(lista1_1)):
                print(lista1_1[a])
            print ("*" * 99)
            opção1 = int(input("Selecione a opção desejada: "))
            print (meio1(opção1)) 

            if (opção1 <=3):
                opção4 = 3
                while opção4>2: 
                    print ("*" * 99)
                    for ab in range(len(lista_final)):
                        print(lista_final[ab])
                    print ("*" * 99)

                    opção4 = int(input("Selecione a opção desejada: "))
                    print (final(opção4))
                    if opção4 ==1:
                        break
                
                    else:
                        print( )
                            
            else:
                print( )
                
            
        
        else:
            print( )


    elif opção == 2:
        opção2 = 5
        while opção2 >4:

            print ("*" * 99) 
            for b in range(len(lista2_1)):
                print(lista2_1[b])
            print ("*" * 99) 
            opção2 = int(input("Selecione a opção desejada: "))
            print(meio2(opção2))

            if (opção2 <=3):
                opção4 = 3
                while opção4 >2:

                    print ("*" * 99) 
                    for ab in range(len(lista_final)):
                        print(lista_final[ab])
                    print ("*" * 99)

                    opção4 = int(input("Selecione a opção desejada: "))
                    print (final(opção4))
                    if opção4 ==1:
                        break
                    else:
                        print ( )
            
            else:
                print( )
        

    elif opção == 3:
        opção3 = 5
        while opção3 >4:


            print ("*" * 99) 
            for c in range(len(lista3_1)):
                print(lista3_1[c])   
            print ("*" * 99)
            opção3 = int(input("Selecione a opção desejada: "))
            print(meio3(opção3))
            if (opção3 <=3) :
                opção4 = 3
                while opção4 >2:
                    print ("*" * 99) 
                    for ab in range(len(lista_final)):
                        print(lista_final[ab])
                    print ("*" * 99)

                    opção4 = int(input("Selecione a opção desejada: "))
                    print (final(opção4))
                    if opção4 ==1:
                        break
                        
                    else:
                        print( )
        
        else:
            print( )
    
    elif opção == 4:
        break
    elif opção4 ==1:
        break

    else:
        print(" ")

print ("O Trust Bank agradece seu contato e não esqueça, banco de confiança é Trust Bank")
        
