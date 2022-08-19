class User:
    def __init__(self,
                 user_id:int,
                 username:str):
        self.user_id = user_id
        self.username = username
        self.books = []

    def info(self):
        books = [book for book in sorted(self.books, key=lambda x: x[0])]
        return ', '.join(books)

    def __str__(self):
        return f"{self.user_id}, {self.username}, {self.books}"

