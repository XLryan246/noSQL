#https://www.w3schools.com/python/python_mongodb_find.asp
import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from datetime import datetime


client = pymongo.MongoClient("mongodb+srv://XLryan246:root@mercadolivre.cx2fknq.mongodb.net/MercadoLivre?retryWrites=true&w=majority", server_api=ServerApi('1'))

global mydb
mydb = client.MercadoLivre

mycol = mydb["usuarios"]
mycolprod = mydb["produtos"]
mycolseller = mydb["vendedor"]
mycolbuy = mydb["compras"]



#inserts
def insert(nome, email, end):
    
    global mydb
    mycol = mydb.usuario
    print("\n####INSERT####")
    mydict = { "nome": nome, 
    "email":email, 
    "end":end, 
    }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


def insertprod(nomeprod, quantidade, preco, vendedor):
    
    global mydb
    mycoldseller = mydb.vendedor
    myquery = { "_id": ObjectId(vendedor) }
    objVendedor= mycolseller.find_one(myquery)


    mycolprod = mydb.produtos
    mydict = { "nomeprod": nomeprod, "quantidade":quantidade, "preco":preco, "vendedor" : objVendedor }
    x = mycolprod.insert_one(mydict)
    print(x.inserted_id)


def insertfav(email, favoritos):
    
    global mydb
    mycol = mydb.usuario
    myquery = { "email": (email) }
    newvalues = { "$set": { "favoritos": favoritos } }
    mycol.update_one(myquery, newvalues)
    print("favorito adicionado")


def insertBuy(idprod, idusuario):
    data = datetime.now()
    dataFormat = data.strftime("%d/%m/%Y %H:%M:%S")
    global mydb
    #usuario
    mycol = mydb.usuario
    myquery = { "_id": ObjectId(idusuario) }
    mydoc = mycol.find_one(myquery)
    #produtos
    mycolprod = mydb.produtos
    myquery = { "_id": ObjectId(idprod) }
    mydoc2 = mycolprod.find_one(myquery)
   

    mycolbuy = mydb.compras
    mydict = { "usuario": mydoc, "produtos": mydoc2, "data": dataFormat }
    x = mycolbuy.insert_one(mydict)
    print (x)



#findsorts
def findSortProd():
    
    global mydb
    mycolprod = mydb.produtos
    print("\n####SORT####") 
    mydoc = mycolprod.find().sort("nomeprod")
    for x in mydoc:
        print(x)



def findSortUsu():
    
    global mydb
    mycol = mydb.usuario
    print("\n####SORT####") 
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)


def findSortSeller():
    
    global mydb
    mycolseller = mydb.vendedor
    print("\n####SORT####") 
    mydoc = mycolseller.find().sort("nome")
    for x in mydoc:
        print(x)


def findSortBuy():
    
    global mydb
    mycolbuy = mydb.compras
    print("\n####SORT####") 
    mydoc = mycolbuy.find().sort("nome")
    for x in mydoc:
        print(x)



    #Query
def findQuery(nomezin):
    
    global mydb
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "nome": nomezin }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)



def findQueryProd(produtin):
    
    global mydb
    mycolprod = mydb.produtos
    print("\n####QUERY####")
    myquery = { "nomeprod": produtin }
    mydoc = mycolprod.find(myquery)
    for x in mydoc:
        print(x)


def findQuerySeller(seller):
    
    global mydb
    mycolseller = mydb.vendedor
    print("\n####QUERY####")
    myquery = { "nomeseller": seller }
    mydoc = mycolseller.find(myquery)
    for x in mydoc:
        print(x)

def findFav(email):
        
    global mydb
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "email": email }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x["favoritos"])


def findQueryBuy(idcompra):
    
    global mydb
    mycolbuy = mydb.compras
    
    myquery = { "_id": ObjectId(idcompra) }
    mydoc = mycolbuy.find(myquery)
    for x in mydoc:
        print(x)



def updateUsu(_id,nome, email):
    
    global mydb
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "_id": ObjectId(_id) }
    newvalues = { "$set": { "nome": nome, "email": email } }
    x = mycol.update_one(myquery, newvalues)
    print(x.modified_count,"dados atualizados.")


def updateProd(_id,nomeprod,quantidade,preco):
    
    global mydb
    mycolprod = mydb.produtos
    print("\n####QUERY####")
    myquery = { "_id": ObjectId(_id) }
    newvalues = { "$set": { "nomeprod": nomeprod, "quantidade": quantidade, "preco": preco } }
    x = mycolprod.update_one(myquery, newvalues)
    print(x.modified_count,"dados atualizados.")


def updateSeller(nomeseller,email,cpf):
    
    global mydb
    mycolseller = mydb.vendedor
    print("\n####QUERY####")
    myquery = { "_id": ObjectId(_id) }
    newvalues = { "$set": { "nomeseller": nomeseller , "emailseller" : email, "cpf" : cpf } }
    x = mycolseller.update_one(myquery, newvalues)
    print(x.modified_count,"dados atualizados.")



        #DELETE

def DeleteUsu(_id):

    global mydb
    mycol= mydb.usuario
    print ("\n###DELETE###")
    myquery = {"_id": ObjectId(_id)}
    mydoc = mycol.delete_one(myquery)


def DeleteProd(_id):

    global mydb
    mycolprod= mydb.produtos
    print ("\n###DELETE###")
    myquery = {"_id": ObjectId(_id)}
    mydoc = mycolprod.delete_one(myquery)


def DeleteSeller(_id):

    global mydb
    mycolseller= mydb.vendedor
    myquery = {"_id": ObjectId(_id)}
    mydoc = mycolseller.delete_one(myquery)

def DeleteFav(email, contador):
    global mydb
    mycol= mydb.usuario
    myquery = {"email": email}
    mydoc = mycol.find(myquery)
    for x in mydoc:
        favoritos = x["favoritos"]
        favoritos.pop(contador)
    newvalues = { "$set": { "favoritos": favoritos } }
    mycol.update_one(myquery, newvalues)
    print("favorito removido")


def DeleteBuy(_id):
    global mydb
    mycolbuy= mydb.compras
    myquery = {"_id": ObjectId(_id)}
    mydoc = mycolbuy.delete_one(myquery)



while True:
    print ("\n ---* BEM VINDO AO MERCADO LIVRE *---")

    print ("\n*** cadastro ***")

    print ("1 - cadastrar usuario")
    print ("2 - cadastro de produto ")
    print ("3 - cadastro de vendedor ")
    print ("4 - cadastro de favorito ")
    print ("5 - cadastro de compra ")
    
    print ("\n*** consulta geral ***")

    print ("6 - consulta geral de usuario")
    print ("7 - consulta geral de produto")
    print ("8 - consulta geral de vendedor")
    print ("9 - consulta geral de compras")
   


    print ("\n*** consulta unica ***")
    print ("10 - consultar usuario")
    print ("11 - consultar produto")
    print ("12 - consultar vendedor")
    print ("13 - consultar favorito")
    print ("14 - consultar compra")

    print ("\n*** atualizar ***")

    print ("15 - atualizar usuario")
    print ("16 - atualizar produto")
    print ("17 - atualizar vendedor")
    


    print ("\n*** deletar ***")
    print ("18 - deletar usuario")
    print ("19 - deletar produto")
    print ("20 - deletar vendedor")
    print ("21 - deletar favoritos")
    print ("22 - deletar compras")

    print ("23 - Sair")

    opcao = int (input("Digite a opção desejada: "))


    if opcao == 1:

        nome = str (input("digite o nome do usuario: "))
        email = str (input("digite o email do usuario: "))
        end = []


        key = 1

        while (key != 'N'):
            

            cep = input ("digite o cep do usuario: "), 
            bairro = input ("digite o bairro do usuario: "),
            num = input ("digite o numero da casa: "), 
            cidade = input ("digite a cidade do usuario: "), 
            estado = input ("digite o estado do usuario: ")
        
            endereco = {
                "cep": cep,
                "bairro": bairro,
                "num": num,
                "cidade": cidade,
                "estado": estado
            }
            end.append(endereco)
            key = input("deseja adicionar mais um endereco? (S/N): ")

        insert(nome, email, end)



    elif opcao == 2:
        nomeprod = str (input("digite o nome do produto: "))
        quantidade = int (input("quantidade: "))
        preco = float (input("preco: "))
        vendedor = str (input("digite o id do vendedor: "))

        insertprod(nomeprod, quantidade, preco, vendedor)
        


    elif opcao == 3:
        nomeseller = str (input("digite o nome do vendedor: "))
        emailseller = str (input("digite o email do vendedor: "))
        cpf = str (input("digite o cpf do vendedor: "))


        insertseller(nomeseller, emailseller, cpf)


    elif opcao == 4:
        email = str (input("digite o email do usuario: "))
        findSortProd()
        idprod = str (input("\n digite o id do produto para ser adicionado aos favoritos: "))

        

        mycolprod= mydb.produtos
        myquery = {"_id": ObjectId(idprod)}
        mydoc = mycolprod.find_one(myquery)
        fav = []
        fav.append(mydoc)

        key = input("deseja adicionar mais produtos aos favoritos? (S/N): ")
        

        while (key != 'N'):
            idprod = str (input("\n digite o id do produto para ser adicionado aos favoritos: "))
            mycolprod= mydb.produtos
            myquery = {"_id": ObjectId(idprod)}
            mydoc = mycolprod.find_one(myquery)
            fav.append(mydoc)
            key = input("deseja adicionar mais produtos aos favoritos? (S/N): ")
        insertfav(email, fav)
                        


    elif opcao == 5:
        idprod = str (input("digite o id do produto: "))
        idusuario = str (input("digite o id do usuario: "))
        insertBuy(idprod,idusuario)

    #Read (Select)
            #Sort


    elif opcao == 6:
        findSortUsu()




    elif opcao == 7:
        findSortProd()




    elif opcao == 8:
        findSortSeller()


    elif opcao == 9:
        findSortBuy()



            

    elif opcao == 10:
        nomezin = str (input("digite o nome do usuario: "))
        findQuery(nomezin)




    elif opcao == 11:
        produtin = str (input("digite o nome do produto: "))
        findQueryProd(produtin)





    elif opcao == 12:
        seller = str (input("digite o nome do vendedor: "))
        findQuerySeller(seller)



    elif opcao == 13:
        email = str (input("digite o email do usuario: "))
        findFav(email)


    elif opcao == 14:
        idcompra = str (input("digite o id do compras: "))
        findQueryBuy(idcompra)
        #UPDATE



    elif opcao == 15:
        _id = str (input("digite o id do usuario: "))
        nome = str (input("digite o novo nome do usuario: "))
        email = str (input("digite o novo email do usuario: "))

        updateUsu(_id,nome, email)





    elif opcao == 16:
        _id = str (input("digite o id do produto: "))
        nomeprod = str (input("digite o novo nome do produto: "))
        quantidade = int (input("digite a nova quantidade: "))
        preco = float (input("digite o novo preco: "))
        updateProd(_id, quantidade, nomeprod, preco)




    elif opcao == 17:
        _id = str (input("digite o id do vendedor: "))
        nomeseller = str (input("digite o novo nome do vendedor: "))
        email = str (input("digite o novo email: "))
        cpf = int (input("digite o novo cpf: "))
        updateSeller(nomeseller,email,cpf)
            


    elif opcao == 18:
        _id = str(input("digite o id do usuario que quer excluir: "))
        DeleteUsu(_id)



    elif opcao == 19:
        _id = str(input("digite o id do produto que quer excluir: "))
        DeleteProd(_id)



    elif opcao == 20:
        _id = str(input("digite o id do vendedor que quer excluir: "))
        DeleteSeller(_id)

    elif opcao == 21:
        contador = 0
        email = str (input("digite o email do usuario: "))
        mycol = mydb.usuario
        myquery = {"email": email}
        mydoc = mycol.find(myquery)
        idprod = str (input("\n digite o id do produto que deseja remover dos fav: "))
        for x in mydoc:

            if idprod == str(x["favoritos"][contador] ["_id"]):
                break
            contador = contador + 1
        DeleteFav(email, contador)


    elif opcao == 22:
        _id = str(input("digite o id da compra que quer excluir: "))
        DeleteBuy(_id) 


    if opcao == 23:
        print("Obrigado por usar nosso sistema")
        break
