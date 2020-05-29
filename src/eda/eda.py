from src.neo4j.utils import connect_from_file, query_graph
from py2neo import Graph
import jupyter

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PATH_CONNECTION = '/home/irene/dev/movie-recsys-gcmc/env/neo4j_connection.json'

def plot_reviews_per_user(graph):

    def reviews_per_user(graph: Graph) -> pd.DataFrame:
        query = """
        MATCH (u:User)--(m:Movie)
        RETURN u.userId as user, size(collect(m.title)) as num_movies_rated
        """
        result = query_graph(graph, query).to_data_frame()
        return result

    df = reviews_per_user(graph)
    plt.hist(df['num_movies_rated'].values)
    plt.ylabel('#movies rated')
    plt.title('Histogram: how many movies have each user rated')
    plt.savefig('/home/irene/dev/movie-recsys-gcmc/img/eda/reviews_per_user')

def mean_rating_per_user(graph):
    query = """
    MATCH (u:User)-[r:RATED]-(m:Movie)
    
    """

if __name__ == '__main__':
    graph = connect_from_file(PATH_CONNECTION)
    plot_reviews_per_user(graph)
