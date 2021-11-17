import datetime
class DVD:
    def __init__(self, name:str, id:int, creation_year:int,
                 creation_month:str, age_restriction: int):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False
    @staticmethod
    def from_date(id: int, name: str, date: str, age_restriction: int):
        day, creation_month, creation_year = date.split(".")
        month = datetime.date(int(creation_year), int(creation_month), int(day)).strftime('%B')

        return DVD(name, id, int(creation_year), month, age_restriction)

    def __repr__(self):
        if self.is_rented:
            status = "rented"
        else:
            status = "not rented"


        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {status}"