class Professor:
    def __init__(self, nome):
        self.nome = nome
    
    def ministrar_aula(self, assunto):
        return f"O professor {self.nome} está ministrando uma aula sobre {assunto}."


class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def presenca(self):
        return f"O aluno {self.nome} está presente."


class Aula:
    def __init__(self, professor, assunto, alunos=None):
        self.professor = professor
        self.assunto = assunto
        if alunos is None:
            self.alunos = []
        else:
            self.alunos = alunos
    
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_presenca(self):
        lista_presenca = f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n"
        for aluno in self.alunos:
            lista_presenca += aluno.presenca() + "\n"
        return lista_presenca

professor = Professor("Python")
aluno1 = Aluno("Ewel")
aluno2 = Aluno("Fernandes")
aluno3 = Aluno("Pereira")
aula = Aula(professor, "POO")
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)
aula.adicionar_aluno(aluno3)
print(aula.listar_presenca())

professor2 = Professor("C++")
professor2.ministrar_aula("Melhor")