import webbrowser
import urllib2
import json


class Movie():

    """An object to store information about a movie, including:
    title, year, poster image, storyline."""

    def __init__(self, movie_title, trailer_youtube):

        movie_info = get_data(movie_title)

        self.trailer_youtube_url = trailer_youtube
        ## Old from OMDB ##
        #self.title = movie_info['Title']
        #self.poster_image_url = movie_info['Poster']
        #self.year = movie_info['Year']
        #self.storyline = movie_info['Plot']

        # TODO: New from TMDB
        self.title = movie_info['title'].encode("utf-8")
        poster_image_url = movie_info['poster_path']
        self.poster_image_url = 'https://image.tmdb.org/t/p/w396/' + poster_image_url
        self.year = movie_info['release_date'][:4]
        storyline = movie_info['overview'].encode("utf-8")
        self.storyline = (storyline[:240] + ' ...') if len(storyline) > 75 else storyline

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

    ## Old OMBD API ##
    #url = 'http://www.omdbapi.com/?t=' + movie_title + '=&plot=short&r=json'
    #json_obj = urllib2.urlopen(url)

    # TODO: Get just the first result from the response
    key = '32bb75d541975c79c4ec558c051aaa3d'
    url = 'http://api.themoviedb.org/3/search/movie?query=' + movie_title + '&api_key=' + key
    json_obj = urllib2.urlopen(url)

    data = json.load(json_obj)
    data = data['results'][0]

    return data
