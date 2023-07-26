class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.song_counter()
        Song.song_genres(genre)
        Song.song_artists(artist)
        Song.song_genre_count(genre)
        Song.song_artist_count(artist)

    @classmethod
    def song_counter(cls):
        cls.count += 1

    @classmethod
    def song_genres(cls, genre):
        cls.genres.append(genre)

    @classmethod
    def song_artists(cls, artist):
        cls.artists.append(artist)

    @classmethod
    def song_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def song_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1

    pass
