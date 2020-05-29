from src.neo4j.utils import connect_from_file, query_graph
import pandas as pd

PATH_CONNECTION = '/home/irene/dev/movie-recsys-gcmc/env/neo4j_connection.json'
PATH_TO_SAVE = '/home/irene/dev/movie-recsys-gcmc/data/edges.csv'

if __name__ == '__main__':
    # 1. Connect to graph DB
    graph = connect_from_file(PATH_CONNECTION)
    query = """
    MATCH (m:Movie)-[r:RATED]-(u:User)
    RETURN id(m) as movie_node_id, id(u) as user_node_id, r.rating as rating
    """
    result = query_graph(graph, query)
    result.to_data_frame().to_csv(PATH_TO_SAVE, header=True, index=False)