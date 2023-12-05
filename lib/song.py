class Song:

    genres = []
    artists = []
    count = 0
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls, increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)
    
    @classmethod
    def add_to_genre_count(cls, genre):
        for i in cls.genres:
            if genre == i:
                cls.genre_count[i] = cls.genre_count.get(i, 0) + 1
                return 
        
        new_pair = {genre: 1}
        cls.genre_count.update(new_pair)

    @classmethod
    def add_to_artist_count(cls, artist):
        for i in cls.artists:
            if artist == i:
                cls.artist_count[i] = cls.artist_count.get(i, 0) + 1
                return
        new_pair = {artist: 1}
        cls.artist_count.update(new_pair)


