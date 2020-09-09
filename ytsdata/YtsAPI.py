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
    def movie_detail(movie_id, with_images=false, with_cast=false):
        request = requests.get(
            f"https://yts.mx/api/v2/movie_details.json?movie_id={movie_id}&with_images={with_images}&with_cast={with_cast}"
        ).json()
        assert request["status"] == 'ok'
        return request["data"]

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