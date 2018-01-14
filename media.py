import webbrowser


class Movie():
    def __init__(self, movie_title, storyline, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = storyline
        self.poster_img = movie_poster
        self.youtube_trailer = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)
