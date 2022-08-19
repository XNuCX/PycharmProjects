from project_20.user import User


class Library:
    def __init__(self):
        self.user_records = []
        self.__books_available = {}
        self.__rented_books = {}

    @property
    def books_available(self):
        return self.__books_available
    @books_available.setter
    def books_available(self, book:dict):
        for key, value in book.items():
            if self.__books_available[key] in self.__books_available:
                self.__books_available[key].append(value)
            else:
                self.__books_available.update({key: value})

    @property
    def rented_books(self):
        return self.__rented_books
    @rented_books.setter
    def rented_books(self, information:dict ):
        for key, value in information.items():
            self.__rented_books[key].update(value)


    def get_book(self,
                 author:str,
                 book_name:str,
                 days_to_return:int,
                 user: User):
        if [True for book in self.rented_books.values() if book_name in book.keys()]:
            days = 0
            for value in self.rented_books.values():
                for k, v in value.items():
                    if k == book_name:
                        days = v
                        break

            return f'The book "{book_name}" is already rented and will be available in {days} days!'
        elif book_name in self.books_available[author]:
            if user.username in self.rented_books.keys():
                self.rented_books[user.username].update({book_name: days_to_return})
            else:
                self.rented_books[user.username] = {book_name: days_to_return}
            # self.books_available[author] = [book for book in self.books_available[author] if book_name not in book]
            for i, book_1 in enumerate(self.books_available[author]):
                if book_name == book_1:
                    self.books_available[author].pop(i)
                    break
            for u in self.user_records:
                if user.user_id == u.user_id:
                    u.books.append(book_name)
            return f"{book_name} successfully rented for the next {days_to_return} days!"
        else:
            return


    def return_book(self,
                    author:str,
                    book_name:str,
                    user:User):

        if book_name in self.rented_books[user.username].keys():
            del self.rented_books[user.username][book_name]
            self.books_available[author].append(book_name)
            user.books = [books for books in user.books if not book_name == books]
            return
        else:
            return f"{user.username} doesn't have this book in his/her records!"



