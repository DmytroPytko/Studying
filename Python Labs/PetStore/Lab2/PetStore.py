class PetStore:
    pets = {}

    def __init__(self):
        pass

    def sort_by_price(self):
        self.pets.sort(key=lambda pet: pet.price)

    def find_pet_by_type_sorted_by_food_type(self, types):
        found_pet = []
        for pet in self.pets:
            if pet.types == types:
                found_pet.append(pet)
        return found_pet

    def sort_by_number_of_food(self):
        self.pets.sort(key=lambda pet: pet.numberOfFood)

    def find_pet_by_numberOfFood(self, numberOfFood):
        found_pet = []
        for pet in self.pets:
            if pet.numberOfFood == numberOfFood:
                found_pet.append(pet)
                return found_pet

    def add_pet(self, pet):
        self.pets += pet

    def print_list(self):
        for pet in self.pets:
            print(pet)
        print("\n")
