import getdata as gd
import pandas as pd

def read_existing_data():
    """ Returns a pandas Series either containing previous entries or empty """
    try:
        movies_data = pd.read_csv('movies.csv')
    except:
        movies_data = pd.Series()
    return movies_data

def write_data():
    """ Writes the new entries into the 'movies.csv' file """
    movies_data = read_existing_data()
    new_movies = gd.get_movie_titles()
    for movie, rating in new_movies.items():
        movies_data[movie] = rating
    movies_data.to_csv('movies.csv')

write_data()