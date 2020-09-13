import requests

class YtsAPI():
    @staticmethod
    def list_movies(limit=20, page=1, quality="",
                    minimum_rating=0, query_term="", genre="",
                    sort_by="date_added", order_by="desc", with_rt_ratings=False):
        request = requests.get(
            f"https://yts.mx/api/v2/list_movies.json?limit={limit}&page={page}&quality={quality}&minimum_rating={minimum_rating}&query_term={query_term}&genre={genre}&sort_by={sort_by}&order_by={order_by}&with_rt_ratings={with_rt_ratings}"
        ).json()
        # {status, status_message, data:
        #      {'movie_count', 'limit', 'page_number', 'movies':
        #          {'id', 'url', 'imdb_code', 'title', 'title_english',
        #              'title_long', 'slug', 'year', 'rating', 'runtime',
        #              'genres', 'summary', 'description_full', 'synopsis',
        #              'yt_trailer_code', 'language', 'mpa_rating', 'background_image',
        #              'background_image_original', 'small_cover_image', 'medium_cover_image',
        #              'large_cover_image', 'state', 'torrents', 'date_uploaded', 'date_uploaded_unix'
        #          }
        #      },
        # @meta
        # }
        assert request["status"] == 'ok'
        return request["data"]

    @staticmethod
    def movie_detail(movie_id, with_images=False, with_cast=False):
        request = requests.get(
            f"https://yts.mx/api/v2/movie_details.json?movie_id={movie_id}&with_images={with_images}&with_cast={with_cast}"
        ).json()
        assert request["status"] == 'ok'
        return request["data"]["movie"]

    @staticmethod
    def movie_suggestions(movie_id):
        request = requests.get(
            f"https://yts.mx/api/v2/movie_suggestions.json?movie_id={movie_id}"
        ).json()
        assert request["status"] == 'ok'
        return request["data"]

    @staticmethod
    def movie_reviews(movie_id):
        request = requests.get(
            f"https://yts.mx/api/v2/movie_reviews.json?movie_id={movie_id}"
        ).json()
        assert request["status"] == 'ok'
        return request["data"]

    @staticmethod
    def display_list(limit=20, page=1, quality="",
                    minimum_rating=0, query_term="", genre="",
                    sort_by="date_added", order_by="desc", with_rt_ratings=False):

        p = page
        while True:
            for movie in YtsAPI.list_movies(limit, p, quality, minimum_rating, query_term, genre, sort_by, order_by, with_rt_ratings)["movies"]:
                    print(f"{movie['id']} \t {movie['title']} \n {movie['rating']} \t {movie['genres']}\n")
            p += 1
            cont = input(f"Do you want to see page number {p}? (y/n) ")
            if cont == "n":
                break

    @staticmethod
    def display_detail(id):
        movie = YtsAPI.movie_detail(id)
        print(f"\n\nId: {movie['id']}\nTitle: {movie['title']}({movie['year']})\nRating: {movie['rating']}\nGenres: {movie['genres']}\nLanguage: {movie['language']}\nDescription: {movie['description_full']}\n\n")

if __name__ == "__main__":
    YtsAPI.display_list()