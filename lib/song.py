class Song:
    """
    A class to represent a song in a music library system.
    Tracks individual song details and maintains global insights
    across all songs created.
    """

    # Class attributes - shared across all Song instances
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        """
        Initialize a new song.
        name: title of the song
        artist: name of the artist
        genre: genre of the song
        """
        self.name = name
        self.artist = artist
        self.genre = genre

        # Trigger all class methods when a new song is created
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    @classmethod
    def add_song_to_count(cls):
        """Increments the total song count by 1."""
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        """
        Adds genre to genres list.
        Ensures no duplicates.
        """
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        """
        Adds artist to artists list.
        Ensures no duplicates.
        """
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        """
        Updates genre_count dictionary.
        Increments genre key by 1, or sets to 1 if new.
        """
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        """
        Updates artist_count dictionary.
        Increments artist key by 1, or sets to 1 if new.
        """
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

    def __repr__(self):
        """String representation of a song."""
        return f"Song: {self.name} | Artist: {self.artist} | Genre: {self.genre}"