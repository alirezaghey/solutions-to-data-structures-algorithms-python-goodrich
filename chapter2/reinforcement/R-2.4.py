# R-2.4 Write a Python class, Flower, that has three instance variables of type str,
# int, and float, that respectively represent the name of the flower, its num-
# ber of petals, and its price. Your class must include a constructor method
# that initializes each variable to an appropriate value, and your class should
# include methods for setting the value of each type, and retrieving the value
# of each type.


class Flower:
    """A flower"""

    def __init__(self, name: str, numOfPetals: int, price: float):
        """Creates a new Flower instance"""
        self._name = name
        self._numOfPetals = numOfPetals
        self._price = price

# setter methods
    def set_name(self, name: str) -> None:
        self._name = name

    def set_numOfPetals(self, numOfPetals: int) -> None:
        self._numOfPetals = numOfPetals

    def set_price(self, price: float) -> None:
        self._price = price

# getter methods
    def get_name(self) -> str:
        return self._name

    def get_numOfPetals(self) -> int:
        return self._numOfPetals

    def get_price(self) -> float:
        return self._price

# Overriding builtin methods
    def __str__(self):
        return self.get_name() + " has " + str(self.get_numOfPetals()) + " petals and costs " + str(self.get_price()) + " imaginary units."


# Tests
if __name__ == "__main__":
    flower = Flower("Abracadabra", 13, 953.78)
    print(flower)
    flower.set_price(54.3)
    print(flower)
    flower.set_name("newName")
    flower.set_numOfPetals(345)
    print(flower)
    print(flower.get_name(), flower.get_numOfPetals(), flower.get_price())
