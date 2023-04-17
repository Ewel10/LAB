from database import Database
from classes import Motorista, Corrida, Passageiro
from motoristaDAO import MotoristaDAO
from MotoristaCLI import MotoristaCLI

db = Database(database="exAvaliativo1", collection="valeMotorista")

motoristaModel = MotoristaDAO(database=db)
motoristaCLI = MotoristaCLI(motoristaModel)
motoristaCLI.run()