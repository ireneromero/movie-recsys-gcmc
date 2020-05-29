import unittest
from src.neo4j.utils import connect_from_file, query_graph
class TestNeo4J(unittest.TestCase):

    PATH_CONNECTION = '/home/irene/dev/movie-recsys-gcmc/env/neo4j_connection.json'
    NUM_NODES = 30028

    # def test_open_connection(self):
    #     graph = connect_from_file(self.PATH_CONNECTION)
    #     print(graph)

    def test_query(self):
        graph = connect_from_file(self.PATH_CONNECTION)

        query = """
        MATCH (n) RETURN count(n) as num_nodes
        """

        result = query_graph(graph, query).data()
        self.assertEqual(result[0]['num_nodes'], self.NUM_NODES)


