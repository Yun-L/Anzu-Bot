'''

Author: Yun

'''

from abc import ABC, abstractmethod


class Song(ABC):

    def __init__(self, song_location, origin_ctx):
        self.song_location = song_location
        self.origin_ctx = origin_ctx
        super().__init__()

    @abstractmethod
    def get_song_name(self):
        pass

    @abstractmethod
    def get_entry_text(self):
        pass

    @abstractmethod
    def get_finish_text(self):
        pass


class LocalSong(Song):

    def __init__(self, song_location, origin_ctx):
        super().__init__(song_location, origin_ctx)

    def get_song_name(self):
        song_name = self.song_location

        if song_name.endswith(".mp3"):
            song_name = song_name.replace(".mp3", "")

        return song_name.replace("_", " ")

    def get_entry_text(self):
        s = "Now Playing: {}".format(self.get_song_name())
        return s

    def get_finish_text(self):
        s = "Finished Playing: {}".format(self.get_song_name())
        return s


class YoutubeSong(Song):

    def __init__(self, song_location, origin_ctx):
        super().__init__(song_location, origin_ctx)

    def get_song_name(self):
        return "Youtube Song Name"

    def get_entry_text(self):
        return "get_entry_text YoutubeSong Entry"

    def get_finish_text(self):
        return "get_finish_text YoutubeSong Finish"


class UrlSong(Song):

    def __init__(self, song_location, origin_ctx):
        super().__init__(song_location, origin_ctx)

    def get_song_name(self):
        return "Url song name"

    def get_entry_text(self):
        return "get_entry_text UrlSong Entry"

    def get_finish_text(self):
        return "get_finish_text UrlSong Entry"


if __name__ == "__main__":

    # testing

    local = LocalSong("Venetian_Snares-Szamar_Madar.mp3", None)
    print(type(local))
    print(local.get_song_name())
    print(local.get_entry_text())
    print(local.get_finish_text())
    
    local2 = LocalSong("REOL-Detarame_Kidding", None)
    print(type(local2))
    print(local2.get_song_name())
    print(local2.get_entry_text())
    print(local2.get_finish_text())

    yt = YoutubeSong("youtubesong", None)
    print(type(yt))
    print(yt.get_song_name())
    print(yt.get_entry_text())
    print(yt.get_finish_text())

    url = UrlSong("urlsong", None)
    print(type(url))
    print(url.get_song_name())
    print(url.get_entry_text())
    print(url.get_finish_text())
