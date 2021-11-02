from .song import Song
from .album import Album
class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        else:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        if album_name in [n.name for n in self.albums]:
            if [n for n in self.albums if n.published and n.name == album_name]:
                return f"Album has been published. It cannot be removed."
            else:
                index = [i for i, n in enumerate(self.albums) if n.name == album_name][0]
                del self.albums[index]

                return f"Album {album_name} has been removed."
        else:
            return f"Album {album_name} is not found."

    def details(self):
        album_details = "\n".join([a.details() for a in self.albums if self.albums])
        return f"Band {self.name}\n{album_details}"



