import getdata as gd
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
# logging.disable(logging.CRITICAL)

def read_existing_data():
    """ Returns a pandas Series either containing previous entries or empty """
    try:
        movies_data = pd.read_csv('movies.csv', index_col=0)
    except:
        movies_data = pd.DataFrame(columns=['Movie','Rating','Category'])
    return movies_data

def write_data():
    """ Writes the new entries into the 'movies.csv' file """
    movies_data = read_existing_data()
    new_movies = gd.get_movie_data()
    for movie, rating_category in new_movies.items():
        if movie not in movies_data['Movie'].values:
            new_row = [movie, rating_category[0], rating_category[1]]
            movies_data.loc[-1] = new_row
            movies_data.index += 1
    movies_data.to_csv('movies.csv')

logging.debug(write_data())