import webbrowser as wb


class Media():
    """
    Abstract class Media contains information about movie's name, description
    a picture, a trailer link and director name
    Assuming the media is made in USA
    """
    def __init__(self, name, desc, pic, trailer, director):
        self.name = name
        self.desc = desc
        self.pic = pic
        self.trailer = trailer
        self.director = director

    def show_trailer(self):
        wb.open(self.trailer)

    def toString(self):
        return(self.name + " is directed by " + self.director + ".")


class ForeignMovies(Media):
    """
    Inherited from Media class
    Contain a new attribute:
    country: where the movie is originally made from
    """
    def __init__(self, name, desc, pic, trailer, director, country):
        Media.__init__(self, name, desc, pic, trailer, director)
        self.country = country

    def toString(self):
        return (
            self.name + " is originally directed by " +
            self.director + " in " + self.country + ".")


class TVShow(Media):
    """
    Inherited from Media class
    Contain a new attribute: (episodes) number of episodes
    """
    def __init__(self, name, desc, pic, trailer, director, episodes):
        Media.__init__(self, name, desc, pic, trailer, director)
        self.episodes = episodes

    def toString(self):
        return (
            self.name + " is directed by " +
            self.director + " and it has " + str(self.episodes) + ".")
