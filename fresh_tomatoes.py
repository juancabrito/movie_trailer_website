import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/twitter-bootstrap/3.1.0/js/bootstrap-tooltip.js"></script>

    <!-- Couple of fonts for the main title! -->
    <link href='http://fonts.googleapis.com/css?family=Slabo+27px' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Pacifico' rel='stylesheet' type='text/css'>

    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-image: url(bg_vault.png);
            background-size: 1500px;
            background-position: center 88px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 95%;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }

        /* === Standard DVD background image === */
        .movie-tile {
            margin: 33px 46px;
            padding-top: 8px;
            background: transparent url(dvd.png) no-repeat center top;
            background-size: contain;
            height: 250px;
            position: relative;
            width: 189px;
        }
        /* ================ */

        /* === Poster image as DVD cover, with more info on a label === */
        /* === Label will only be shown on mouse over                   */
        .movie-tile .poster-img {
          background-repeat:no-repeat;
          background-position: center top;
          background-size: cover;
          width: 159px;
          height: 223px;
          position: absolute;
          left: 6px;
          -webkit-border-top-right-radius: 4px;
          -webkit-border-bottom-right-radius: 4px;
          -moz-border-radius-topright: 4px;
          -moz-border-radius-bottomright: 4px;
          border-top-right-radius: 4px;
          border-bottom-right-radius: 4px;
        }
        .movie-tile .movie-label {
          position: absolute;
          font-size: 14px;
          font-family: 'Slabo 27px', serif;
          color: #fff;
          text-align: center;
          background: rgba(50,50,50,0.9) url('bg_label.png') repeat-x left top;
          padding: 20px 10px 10px;
          bottom: 0.5em;
          left: 0;
          right: 0;
          margin: 0 auto;
          width: 190px;
          border-bottom: 1px solid #000;
          display: none;
        }
        .movie-tile:hover .movie-label {
          display: block;
        }
        .movie-tile:hover {
            cursor: pointer;
        }
        /* ================ */

        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }

        /* === Complements === */
        .navbar {
            border-bottom: solid 2px #d59256;
        }
        .navbar-header {
            height: 85px; text-align: center; margin: 0 auto; float: none;
        }
        .navbar-header h1 {
            margin: 10px 0 3px; padding: 0; color: #fff; font-size: 2.3em;font-family: 'Slabo 27px', serif;
        }
        .navbar-header h2 {
            margin: 0; color: #fff; font-size: 1.7em; font-family: 'Pacifico', cursive; color: #d59256;
        }
        .tooltip {
            font-family: Arial, Helvetica, sans-serif;
            width: 100%;
        }
        .tooltip .tooltip-inner {
            text-align: left; padding: 10px;
        }
        .footer {
            padding: 10px 0; text-align: center; color: #ead1b5; font-size: 11px;
        }
        /* ================ */

        /* === A small adjustment to keep responsiveness === */
        @media (min-width: 1000px) {
          #trailer .modal-dialog {
              margin-top: 100px;
              width: 85%;
          }
        }
        /* ================ */

    </style>

    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });

        // Initialize tooltips
        $(function () {
          $('[data-toggle="tooltip"]').tooltip()
        })
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <h1>Movie Trailers Online</h1>
            <h2>Juancabrito's favorites</h2>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
    <div class="footer">
      <img src="https://assets.tmdb.org/images/logos/var_1_0_PoweredByTMDB_Blk_Antitled.png" width="150px" />
      <br />
      Thanks to: PSDcovers.com
    </div>
  </body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-4 col-lg-3 col-sm-6 col-xs-6 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <div class="poster-img" style="background-image: url({poster_image_url});"></div>
    <h2 class="movie-label">{movie_title} ({movie_year}) &nbsp;&nbsp; <span class="glyphicon glyphicon glyphicon-info-sign" data-toggle="tooltip" data-placement="top" title="{movie_plot}"></span></h2>
</div>
'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_year=movie.year,
            poster_image_url=movie.poster_image_url,
            movie_plot=movie.storyline,
            trailer_youtube_id=trailer_youtube_id
        )
    return content

def open_movies_page(movies):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
