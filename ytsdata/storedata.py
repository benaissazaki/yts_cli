import getdata as gd
import pandas as pd
import logging


def read_existing_data():
    """ Returns a pandas Series either containing previous entries or empty """
    try:
        movies_data = pd.read_csv('movies.csv', index_col=0)
    except:
        movies_data = pd.DataFrame(columns=['Movie','Rating','Category', '720p.BluRay', '1080p.BluRay', '720p.WEB', '1080.WEB'])
    return movies_data

def write_data():
    """ Writes the new entries into the 'movies.csv' file """
    movies_data = read_existing_data()
    new_movies = gd.get_movie_data()
    for movie, rating_category_quality in new_movies.items():
        if movie not in movies_data['Movie'].values:
            new_row = [movie, rating_category_quality[0], rating_category_quality[1],
                        rating_category_quality[2].get('720p.BluRay'),
                        rating_category_quality[2].get('1080p.BluRay'),
                        rating_category_quality[2].get('720p.WEB'),
                        rating_category_quality[2].get('1080p.WEB')]
            movies_data.loc[-1] = new_row
            movies_data.index += 1
    movies_data.to_csv('movies.csv')

if __name__ == "__main__":
    
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
    # logging.disable(logging.CRITICAL)
    logging.debug(write_data())