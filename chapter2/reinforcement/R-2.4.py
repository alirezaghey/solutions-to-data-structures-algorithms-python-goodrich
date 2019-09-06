# R-2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its num-
# ber of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.


class Flower:
    """A flower"""

    def __init__(self: Flower, name: str, numOfPetals: int, price: float):
        """Creates a new Flower instance"""
        self._name = name
        self._numOfPetals = numOfPetals
        self._price = price

# setter methods
    def set_name(self: Flower, name: str) -> None:
        self._name = name

    def set_numOfPetals(self: Flower, numOfPetals: int) -> None:
        self._numOfPetals = numOfPetals

    def set_price(self: Flower, price: float) -> None:
        self._price = price

# getter methods
    def get_name(self: Flower) -> str:
        return self._name

    def get_numOfPetals(self: Flower) -> int:
        return self._numOfPetals

    def get_price(self: Flower) -> float:
        return self._price
