from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        
    def fechar(self):
        self.driver.close()
        
    def executar_consulta(self, query, parameters=None):
        with self.driver.session() as session:
            results = session.run(query, parameters=parameters)
            return [record for record in results]

    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")