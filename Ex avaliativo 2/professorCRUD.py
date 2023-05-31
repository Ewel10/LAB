class ProfessorCRUD:
    def __init__(self, db):
        self.db = db

    def criar(self, nome, ano_nasc, cpf):
        consulta = f"CREATE(:Professor{{name:'{nome}', ano_nasc:{ano_nasc}, cpf:'{cpf}'}})"
        self.db.executar_consulta(consulta)

    def ler(self, nome):
        consulta = f"MATCH(p:Professor{{name:'{nome}'}}) RETURN p"
        resultado = self.db.executar_consulta(consulta)
        return [registro['p'] for registro in resultado]

    def excluir(self, nome):
        consulta = f"MATCH(p:Professor{{name:'{nome}'}}) DETACH DELETE p"
        self.db.executar_consulta(consulta)

    def atualizar(self, nome, novo_cpf):
        consulta = f"MATCH(p:Professor{{name:'{nome}'}}) SET p.cpf = '{novo_cpf}'"
        self.db.executar_consulta(consulta)

    def fechar(self):
        self.db.fechar()
