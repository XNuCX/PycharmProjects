class Dough:
    def __init__(self, flour_type:str, baking_technique:str, weight:float):
        self._flour_type = flour_type
        self._baking_technique = baking_technique
        self._weight = weight

    def __setattr__(self, key, value):
        if key == "_flour_type":
            if value == "":
                raise ValueError("The flour type cannot be an empty string")
            else:
                self.__dict__[key] = value
        elif key == "_baking_technique":
            if value == "":
                raise ValueError("The baking technique cannot be an empty string")
            else:
                self.__dict__[key] = value
        elif key == "_weight":
            if value <= 0:
                raise ValueError("The weight cannot be less or equal to zero")
            else:
                self.__dict__[key] = value
        return

    @property
    def flour_type(self):
        return self._flour_type

    @flour_type.setter
    def flour_type(self, value):
        if value == "":
            raise ValueError("The flour type cannot be an empty string")
        else:
            self._flour_type = value

    @property
    def baking_technique(self):
        return self._baking_technique

    @baking_technique.setter
    def baking_technique(self, value):
        if value == "":
            raise ValueError("The baking technique cannot be an empty string")
        else:
            self._baking_technique = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        else:
            self._weight = value