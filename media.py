"""This is my docstring"""
import webbrowser

class Movie(object):
    """This class is used to creates movie objects"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        """This method is used to open the youtube video in the modal"""
        webbrowser.open(self.trailer_youtube_url)
