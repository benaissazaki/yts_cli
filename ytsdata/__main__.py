import storedata
import pandas as pd
import numpy as np
from selenium import webdriver

def display_movies(movie_df):
    """ Displays: <index>-<Movie Title> """
    for i in range(len(movie_df.index)):
        print('{}-{}'.format(i, movie_df['Movie'].loc[i]))

def available_quality(movie_df, movie_ind):
    """ Returns dictionary with available qualities from movie's index"""
    qualities = ['720p.BluRay', '1080p.BluRay', '720p.WEB', '1080.WEB']
    i = 1
    qual_dict = {}
    for quality in qualities:
        if movie_df[quality].loc[movie_ind] is not np.nan:
            qual_dict[i] = quality
            i += 1
    return qual_dict 

def prompt_quality(movie_df, movie_ind):
    qual_dict = available_quality(movie_df, movie_ind)
    for ind, qual in qual_dict.items():
        print('{}-{}'.format(ind, qual))
    ind_to_dl = int(input('\nChoose quality: '))
    return qual_dict.get(ind_to_dl)

def download_movie(movie_df):
    """ Asks the user to enter the index of the movie to download """
    movie_ind = int(input('\nWhich movie do you want to download?: '))
    qual = prompt_quality(movie_df, movie_ind)
    dl_link = movie_df[qual].loc[movie_ind]
    browser = webdriver.Firefox()
    browser.get(dl_link)

if __name__ == "__main__":
    storedata.write_data()
    movies = pd.read_csv("movies.csv", index_col=0)

    display_movies(movies)
    download_movie(movies)