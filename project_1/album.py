from .song import Song
class Album:
    def __init__(self, name:str, *args):
        self.name = name
        self.songs = [_ for _ in args]
        self.published = False

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        elif self.published:
            return "Cannot add songs. Album is published."
        elif song.name in [s.name for s in self.songs if self.songs]:
            return "Song is already in the album."
        else:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        elif song_name not in [n.name for n in self.songs if self.songs]:
            return "Song is not in the album."
        else:
            for i, n in enumerate(self.songs):
                if n.name == song_name:
                    return f"Removed song {self.songs.pop(i).name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        songs = "\n".join([f"== {s.get_info()}" for s in self.songs if self.songs])
        return f"Album {self.name}\n{songs}"


