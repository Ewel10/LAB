from classes import Corrida, Motorista, Passageiro

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Entre com um comando: ")
            if command == "sair":
                print("Obrigado por utilizar nossos serviços!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando invalido, tente novamente.")

class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("1", self.create_motorista) #C
        self.add_command("2", self.read_motorista)   #R
        self.add_command("3", self.update_motorista) #U
        self.add_command("4", self.delete_motorista) #D

    def create_motorista(self):
        notas = 0
        corridas = []
        nome = input("Nome do passageiro: ")
        documento = input("Documento do passageiro: ")
        passageiro = Passageiro(nome, documento)

        qntCorridas = int(input("Quantidade de Corridas: "))
        for i in range(qntCorridas):
            nota = int(input(f"Corrida {i + 1}: Nota: "))
            notas += nota
            distancia = float(input(f"Corrida {i + 1}: Distancia: "))
            valor = float(input(f"Corrida {i + 1}: Valor: "))
            corrida = Corrida(nota, distancia, valor, passageiro.to_dict())
            corridas.append(vars(corrida))

        motorista = Motorista(corridas, notas//qntCorridas)
        self.motorista_model.create_motorista(motorista)


    def read_motorista(self):
        id = input("Id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        if motorista:
            print(f"Média de notas: {motorista['nota média']}")
            for x in motorista['corridas']:
                print(f"!!! Corrida !!!")
                print(f"")
                print(f"Nota: {x['nota']}")
                print(f"Distancia: {x['distancia']}")
                print(f"Valor: {x['valor']}")
                print(f"Passageiro: {x['passageiro']['nome']}")
                print(f"Documento: {x['passageiro']['documento']}")

    def update_motorista(self):
        id = input("Id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)

        if motorista:
            corridas_new = []
            nome = input("Passageiro: ")
            documento = input("Documento do passageiro: ")
            passageiro = Passageiro(nome, documento)
            qntCorridas = int(input("Quantidade de corridas:"))
            for i in range(qntCorridas):
                nota = int(input(f"{i + 1} - Nota: "))
                distancia = float(input(f"{i + 1} - Distância: "))
                valor = float(input(f"{i + 1} - Valor: "))
                corrida = Corrida(nota, distancia, valor, passageiro.to_dict())
                corridas_new.append(vars(corrida))
            self.motorista_model.update_motorista(id,corridas_new)

    def delete_motorista(self):
        id = input("Id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Faça o CRUD aqui! Siga os comandos abaixo:")
        print("1 - Create, 2 - Read, 3 - Update, 4 - Delete. Use também o comando \"sair\" para sair.")
        super().run()