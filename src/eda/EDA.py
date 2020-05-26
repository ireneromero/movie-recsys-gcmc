from src.neo4j.Utils import connect_from_file, query_graph
from py2neo import Graph

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH_CONNECTION = '/home/irene/dev/movie-recsys-gcmc/env/neo4j_connection.json'


def reviews_per_user(graph: Graph) -> pd.DataFrame:
    query = """
    MATCH (u:User)--(m:Movie)
    WITH u.userId as user, collect(m.title) as movies_rated
    RETURN user, count(movies_rated) as num_movies_rated
    """
    result = query_graph(graph, query).to_data_frame()
    return result

def plot_reviews_per_user(df: pd.DataFrame):
    plt.hist(df['num_movies_rated'].values)
    plt.savefig('/home/irene/dev/movie-recsys-gcmc/img/eda/reviews_per_user')

if __name__ == '__main__':
    graph = connect_from_file(PATH_CONNECTION)
    plot_reviews_per_user(reviews_per_user(graph))
