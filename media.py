import webbrowser
import urllib2
import json

class Movie():
	
	"""This class stores information about movies""" 

	def __init__(self, movie_title, trailer_youtube):
					
		movie_info = get_data(movie_title)

		self.trailer_youtube_url = trailer_youtube
		self.title = movie_info['Title']
		self.poster_image_url = movie_info['Poster']
		self.year = movie_info['Year']
		self.storyline = movie_info['Plot']

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

def get_data(movie_title):

	"""Get movie data from OMDb API"""

	movie_title = movie_title.replace('_','+')

	if '_' in movie_title:
		movie_title = movie_title.replace('_','+')
	elif ' ' in movie_title:
		movie_title = movie_title.replace(' ','+')		

	url = 'http://www.omdbapi.com/?t=' + movie_title + '=&plot=short&r=json'
	json_obj = urllib2.urlopen(url)

	data = json.load(json_obj)

	return data
