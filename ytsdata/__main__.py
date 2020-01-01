import storedata
import pandas as pd
from selenium import webdriver


def display_movies(movie_df):
    """ Displays: <index>-<Movie Title> """
    for i in range(len(movie_df.index)):
        print('{}-{}'.format(i, movie_df['Movie'].loc[i]))

def download_movie(movie_df):
    """ Asks the user to enter the index of the movie to download """
    ind_movie = int(input('Which movie do you want to download?: '))
    dl_link = movie_df['720p.BluRay'].loc[ind_movie]
    browser = webdriver.Firefox()
    browser.get(dl_link)

if __name__ == "__main__":
    storedata.write_data()
    movies = pd.read_csv("movies.csv", index_col=0)

    display_movies(movies)
    download_movie(movies)