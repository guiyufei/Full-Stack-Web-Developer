import webbrowser

class Movie:
    """This is a class describing the attribute of some of the hottest movies.
       There will be movie title, poster image link, short description and
       a trailer video link.
       There will also be some functions related to build the movie website.
    """
    def __init__(self, title, description, poster, trailer_link):
        self.title=title
        self.storyline=description
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer_link

    # a function to open the trailer on the website
    
    def show_trailer(self):
        webbrowser.open(trailer_youtube_url)
        
