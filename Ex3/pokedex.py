from typing import Collection
import pymongo
from dataset.pokemon_dataset import dataset
from helper.writeAJson import writeAJson

class Pokedex:
    pass

class Database:
    def __init__(self, database, collection, pokedex: Pokedex):
        _pokedex = Pokedex
        self.connect(database, collection)
        
    def connect(self, database, collection):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try: 
            self.db.drop_collection(self.collection)
            self.collection.insert_many(dataset)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)

db = Database(database="pokedex", collection="pokemons", pokedex=Pokedex)
db.resetDatabase

pokedex1 = db.collection.find({"$or": [{"type":"Fire"},{"weaknesses": "Water"}]}) #pokemons do tipo fogo ou com fraqueza ao tipo água
writeAJson(pokedex1, "pokemons1")
pokedex2 = db.collection.find({"next_evolution.1.num": {"$lte": "030"}}) #pokemons que a segunda evolução aparece até o #31 da pokedex
writeAJson(pokedex2, "pokemons2")
pokedex3 = db.collection.find({"spawn_chance": {"$gt": 0.6, "$lt": 0.9}}) #pokemons com o spawnrate entre 0.6 e 0.9
writeAJson(pokedex3, "pokemons3")
pokedex4 = db.collection.find({"weaknesses": {"$size": 6}}) #pokemons com 6 ou mais fraquezas
writeAJson(pokedex4, "pokemons4")
fraquezas = ["Fire", "Ice"] #definindo as fraquezas
pokedex5 = db.collection.find({"weaknesses": {"$all": fraquezas}}) #mostrando os pokemons que sofrem das duas fraquezas definidas
writeAJson(pokedex5, "pokemons5")
