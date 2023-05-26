#https://www.w3schools.com/python/python_mongodb_find.asp
import pymongo
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId

client = pymongo.MongoClient("mongodb+srv://XLryan246:root@mercadolivre.cx2fknq.mongodb.net/MercadoLivre?retryWrites=true&w=majority", server_api=ServerApi('1'))

global mydb
mydb = client.MercadoLivre

mycol = mydb["usuarios"]
mycolprod = mydb["produtos"]
mycolseller = mydb["vendedor"]
mycolbuy = mydb["compras"]


print ("---* BEM VINDO AO MERCADO LIVRE *---")

print ("\n*** cadastro ***")

print ("1 - cadastrar usuario")
print ("2 - cadastro de produto ")
print ("3 - cadastro de vendedor ")
print ("19 - cadastro de favorito ")

print ("\n*** consulta geral ***")

print ("4 - consulta geral de usuario")
print ("5 - consulta geral de produto")
print ("6 - consulta geral de vendedor")
print ("7 - consulta geral de compras")


print ("\n*** consulta unica ***")
print ("8 - consultar usuario")
print ("9 - consultar produto")
print ("10 - consultar vendedor")


print ("\n*** atualizar ***")

print ("11 - atualizar usuario")
print ("12 - atualizar produto")
print ("13 - atualizar vendedor")


print ("\n*** deletar ***")
print ("14 - deletar usuario")
print ("15 - deletar produto")
print ("16 - deletar vendedor")
print ("17 - deletar favoritos")

print ("18 - Sair")

opcao = int (input("Digite a opção desejada: "))

    #inserts
def insert(nome, email, end):
    
    global mydb
    mycol = mydb.usuario
    print("\n####INSERT####")
    mydict = { "nome": nome, 
    "email":email, 
    "end":end, 
    "cupom":cup,
    #"favoritos": [{"idproduto":idproduto , "nomeprod":nomeprod , "preco":preco }]
    }
    x = mycol.insert_one(mydict)
    print(x.inserted_id)


if opcao == 1:

    nome = str (input("digite o nome do usuario: "))
    email = str (input("digite o email do usuario: "))
    end = []
    cup = []
    

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
    


def insertprod(nomeprod, quantidade, preco):
    
    global mydb
    mycolprod = mydb.produtos
    print("\n####INSERT####")
    mydict = { "nomeprod": nomeprod, "quantidade":quantidade, "preco":preco }
    x = mycolprod.insert_one(mydict)
    print(x.inserted_id)


if opcao == 2:
    nomeprod = str (input("digite o nome do produto: "))
    quantidade = int (input("quantidade: "))
    preco = float (input("preco: "))

    insertprod(nomeprod, quantidade, preco)
    main()


def insertseller(nomeseller, emailseller, cpf):
    
    global mydb
    mycolseller = mydb.vendedor
    print("\n####INSERT####")
    mydict = { "nomeseller": nomeseller, "emailseller":emailseller, "cpf":cpf }
    x = mycolseller.insert_one(mydict)
    print(x.inserted_id)

if opcao == 3:
    nomeseller = str (input("digite o nome do vendedor: "))
    emailseller = str (input("digite o email do vendedor: "))
    cpf = str (input("digite o cpf do vendedor: "))


    insertseller(nomeseller, emailseller, cpf)


if opcao == 19:

    findSortProd()
        
    fav = []


    key = 1

    while (key != 'N'):
        

        cep = input ("digite o cep do usuario: "), 
        bairro = input ("digite o bairro do usuario: "),
        num = input ("digite o numero da casa: "), 
        cidade = input ("digite a cidade do usuario: "), 
        estado = input ("digite o estado do usuario: ")
    
        favoritos = {
            "cep": cep,
            "bairro": bairro,
            "num": num,
            "cidade": cidade,
            "estado": estado
        }
        end.append(endereco)
        key = input("deseja adicionar mais um endereco? (S/N): ")

    insert(nome, email, end)






#Read (Select)
        #Sort
def findSortUsu():
    
    global mydb
    mycol = mydb.usuario
    print("\n####SORT####") 
    mydoc = mycol.find().sort("nome")
    for x in mydoc:
        print(x)

if opcao == 4:
    findSortUsu()


def findSortProd():
    
    global mydb
    mycolprod = mydb.produtos
    print("\n####SORT####") 
    mydoc = mycolprod.find().sort("nomeprod")
    for x in mydoc:
        print(x)

if opcao == 5:
    findSortProd()


def findSortSeller():
    
    global mydb
    mycolseller = mydb.vendedor
    print("\n####SORT####") 
    mydoc = mycolseller.find().sort("nome")
    for x in mydoc:
        print(x)

if opcao == 6:
    findSortSeller()


if opcao == 7:
    findSortBuy()


    #Query
def findQuery(nomezin):
    
    global mydb
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "nome": nomezin }
    mydoc = mycol.find(myquery)
    for x in mydoc:
        print(x)
        

if opcao == 8:
    nomezin = str (input("digite o nome do usuario: "))
    findQuery(nomezin)


def findQueryProd(produtin):
    
    global mydb
    mycolprod = mydb.produtos
    print("\n####QUERY####")
    myquery = { "nomeprod": produtin }
    mydoc = mycolprod.find(myquery)
    for x in mydoc:
        print(x)

if opcao == 9:
    produtin = str (input("digite o nome do produto: "))
    findQueryProd(produtin)



def findQuerySeller(seller):
    
    global mydb
    mycolseller = mydb.vendedor
    print("\n####QUERY####")
    myquery = { "nomeseller": seller }
    mydoc = mycolseller.find(myquery)
    for x in mydoc:
        print(x)

if opcao == 10:
    seller = str (input("digite o nome do vendedor: "))
    findQuerySeller(seller)


    #UPDATE

def updateUsu(_id,nome, email):
    
    global mydb
    mycol = mydb.usuario
    print("\n####QUERY####")
    myquery = { "_id": ObjectId(_id) }
    newvalues = { "$set": { "nome": nome, "email": email } }
    x = mycol.update_one(myquery, newvalues)
    print(x.modified_count,"dados atualizados.")

if opcao == 11:
    _id = str (input("digite o id do usuario: "))
    nome = str (input("digite o novo nome do usuario: "))
    email = str (input("digite o novo email do usuario: "))

    updateUsu(_id,nome, email)


def updateProd(_id,nomeprod,quantidade,preco):
    
    global mydb
    mycolprod = mydb.produtos
    print("\n####QUERY####")
    myquery = { "_id": ObjectId(_id) }
    newvalues = { "$set": { "nomeprod": nomeprod, "quantidade": quantidade, "preco": preco } }
    x = mycolprod.update_one(myquery, newvalues)
    print(x.modified_count,"dados atualizados.")


if opcao == 12:
    _id = str (input("digite o id do produto: "))
    nomeprod = str (input("digite o novo nome do produto: "))
    quantidade = int (input("digite a nova quantidade: "))
    preco = float (input("digite o novo preco: "))
    updateProd(_id, quantidade, nomeprod, preco)


def updateSeller(nomeseller,email,cpf):
    
    global mydb
    mycolseller = mydb.vendedor
    print("\n####QUERY####")
    myquery = { "_id": ObjectId(_id) }
    newvalues = { "$set": { "nomeseller": nomeseller , "emailseller" : email, "cpf" : cpf } }
    x = mycolseller.update_one(myquery, newvalues)
    print(x.modified_count,"dados atualizados.")

if opcao == 13:
    _id = str (input("digite o id do vendedor: "))
    nomeseller = str (input("digite o novo nome do vendedor: "))
    email = str (input("digite o novo email: "))
    cpf = int (input("digite o novo cpf: "))
    updateSeller(nomeseller,email,cpf)
        
        
        #DELETE

def DeleteUsu(_id):

    global mydb
    mycol= mydb.usuario
    print ("\n###DELETE###")
    myquery = {"_id": ObjectId(_id)}
    mydoc = mycol.delete_one(myquery)


if opcao == 14:
    _id = str(input("digite o id do usuario que quer excluir: "))
    DeleteUsu(_id)



def DeleteProd(_id):

    global mydb
    mycolprod= mydb.produtos
    print ("\n###DELETE###")
    myquery = {"_id": ObjectId(_id)}
    mydoc = mycolprod.delete_one(myquery)

if opcao == 15:
    _id = str(input("digite o id do produto que quer excluir: "))
    DeleteProd(_id)



def DeleteSeller(_id):

    global mydb
    mycolseller= mydb.vendedor
    print ("\n###DELETE###")
    myquery = {"_id": ObjectId(_id)}
    mydoc = mycolseller.delete_one(myquery)

if opcao == 16:
    _id = str(input("digite o id do vendedor que quer excluir: "))
    DeleteSeller(_id)













############# main

    #insert#

#insert("bkay", "b@b", "SP")

#insertprod("album","3","400")

#insertseller("dfideliz", "d@d", "125-94")


    #select

#findSortUsu() #pegar todos que estao dentro daquele parametro
#findSortProd()
#findSortSeller()


    #update

#updateUsu()
#updateProd()
#updateSeller()



#pegar a linha que o parametro inserido se encontra

#findQuery() 
#findQueryProd()
#findQuerySeller()

    #delete

#DeleteUsu()
#DeleteProd()
#DeleteSeller()
