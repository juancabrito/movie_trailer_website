import webbrowser
import urllib2
import json


class Movie():

    """An object to store information about a movie, including:
    title, year, poster image, storyline."""

    def __init__(self, movie_title, trailer_youtube):

        movie_info = get_data(movie_title)
        self.trailer_youtube_url = trailer_youtube
        self.title = movie_info['Title']
        self.poster_image_url = movie_info['Poster']
        self.year = movie_info['Year']
        self.storyline = movie_info['Plot']

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


# Helper to get info about the movie
def get_data(movie_title):

    """This function gets movie data from OMDb API
    by providing the title as parameter.
    Returns info as a JSON object."""

    # Fix the movie title replacing spaces for the API call
    movie_title = movie_title.replace('_', '+')
    if '_' in movie_title:
        movie_title = movie_title.replace('_', '+')
    elif ' ' in movie_title:
        movie_title = movie_title.replace(' ', '+')

    url = 'http://www.omdbapi.com/?t=' + movie_title + '=&plot=short&r=json'
    json_obj = urllib2.urlopen(url)

    data = json.load(json_obj)

    return data
