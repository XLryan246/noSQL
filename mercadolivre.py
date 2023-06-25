from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import uuid

cloud_config= {
  'secure_connect_bundle': './secure-connect-mercadolivre.zip'
}


auth_provider = PlainTextAuthProvider('nyvsAtxFHLeuoMFoGWNrbzaA', 'gdhoWXiAKLtddUH373nQsGqG82SLXlkea4JZXeaAFNkS0XvlZXHmoBW9zdz1dZfbw7h,afjCHkKTmRohxGTRpFqMjSXSBw,h7efUZhUy+TpRNb8pUvaswXAhvmP5W358')
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

keyspace = "mercadolivre" 
session.set_keyspace(keyspace)

# session.execute ("DROP TABLE Usuario")

session.execute ("CREATE TABLE IF NOT EXISTS mercadolivre.Usuario  (id UUID PRIMARY KEY, nome_usuario TEXT, email_usuario TEXT, rg_usuario TEXT, cpf_usuario TEXT, endereco LIST<TEXT>, favoritos LIST<TEXT>)")

session.execute ("CREATE TABLE IF NOT EXISTS mercadolivre.Produtos  (id UUID PRIMARY KEY, nomeprod TEXT, quantidade TEXT, preco TEXT)")

session.execute ("CREATE TABLE IF NOT EXISTS mercadolivre.Vendedor  (id UUID PRIMARY KEY, nomevend TEXT, emailvend TEXT, cpf TEXT)")

session.execute ("CREATE TABLE IF NOT EXISTS mercadolivre.Compras (id UUID PRIMARY KEY, idusuario TEXT, idproduto TEXT, idvendedor TEXT )")


while True:
  print ('\n ---* BEM VINDO AO MERCADO LIVRE *---')

  print ("\n *** Cadastro ***")
  print ("\n 1 - Cadastrar usuario")
  print ("\n 2 - Cadastrar produto")
  print ("\n 3 - Cadastrar vendedor")
  print ("\n 4 - Cadastrar compra")

  print ("\n *** Listagem de Dados ***")
  print ("\n 5 - Listar usuario")
  print ("\n 6 - Listar produto")
  print ("\n 7 - Listar vendedor")
  print ("\n 8 - Listar Compra")

  print ("\n *** Atualizar Dados ***")
  print ("\n 9 - Atualizar dados de usuario")
  print ("\n 10 - Atualizar dados de produto")
  print ("\n 11 - Atualizar dados de vendedor")

  print ("\n *** Deletar ***")
  print ("\n 12 - Deletar usuario")
  print ("\n 13 - Deletar produto")
  print ("\n 14 - Deletar vendedor")
  print ("\n 15 - Deletar Compras")
  print ("\n 16 - Sair")

  opcao = int(input ('\n Digite o numero opcao desejada: '))

  if opcao == 1:

      nome_usuario = input("\n Digite o nome do usuário: ")
      email_usuario = input("\n Digite o email do usuário: ")
      cpf_usuario = int(input("\n Digite o CPF do usuário: "))
      favoritos = []
      endereco = []
      key = 'S'

      
      opcfav = input ("\n Deseja adicionar um favorito? (S/N): ").upper()     
      while opcfav == 'S':
        favoritos.append(input("\n Digite o id do produto a ser favoritado: "))
        opcfav = input ("\n Deseja adicionar outro favorito? (S/N): ").upper() 


      while key.upper() == 'S':
          endereco.append(input("\n Digite o cep do usuário: "))
          endereco.append(input("\n Digite o bairro do usuário: "))
          endereco.append(input("\n Digite o número da casa: "))
          endereco.append(input("\n Digite a cidade do usuário: "))
          endereco.append(input("\n Digite o estado do usuário: "))
          key = input("\n Deseja adicionar mais um endereço? (S/N): ").upper()

      session.execute(f"INSERT INTO mercadolivre.Usuario (id, nome_usuario, email_usuario, cpf_usuario, endereco, favoritos) VALUES (uuid(),'{nome_usuario}', '{email_usuario}', '{cpf_usuario}', {endereco}, {favoritos});")
      print ("usuario adicionado!")

  if opcao == 2:
    nomeprod = input('Digite o nome do produto: ')
    quantidade = input('Digite a quantidade de produtos: ')
    preco = float(input('Digite o preço do produto: '))
    session.execute(f"INSERT INTO mercadolivre.Produtos (id, nomeprod, quantidade, preco) VALUES (uuid(), '{nomeprod}', '{quantidade}', '{preco}');")
    print ("\n produto adicionado!")

  if opcao == 3:
    nomevend = input('Digite o nome do vendedor: ')
    emailvend = input('Digite o email do vendedor: ')
    cpf = int(input('Digite o CPF do vendedor: '))
    session.execute(f"INSERT INTO mercadolivre.Vendedor (id, nomevend, emailvend, cpf) VALUES (uuid(), '{nomevend}', '{emailvend}', '{cpf}');")
    print ("\n vendedor adicionado!")

  if opcao == 4:
    idusuario = input ('Digite o id do usuario: ')
    idproduto = input ('Digite o id do produto: ')
    idvendedor = input ('Digite o id do vendedor: ')

    verificador = session.execute(f"Select * from usuario where id = {idusuario} ").one()
    verificador2 = session.execute(f"Select * from produtos where id = {idproduto} ").one()
    verificador3 = session.execute(f"Select * from vendedor where id = {idvendedor} ").one()    

    session.execute(f"INSERT INTO mercadolivre.Compras (id, idusuario, idproduto, idvendedor ) VALUES (uuid(), '{idusuario}', '{idproduto}', '{idvendedor}');")
    print ("\n compra adicionada!")



  if opcao == 5:

    selectUsuario = session.execute("SELECT * FROM Usuario").all()
    print(selectUsuario)

  if opcao == 6:

    selectProdutos = session.execute("SELECT * FROM Produtos").all()
    print(selectProdutos)

  if opcao == 7:

    selectVendedor = session.execute("SELECT * FROM Vendedor").all()
    print(selectVendedor)


  if opcao == 8:
    selectCompras = session.execute("SELECT * FROM Compras").all()
    print(selectCompras)

  if opcao == 9:

    id_verificador = uuid.UUID(input('\n Digite o id do usuario que deseja atualizar: '))
    verificador = session.execute(f"Select * from usuario wherE id = {id_verificador} ").one()
    if verificador is None:
      print("usuario não encontrado!")
    else:
      nome_usuario = input("\n Digite o novo nome do usuário: ")
      email_usuario = input("\n Digite o novo email do usuário: ")
      cpf_usuario = int(input("\n Digite o novo CPF do usuário: "))
      endereco = []
      key = 'S'

      while key.upper() == 'S':
          endereco.append(input("\n Digite o novo cep do usuário: "))
          endereco.append(input("\n Digite o novo bairro do usuário: "))
          endereco.append(input("\n Digite o novo número da casa: "))
          endereco.append(input("\n Digite a nova cidade do usuário: "))
          endereco.append(input("\n Digite o novo estado do usuário: "))
          key = input("\n Deseja adicionar mais um endereço? (S/N): ").upper()

      session.execute(f"UPDATE Usuario SET nome_usuario = '{nome_usuario}', email_usuario = '{email_usuario}', cpf_usuario = '{cpf_usuario}', endereco = {endereco} WHERE id = {id_verificador}")
      print ("usuario atualizado!")


  if opcao == 10:

      id_verificador = uuid.UUID(input('\n Digite o id do produto que deseja atualizar: '))
      verificador = session.execute(f"Select * from produtos where id = {id_verificador} ").one()
      if verificador is None:
        print("produto não encontrado!")
      else:
        nomeprod = input('Digite o novo nome do produto: ')
        quantidade = input('Digite a nova quantidade de produtos: ')
        preco = float(input('Digite o novo preço do produto: '))

        session.execute(f"UPDATE Produtos SET nomeprod = '{nomeprod}', quantidade = '{quantidade}', preco = '{preco}' WHERE id = {id_verificador}")
        print ("produto atualizado!")

  if opcao == 11:

      id_verificador = uuid.UUID(input('\n Digite o id do vendedor que deseja atualizar: '))
      verificador = session.execute(f"Select * from vendedor where id = {id_verificador} ").one()
      if verificador is None:
        print("vendedor não encontrado!")
      else:
        nomevend = input('Digite o novo nome do vendedor: ')
        emailvend = input('Digite o novo email do vendedor: ')
        cpf = int(input('Digite o novo CPF do vendedor: '))

        session.execute(f"UPDATE Vendedor SET nomevend = '{nomevend}', emailvend = '{emailvend}', cpf = '{cpf}' WHERE id = {id_verificador}")
        print ("Vendedor atualizado!")

  if opcao == 12:
    
      id_verificador = uuid.UUID(input('\n Digite o id do usuario que deseja deletar: '))
      verificador = session.execute(f"Select * from usuario where id = {id_verificador} ").one()
      if verificador is None:
        print("usuario não encontrado!")
      else:
        session.execute(f"DELETE from Usuario where id = {id_verificador}")
        print ("Usuario deletado!")

  if opcao == 13:
    
      id_verificador = uuid.UUID(input('\n Digite o id do produto que deseja deletar: '))
      verificador = session.execute(f"Select * from produtos where id = {id_verificador} ").one()
      if verificador is None:
        print("produto não encontrado!")
      else:
        session.execute(f"DELETE from Produtos where id = {id_verificador}")
        print ("Produto deletado!")

  if opcao == 14:
    
      id_verificador = uuid.UUID(input('\n Digite o id do vendedor que deseja deletar: '))
      verificador = session.execute(f"Select * from vendedor where id = {id_verificador} ").one()
      if verificador is None:
        print("produto não encontrado!")
      else:
        session.execute(f"DELETE from Vendedor where id = {id_verificador}")
        print ("Vendedor deletado!")  
  

  if opcao == 15:

    id_verificador = uuid.UUID(input('\n Digite o id da compra que deseja deletar: '))
    verificador = session.execute(f"Select * from compras where id = {id_verificador} ").one()
    if verificador is None:
      print("compra não encontrada!")
    else:
      session.execute(f"DELETE from Compras where id = {id_verificador}")
      print ("Compra deletado!")  

  if opcao == 16:
    break