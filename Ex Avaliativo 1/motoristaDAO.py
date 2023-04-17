from pymongo import MongoClient
from bson.objectid import ObjectId
from classes import *
from statistics import mean

class MotoristaDAO:
    def __init__(self, database):
        self.db = database
    
    def create_motorista(self, motorista: Motorista):
        try:
            res = self.db.collection.insert_one(vars(motorista))
            print(f"Motorista criado!!! Seu ID é: {res.inserted_id}")
            return res.inserted_id
        
        except Exception as e:
            print(f"Erro!! {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"O Motorista foi encontrado com sucesso!")
            return res
        except Exception as e:
            print(f"Erro!!!: {e}")
            return None

    def update_motorista(self, id: str, corridas):
        try:
            motorista = self.db.collection.find_one({"_id": ObjectId(id)})
            motorista['corridas'].extend(corridas)
            notas = [x['nota'] for x in motorista['corridas']]
            media = sum(notas) // len(notas)
            motorista['nota'] = media

            res = self.db.collection.update_one({"_id": ObjectId(id)}, {'$set': motorista})

            print(f"Motorista modificado!")
            return res.modified_count
        except Exception as e:
            print(f"Erro!!!! {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"motorista deletedo: {res.deleted_count} , documentos delatados:")
            return res.deleted_count
        except Exception as e:
            print(f"Erro!!!!! {e}")
            return None