import webbrowser


class Movie():
    def __init__(self, movie_title, storyline, movie_poster, movie_trailer):
        """
        initializes the info for each card with all of the info

        :param movie_title: title of movie
        :param storyline: storyline of movie
        :param movie_poster: poster for movie
        :param movie_trailer: youtube trailer for movie
        """
        self.title = movie_title
        self.storyline = storyline
        self.poster_img = movie_poster
        self.youtube_trailer = movie_trailer

    def show_trailer(self):
        """
        uses webbrowser to open youtube_trailer and display in browser
        :return: nothing
        """
        webbrowser.open(self.youtube_trailer)
