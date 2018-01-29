import webbrowser
import os
import re

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 4 -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/css/bootstrap.min.css">
    <link rel="stylesheet" href="style.css">
    <link href='https://fonts.googleapis.com/css?family=Oswald' rel='stylesheet'>
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.3/js/bootstrap.min.js"></script>
    <script src="script.js"></script>
    
</head>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    
    <!-- Main Page Content -->
    <div class="container">
      <nav class="navbar navbar-dark bg-dark fixed-top">
            <a class="navbar-brand" href="#">Fresh Tomatoes</a>
        </nav>
    </div>
    <div class="container">
        <div class="row">
            {movie_cards}
        </div>
    </div>
  </body>
</html>
'''

# each card contains a front with poster & title and flips to back to show storyline & button for movie trailer modal
movie_cards = '''
        <div class="col-sm">
            <div class="card-container">
                <div class="card">
                    <div class="side"><img src="{poster_img}" width="220" height="342" style="padding-top: 8px; padding-bottom: 8px" alt="card img">
                        <h3 class="movie_title">{movie_title}</h3>
                    </div>
                    <div class="side back"> 
                        <span class="storyline"> {storyline} </span>
                        <div class="button">
                            <button type="button" class="btn btn-dark" data-toggle="modal" data-src="https://www.youtube.com/embed/zLAhRiUeJ8E" data-target="#myModal{counter}">Movie Trailer</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        

        <div id="myModal{counter}" class="modal fade bd-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
          <div class="modal-dialog modal-lg">
            <div class="modal-content">
              <iframe id="myFrame{counter}" width="560" height="315" src="{trailer_youtube_id}" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen allowscriptaccess="always"></iframe>
            </div>
          </div>
        </div>
'''


def create_movie_card_content(movies):
    # The HTML content for this section of the page
    content = ''
    counter = 0
    for movie in movies:

        # Append the tile for the movie with its content filled in
        content += movie_cards.format(
            movie_title=movie.title,
            poster_img=movie.poster_img,
            trailer_youtube_id=movie.youtube_trailer,
            storyline=movie.storyline,
            counter=counter
        )
        counter += 1
    return content


def open_movies_page(movies_list):
  # Create or overwrite the output file
  output_file = open('fresh_tomatoes.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  rendered_content = main_page_content.format(movie_cards=create_movie_card_content(movies_list))

  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible
