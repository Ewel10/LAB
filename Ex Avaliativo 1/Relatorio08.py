from py2neo import Graph, Node, Relationship

class GameDatabase:
    def _init_(self, uri, username, password):
        self.graph = Graph(uri, auth=(username, password))

    def create_player(self, name):
        player = Node("Player", name=name)
        self.graph.create(player)
        return player

    def update_player(self, player_id, name):
        player = self.graph.nodes.get(player_id)
        player["name"] = name
        player.push()
        return player

    def delete_player(self, player_id):
        player = self.graph.nodes.get(player_id)
        self.graph.delete(player)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p"
        result = self.graph.run(query)
        return [record["p"] for record in result]

    def create_match(self, players, result):
        match = Node("Match", result=result)
        for player in players:
            relationship = Relationship(player, "PLAYED", match)
            self.graph.create(relationship)
        self.graph.create(match)
        return match

    def get_match(self, match_id):
        match = self.graph.nodes.get(match_id)
        players = self.graph.match(nodes=[match], r_type="PLAYED", direction="in")
        return {
            "id": match.id,
            "result": match["result"],
            "players": [player["name"] for player in players]
        }

    def get_player_matches(self, player_id):
        player = self.graph.nodes.get(player_id)
        matches = self.graph.match(nodes=[player], r_type="PLAYED", direction="out")
        return [{
            "id": match.end_node.id,
            "result": match.end_node["result"],
            "players": [player["name"] for player in self.graph.match(nodes=[match.end_node], r_type="PLAYED", direction="in")]
        } for match in matches]
        
uri = "bolt://3.231.206.24:7687"
username = "neo4j"
password = "landings-projectile-compliances"

game_db = GameDatabase(uri, username, password)