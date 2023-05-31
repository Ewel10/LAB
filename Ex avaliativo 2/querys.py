from database import Database
db = Database("bolt://44.203.114.213:7687", "neo4j", "gas-seas-comforts")

# 1
result = db.execute_query("MATCH(t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf")
print("Consulta 1:")
for record in result:
    print(record['t.ano_nasc'], record['t.cpf'])

result = db.execute_query("MATCH(t:Teacher) WHERE t.name STARTS WITH $letter RETURN t.name, t.cpf", parameters={"letter": "M"})
print("Consulta 2:")
for record in result:
    print(record['t.name'], record['t.cpf'])

result = db.execute_query("MATCH(c:City) RETURN c.name")
print("Consulta 3:")
for record in result:
    print(record['c.name'])

result = db.execute_query("MATCH(s:School) WHERE s.number >= $min_number AND s.number <= $max_number RETURN s.name, s.address, s.number", parameters={"min_number": 150, "max_number": 550})
print("Consulta 4:")
for record in result:
    print(record['s.name'], record['s.address'], record['s.number'])
    
# 2
result = db.execute_query("MATCH(t:Teacher) RETURN min(t.ano_nasc) as min_year, max(t.ano_nasc) as max_year")
print("Consulta 5:")
for record in result:
    print(f"Ano mínimo: {record['min_year']}, Ano máximo: {record['max_year']}")

result = db.execute_query("MATCH(c:City) RETURN avg(c.population)")
print("Consulta 6:")
for record in result:
    print(record[0])

result = db.execute_query("MATCH(c:City{cep:'37540-000'}) RETURN replace(c.name, 'a', 'A')")
print("Consulta 7:")
for record in result:
    print(record[0])

result = db.execute_query("MATCH(t:Teacher) RETURN substring(t.name, 2)")
print("Consulta 8:")
for record in result:
    print(record[0])