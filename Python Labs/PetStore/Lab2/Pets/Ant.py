from Lab2.Enums.Accommodation import Accommodation
from Lab2.Enums.Types import Types
from Lab2.Enums.Food import Food
from Lab2.Pet import Pet


class Ant(Pet):

    def __init__(self, name="Ant",  types=Types.INSECTS, price=220, numberOfFood=60, food=Food.FEED, accommodation=Accommodation.TERRARIUM):
        Pet.__init__(self, name, types, price, numberOfFood,  food, accommodation)
        self.types = types
        self.food = food
        self.accommodation = accommodation

    def __str__(self):
        return "Pet called : " + str(self.name) + ", of type " + str(self.types) \
               + ", costs " + str(self.price) + ", eats " + str(self.numberOfFood) \
               + ", of " + str(self.food) + " and lives in " + str(self.accommodation)
