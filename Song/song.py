from __future__ import print_function


class Song:
    """
    Class to represent a song

    Attributes:
              title (str): The title of the song
              artist (str): The artist name of the song
              duration (int): The duration of the song
    """

    def __init__(self, title, artist, duration=0):
        """
        Song init method

        Args:
                title (str): The title of the song
                artist (Artist): The artist of the song
                duration (Optional int): The duration of the song
        """
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "Various"
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, pos=None):
        song_found = find_obj(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
        if pos is None:
            self.tracks.append(song_found)
        else:
            self.tracks.insert(pos, song_found)


class Artist:

    def __init__(self, name):
        self.name = name
        self.songs = []
        self.albums = []

    def add_album(self, album):
        self.albums.append(album) if album not in self.albums else \
            print("Album already in the list!")

    def add_song(self, year, album, song):
        album_found = find_obj(album, self.albums)
        if album_found is None:
            album_found = Album(album, year, self.name)
            self.add_album(album_found)
        album_found.add_song(song)


def find_obj(field, obj_list):
    for item in obj_list:
        if item.name == field:
            return item
    return None


def load_data():
    artists = []
    with open("data/albums.txt", 'r') as f:
        for line in f:
            artist, album, year, song = tuple(line.strip('\n').split('\t'))
            year = int(year)
            new_artist = find_obj(artist, artists)
            if new_artist is None:
                new_artist = Artist(artist)
                artists.append(new_artist)
            new_artist.add_song(album, year, song)
    return artists


def check(artists) -> None:
    with open("data/checkfile.txt", 'w') as f:
        for artist in artists:
            for album in artist.albums:
                for song in album.tracks:
                    print(f"{artist.name}\t{album.name}\t{album.year}\t{song.name}", file=f)


if __name__ == '__main__':
    artists = load_data()
    print(len(artists))
    check(artists)
