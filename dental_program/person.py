from datetime import date, datetime
import re


class Person:

    def __init__(self):
        self.__name = dict
        self.__age = int

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, args: list):
        """
        :format ["fist_name", "last_name"]
        :param args:
        :return:
        """

        def catch(value):
            if type(value) == str:
                return value
            else:
                raise ValueError("Name is not string")

        args = [catch(v).strip() for v in args]
        fst_name, lst_name = args
        self.__name = {"First Name": fst_name, "Last Name": lst_name}

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, birthdate: str):
        """
        :format "mm/dd/yyyy"
        :param birthdate:
        :return:
        """

        def check_date(birthdate_local):
            year_re = r"\d{4}$"
            month_re = r"/\d{2}/"
            day_re = r"^\d{2}"
            try:
                year = int(re.search(year_re, birthdate_local).group())
                month = int(re.search(month_re, birthdate_local).group().strip("/"))
                day = int(re.search(day_re, birthdate_local).group())
                return year, month, day
            except:
                raise ValueError("Incorrect Date format")

        def age_check(birthdate_local):
            today = date.today()
            birthdate = date(*birthdate_local)
            age = today.year - birthdate.year - (
                    (today.month, today.day) < (birthdate.month, birthdate.day))
            if age < 0:
                raise ValueError("Incorrect Age")
            return age

        self.__age = age_check(check_date(birthdate))

a = Person()
a.name = ["Lyubomir", "Lyubenov"]
a.age = "01/01/2020"
print(a.name, a.age)