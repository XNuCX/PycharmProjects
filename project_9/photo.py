class PhotoAlbum:
    def __init__(self, pages:int):
        self.pages = pages
        self.photos = [list() for _ in range(pages)]
    @staticmethod
    def from_photos_count(photos_count:int):
        if photos_count % 4 == 0:
            pages_count = photos_count / 4
        else:
            pages_count = photos_count // 4 + 1

        album = PhotoAlbum(int(pages_count))
        # PhotoAlbum.photos = [list() for _ in range(int(pages_count))]
        return album

    def add_photo(self, label:str):
        for i, page in enumerate(self.photos):
            if len(page) == 4:
                if i + 1 == len(self.photos):
                    return "No more free slots"
                else:
                    continue
            else:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(page)}"


        return "No more free slots"

    def display(self):
        pages = '\n-----------\n'.join([" ".join("[]" for _ in page) for page in self.photos])

        return f"-----------\n{pages}\n-----------"

album = PhotoAlbum(2)
album_1 = album.from_photos_count(12)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.photos)
print(album.display())
print(album_1.display())
print(album_1.photos)