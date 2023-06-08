import json
from py2neo import Graph, Node, Relationship

graph = Graph("neo4j+s://ba24c13b.databases.neo4j.io", auth=("neo4j", "syhburyJkk4cmsJUuM9KXpOrrjQS73mfE_IgXZ93mEQ"))

print ('\n ---* BEM VINDO AO MERCADO LIVRE *---')

print ("\n *** Cadastro ***")
print ("\n 1 - Cadastrar usuario")
print ("\n 2 - Cadastrar produto")
print ("\n 3 - Cadastrar vendedor")
print ("\n 4 - Cadastrar favorito")

print ("\n *** Listagem de Dados ***")
print ("\n 5 - Listar usuario")
print ("\n 6 - Listar produto")
print ("\n 7 - Listar vendedor")

print ("\n *** Atualizar Dados ***")
print ("\n 8 - Atualizar dados de usuario")
print ("\n 9 - Atualizar dados de produto")
print ("\n 10 - Atualizar dados de vendedor")

print ("\n *** Deletar ***")
print ("\n 11 - Deletar usuario")
print ("\n 12 - Deletar produto")
print ("\n 13 - Deletar vendedor")
print ("\n 14 - Deletar Favoritos")

opcao = int(input ('\n Digite o numero opcao desejada: '))


#                    INSERT               #
if opcao == 1:
    nome = input('Digite o nome do usuário: ')
    email = input('Digite seu email: ')
    end = []
    key = 'S'

    while key.upper() == 'S':
        cep = input("Digite o cep do usuário: ")
        bairro = input("Digite o bairro do usuário: ")
        num = input("Digite o número da casa: ")
        cidade = input("Digite a cidade do usuário: ")
        estado = input("Digite o estado do usuário: ")

        endereco = {
            "cep": cep,
            "bairro": bairro,
            "num": num,
            "cidade": cidade,
            "estado": estado
        }
        end.append(json.dumps(endereco))  # Converter o dicionário em uma string JSON
        key = input("Deseja adicionar mais um endereço? (S/N): ")

    node = Node("Usuario", nome=nome, email=email, endereco=end)
    graph.create(node)
    print ("usuario adicionado!")

if opcao == 2:
    nomeprod = input('Digite o nome do produto: ')
    quantidade = input('Digite a quantidade de produtos: ')
    preco = float(input('Digite o preço do produto: '))
    node = Node("Produtos", nome_produto=nomeprod, quantidade=quantidade, preco=preco)
    graph.create(node)
    print ("produto adicionado!")

if opcao == 3:
    nomevend = input('Digite o nome do vendedor: ')
    emailvend = input('Digite o email do vendedor: ')
    cpf = int(input('Digite o CPF do vendedor: '))
    vendedor = Node("Vendedor", nome_vendedor=nomevend, email_vendedor=emailvend, cpf=cpf)
    graph.create(vendedor)
    print ("vendedor adicionado!")


if opcao == 4:
    user_id = input("Digite o ID do usuário: ")
    product_id = input("Digite o ID do produto: ")

    # Verificar se o usuário e o produto existem
    user_query = "MATCH (u:Usuario) WHERE ID(u) = $user_id RETURN u"
    product_query = "MATCH (p:Produtos) WHERE ID(p) = $product_id RETURN p"

    user_result = graph.run(user_query, user_id=int(user_id))
    product_result = graph.run(product_query, product_id=int(product_id))

    if not user_result:
        print("Usuário não encontrado.")
    elif not product_result:
        print("Produto não encontrado.")
    else:
        # Criar o relacionamento "FAVORITO" entre o usuário e o produto
        query = """
        MATCH (u:Usuario), (p:Produtos)
        WHERE ID(u) = $user_id AND ID(p) = $product_id
        CREATE (u)-[:FAVORITO]->(p)
        """
        graph.run(query, user_id=int(user_id), product_id=int(product_id))

        print("Produto adicionado aos favoritos do usuário com sucesso!")


#                    Read               #
if opcao == 5:
    find = input("Digite o nome do usuário que deseja listar: ")
    query = "MATCH (u:Usuario {nome: $nome}) RETURN u"  # Adiciona um parâmetro de consulta para o nome do usuário
    result = graph.run(query, nome=find)
    found_users = list(result)
    if not found_users:
        print("Não encontrado")
    else:
        for found in found_users:
            print(found)

if opcao == 6:
    find = input("Digite o nome do produto que deseja listar: ")
    query = "MATCH (u:Produtos {nome_produto: $nomeprod}) RETURN u"  # Adiciona um parâmetro de consulta para o nome do usuário
    result = graph.run(query, nomeprod=find)
    found_users = list(result)
    if not found_users:
        print("Não encontrado")
    else:
        for found in found_users:
            print(found)


if opcao == 7:
    find = input("Digite o nome do produto que deseja listar: ")
    query = "MATCH (u:Vendedor {nome_vendedor: $nomevend}) RETURN u"  # Adiciona um parâmetro de consulta para o nome do usuário
    result = graph.run(query, nomevend=find)
    found_users = list(result)
    if not found_users:
        print("Não encontrado")
    else:
        for found in found_users:
            print(found)


#                    Update                 #

if opcao == 8:
        # Solicitar o ID do usuário que será atualizado
    user_id = input("Digite o ID do usuário que deseja atualizar: ")

    # Solicitar os novos valores para as propriedades do usuário
    novo_nome = input("Digite o novo nome do usuário: ")
    novo_email = input("Digite o novo email do usuário: ")

    # Executar a consulta de atualização
    query = """
    MATCH (u:Usuario)
    WHERE ID(u) = $user_id
    SET u.nome = $novo_nome, u.email = $novo_email
    RETURN u
    """
    result = graph.run(query, user_id=int(user_id), novo_nome=novo_nome, novo_email=novo_email)

    # Verificar se o nó foi atualizado com sucesso
    if result:
        print("Usuário atualizado com sucesso!")
    else:
        print("Falha ao atualizar o usuário.")



if opcao == 9:
        # Solicitar o ID do produto que será atualizado
    user_id = input("Digite o ID do produto que deseja atualizar: ")

    # Solicitar os novos valores para as propriedades do produto
    novo_nomeprod = input("Digite o novo nome do produto: ")
    nova_quantidade = input("Digite a nova quantidade do produto: ")
    novo_preco = input ("Digite o novo preco do produto: ")
    # Executar a consulta de atualização
    query = """
    MATCH (u:Produtos)
    WHERE ID(u) = $user_id
    SET u.nome_produto = $novo_nome_produto, u.quantidade = $nova_quantidade, u.preco = $novo_preco
    RETURN u
    """
    result = graph.run(query, user_id=int(user_id), novo_nome_produto = novo_nomeprod, nova_quantidade = nova_quantidade, novo_preco = novo_preco)

    # Verificar se o nó foi atualizado com sucesso
    if result:
        print("Produto atualizado com sucesso!")
    else:
        print("Falha ao atualizar o produto.")


if opcao == 10:
        # Solicitar o ID do vendedor que será atualizado
    user_id = input("Digite o ID do vendedor que deseja atualizar: ")

    # Solicitar os novos valores para as propriedades do vendedor
    novo_nome_vendedor = input("Digite o novo nome do vendedor: ")
    novo_email_vendedor = input("Digite o novo email do vendedor: ")
    novo_cpf = input ("Digite o novo CPF do vendedor: ")
    # Executar a consulta de atualização
    query = """
    MATCH (u:Vendedor)
    WHERE ID(u) = $user_id
    SET u.nome_vendedor = $novo_nome_vendedor, u.email_vendedor = $novo_email_vendedor, u.cpf = $novo_cpf
    RETURN u
    """
    result = graph.run(query, user_id=int(user_id),novo_nome_vendedor=novo_nome_vendedor, novo_email_vendedor = novo_email_vendedor, novo_cpf = novo_cpf)

    # Verificar se o nó foi atualizado com sucesso
    if result:
        print("Vendedor atualizado com sucesso!")
    else:
        print("Falha ao atualizar o produto.")

if opcao == 11:
    user_id = input("Digite o ID do usuario que deseja deletar: ")

    # Deletar relacionamentos do usuário
    query = """
    MATCH (u:Usuario)-[r]-()
    WHERE ID(u) = $user_id
    DELETE r
    """
    graph.run(query, user_id=int(user_id))

    query = """
    MATCH (u:Usuario)
    WHERE ID(u) = $user_id
    DELETE u
    """
    result = graph.run(query, user_id=int(user_id))

    if result.stats()['nodes_deleted'] > 0:
        print("Usuário deletado com sucesso!")
    else:
        print("Falha ao deletar o usuário.")


if opcao == 12:
    user_id = input("Digite o ID do produto que deseja deletar: ")
    
    # Deletar relacionamentos do produto
    query = """
    MATCH (u:Produtos)-[r]-()
    WHERE ID(u) = $user_id
    DELETE r
    """
    graph.run(query, user_id=int(user_id))
    query = """
    MATCH (u:Produtos)
    WHERE ID(u) = $user_id
    DELETE u
    """
    result = graph.run(query, user_id=int(user_id))

    if result.stats()['nodes_deleted'] > 0:
        print("Produto deletado com sucesso!")
    else:
        print("Falha ao deletar o usuário.")


if opcao == 13:
    user_id = input("Digite o ID do vendedor que deseja deletar: ")

    # Deletar relacionamentos do vendedor
    query = """
    MATCH (u:Vendedor)-[r]-()
    WHERE ID(u) = $user_id
    DELETE r
    """

    query = """
    MATCH (u:Vendedor)
    WHERE ID(u) = $user_id
    DELETE u
    """
    result = graph.run(query, user_id=int(user_id))

    if result.stats()['nodes_deleted'] > 0:
        print("Vendedor deletado com sucesso!")
    else:
        print("Falha ao deletar o usuário.")

if opcao == 14:
    user_id = input("Digite o ID do usuário: ")
    product_id = input("Digite o ID do produto: ")

    # Verificar se o usuário e o produto existem
    user_query = "MATCH (u:Usuario) WHERE ID(u) = $user_id RETURN u"
    product_query = "MATCH (p:Produtos) WHERE ID(p) = $product_id RETURN p"

    user_result = graph.run(user_query, user_id=int(user_id))
    product_result = graph.run(product_query, product_id=int(product_id))

    if not user_result:
        print("Usuário não encontrado.")
    elif not product_result:
        print("Produto não encontrado.")
    else:
        # Verificar se o relacionamento "FAVORITO" existe entre o usuário e o produto
        favorite_query = """
        MATCH (u:Usuario)-[r:FAVORITO]->(p:Produtos)
        WHERE ID(u) = $user_id AND ID(p) = $product_id
        RETURN r
        """
        favorite_result = graph.run(favorite_query, user_id=int(user_id), product_id=int(product_id))

        if not favorite_result:
            print("Produto não está nos favoritos do usuário.")
        else:
            # Deletar o relacionamento "FAVORITO" entre o usuário e o produto
            delete_query = """
            MATCH (u:Usuario)-[r:FAVORITO]->(p:Produtos)
            WHERE ID(u) = $user_id AND ID(p) = $product_id
            DELETE r
            """
            graph.run(delete_query, user_id=int(user_id), product_id=int(product_id))

            print("Produto removido dos favoritos do usuário com sucesso!")
