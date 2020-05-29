from py2neo import Graph
import json

CONNECTION_BOLT_URL_NAME = 'bolt_url'
CONNECTION_PASSWORD_NAME = 'password'

def connect(bolt_url: str, password: str) -> Graph:
    graph = Graph(bolt_url, auth=('neo4j', password))
    return graph

def connect_from_file(path_file: str) -> Graph:
    with open(path_file) as connection_file:
        connection_details = json.load(connection_file)
        return connect(connection_details[CONNECTION_BOLT_URL_NAME], connection_details[CONNECTION_PASSWORD_NAME])

def query_graph(graph: Graph, query: str):
    return graph.run(query)


