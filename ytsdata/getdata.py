import logging
import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
# logging.disable(logging.CRITICAL)

def get_movie_titles():
    """ Returns a list of latest YTS movies added """
    movies_titles = []
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
                movies_titles.append(parser.select(movie_title_selector.format(i,j))[0].text)
    return movies_titles

logging.debug(get_movie_titles())