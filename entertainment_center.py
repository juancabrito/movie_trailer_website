import fresh_tomatoes
import media


"""Instances of a movie. Title and trailer URL required"""

# URL of the trailer because it is not provided by OMDb

v_for_vendetta = media.Movie(
    "V for Vendetta",
    "https://youtu.be/qxyUl9M_7vc")
almost_famous = media.Movie(
    "Almost Famous",
    "https://youtu.be/qk0XnyrENrE")
closer = media.Movie(
    "Closer",
    "https://youtu.be/MdCc_NBlQC4")
dogville = media.Movie(
    "Dogville",
    "https://youtu.be/J5-LqwUHTaM")
snatch = media.Movie(
    "Snatch",
    "https://youtu.be/ni4tEtuTccc")
paris_texas = media.Movie(
    "Paris Texas",
    "https://www.youtube.com/watch?v=9e590FeeGCM")
taxi_driver = media.Movie(
    "Taxi Driver",
    "https://youtu.be/UUxD4-dEzn0")
fear_loathing_las_vegas = media.Movie(
    "Fear and loathing in Las Vegas",
    "https://youtu.be/Zm7r491n-8o")
fight_club = media.Movie(
    "Fight Club",
    "https://youtu.be/D3Yw9Yc1YmY")
babel = media.Movie(
    "Babel",
    "https://youtu.be/gzrHrTVaqJs")
american_beauty = media.Movie(
    "American Beauty",
    "https://youtu.be/3ycmmJ6rxA8")
lemony_snicket = media.Movie(
    "A series of Unfortunate Events",
    "https://youtu.be/fccho1IyX8Y")


movies = [v_for_vendetta, almost_famous, closer, dogville,
          snatch, paris_texas, taxi_driver, fear_loathing_las_vegas,
          fight_club, babel, american_beauty, lemony_snicket]

fresh_tomatoes.open_movies_page(movies)
