import redis
import pymongo
import json
import time
from pymongo.server_api import ServerApi

# Redis connect
r = redis.Redis(
    host='redis-13116.c114.us-east-1-4.ec2.cloud.redislabs.com',
    port=13116,
    password='root'
)

# MongoDB connect
client = pymongo.MongoClient("mongodb+srv://XLryan246:root@mercadolivre.cx2fknq.mongodb.net/MercadoLivre?retryWrites=true&w=majority", server_api=ServerApi('1'))
mydb = client.MercadoLivre
collection = mydb["usuario"]


nome = input("digite o usuario existente no mongoDB: ")

# Buscar o usuario no MongoDB
client_data = collection.find_one({"nome": nome})

if client_data:
    client_json = json.dumps(client_data, default=str)

    # Armazenar usuario no Redis
    r.set('usuario', client_json)
    print("Usuario encontrado e inserido no REDIS!")

    # Obter os dados do Redis
    redis_data = r.get('usuario')

    if redis_data:
        redis_dict = json.loads(redis_data)

        print("\nCadastrar cupom")

        #adição do cupom na lista vazia criada na tabela cliente do mongoDB
        new_cupom_obj = {
            "id": str(input("Digite o id do usuario que recebera o cupom: ")),
            "cupom": str(input("Digite o nome do cupom: ")),
            "desconto": str(input("Digite o desconto com % apos o numero: "))
        }

        # adicionar um cupom ao dicionario
        redis_dict.setdefault("cupom", []).append(new_cupom_obj)

        # Converter o dict pra json
        # updated_json = json.dumps(redis_dict, default=str)

        # for x in range(12):
        #     xr = r.get('cupom')
        #     print(xr)
        #     time.sleep(1)

        # redis_dict.pop("cupom", None)
        # updated_json = json.dumps(redis_dict, default=str)
        # r.set('usuario', updated_json)

        # Atualizando dados no MongoDB
        collection.update_one({"_id": client_data["_id"]}, {"$set": {"cupom": redis_dict["cupom"]}})


        print("Cupom inserido!")
    else:
        print("Erro ao obter os dados do Redis")
else:
    print("Usuario não encontrado no MongoDB")

