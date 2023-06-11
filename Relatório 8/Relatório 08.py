from py2neo import Graph, Node, Relationship

class Player:
    def __init__(self, name):
        self.name = name
        self.node = Node("Player", name=name)


class GameDB:
    def __init__(self, uri, user, password):
        self.graph = Graph(uri, auth=(user, password))

    def create_player(self, player):
        tx = self.graph.begin()
        tx.create(player.node)
        game_db.graph.commit(tx)
        return player

    def create_match(self, players, result):
        tx = self.graph.begin()
        match_node = Node("Match", result=result)
        tx.create(match_node)
        for player in players:
            player_node = self.graph.nodes.get(player.node.identity)
            relationship = Relationship(player_node, "PLAYED", match_node)
            tx.create(relationship)
        game_db.graph.commit(tx)
        return match_node


if __name__ == '__main__':
    uri = "bolt://3.231.206.24:7687"
    username = "neo4j"
    password = "landings-projectile-compliances"
    game_db = GameDB(uri, username, password)

    ewel = game_db.create_player(Player("Ewel"))
    matheus = game_db.create_player(Player("Matheus"))
    vinicius = game_db.create_player(Player("Vinicius"))
    edmundo = game_db.create_player(Player("Edmundo"))
    jv = game_db.create_player(Player("JV"))

    match = game_db.create_match([ewel, matheus, vinicius], "Vinicius venceu")
    print(match)

