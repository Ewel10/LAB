from database import Database
from professorCRUD import *

class CLI_Simples:
    def __init__(self):
        self.comandos = {}

    def adicionar_comando(self, nome, funcao):
        self.comandos[nome] = funcao

    def executar(self):
        while True:
            comando = input("Digite um comando: ")
            if comando == "sair":
                print("Até logo!")
                break
            elif comando in self.comandos:
                self.comandos[comando]()
            else:
                print("Comando inválido. Tente novamente.")


class CLI_Professor(CLI_Simples):
    def __init__(self, professor_crud):
        super().__init__()
        self.professor_crud = professor_crud
        self.adicionar_comando("criar", self.criar_professor)
        self.adicionar_comando("ler", self.ler_professor)
        self.adicionar_comando("atualizar", self.atualizar_professor)
        self.adicionar_comando("excluir", self.excluir_professor)

    def criar_professor(self):
        nome = input("Digite o nome do professor: ")
        ano_nasc = int(input("Digite o ano de nascimento do professor: "))
        cpf = input("Digite o CPF do professor: ")
        self.professor_crud.criar(nome, ano_nasc, cpf)

    def ler_professor(self):
        nome = input("Digite o nome do professor: ")
        professor = self.professor_crud.ler(nome)
        print(professor)

    def atualizar_professor(self):
        nome = input("Digite o nome do professor: ")
        novo_cpf = input("Digite o novo CPF do professor: ")
        self.professor_crud.atualizar(nome, novo_cpf)
    
    def excluir_professor(self):
        nome = input("Digite o nome do professor: ")
        self.professor_crud.excluir(nome)

    def executar(self):
        print("Bem-vindo ao CLI do Professor!")
        print("Comandos disponíveis: criar, ler, atualizar, excluir, sair")
        super().executar()


database = Database("bolt://44.203.114.213:7687", "neo4j", "gas-seas-comforts")
professor_crud = ProfessorCRUD(database)
cli = CLI_Professor(professor_crud)
cli.executar()
database.fechar()