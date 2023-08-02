import pymongo
from pprint import pprint


client = pymongo.MongoClient("localhost", 27017)

# Conecta ao db 'dio' e depois a collection 'bank'
db = client.dio
bank = db.bank


document_1 = {
    "nome": "João",
    "cpf": "11111111111",
    "endereco": "Rua A",
    "conta": {
        "tipo": "Corrente",
        "agencia": "1",
        "conta": "123-4",
        "saldo": 100
    }
}

id_joao = bank.insert_one(document_1).inserted_id
print(id_joao)

print("Cliente João:")
pprint(db.bank.find_one())

# Lista com os demais documentos a inserir
bank_documents = [
    {
        "nome": "Maria",
        "cpf": "22222222222",
        "endereco": "Rua B",
        "conta": {
            "tipo": "Corrente",
            "agencia": "1",
            "conta": "124-0",
            "saldo": 500
        }
    },
    {
        "nome": "José",
        "cpf": "33333333333",
        "endereco": "Rua C",
        "conta": {
            "tipo": "Poupança",
            "agencia": "1",
            "conta": "123-5",
            "saldo": 50
        }
    },

]

results = bank.insert_many(bank_documents)
pprint(results.inserted_ids)

print("\nDocumentos presentes na coleção bank")
for document in bank.find():
    pprint(document)