import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
logging.disable(logging.CRITICAL)

def get_movie_rating(movie_title_selector, yts_parser):
    """ Returns a movie's rating from its title's selector """
    movie_page_link = yts_parser.select(movie_title_selector)[0]['href']
    try:
        movie_page = requests.get(movie_page_link)
    except:
        print('Cannot access to yts.lt. Please check your connexion.')
        return None
    else:
        movie_rating_selector = 'div.rating-row:nth-child(2) > span:nth-child(2)'
        parser = BeautifulSoup(movie_page.text, 'html.parser')
        rating = parser.select(movie_rating_selector)[0].text
        return rating

def get_movie_category(movie_title_selector, yts_parser):
    """ Returns a movie's category from its title's selector """
    movie_page_link = yts_parser.select(movie_title_selector)[0]['href']
    try:
        movie_page = requests.get(movie_page_link)
    except:
        print('Cannot access to yts.lt. Please check your connexion.')
        return None
    else:
        movie_category_selector = 'div.hidden-xs:nth-child(1) > h2:nth-child(3)'
        parser = BeautifulSoup(movie_page.text, 'html.parser')
        category = parser.select(movie_category_selector)[0].text
        return category       

def get_movie_data():
    """ Returns a list of latest YTS movies added """
    movies = {}
    movie_title_selector = 'div.home-content:nth-child(1) > div:nth-child(1) > div:nth-child({}) > div:nth-child({}) > div:nth-child(2) > a:nth-child(1)'
    try:
        yts_page = requests.get('https://yts.lt/')
    except:
        print('Cannot access to yts.lt. Please check your connexion.')
        return None
    else:
        parser = BeautifulSoup(yts_page.text, 'html.parser')
        for i in [2,3]:
            for j in range(1,5):
                movie_title = parser.select(movie_title_selector.format(i,j))[0].text
                movie_score = get_movie_rating(movie_title_selector.format(i,j), parser)
                movie_category = get_movie_category(movie_title_selector.format(i,j), parser)
                movies[movie_title] = [float(movie_score), movie_category]
    return movies

logging.debug(get_movie_data())
