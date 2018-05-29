from Lab2.PetStore import PetStore
from Lab2.Pets.Ant import Ant
from Lab2.Pets.Dog import Dog
from Lab2.Pets.Monkey import Monkey
from Lab2.Pets.Nemo import Nemo


if __name__ == '__main__':
    petstore = PetStore()

    dog = Dog(name='Dog')
    ant = Ant(name='Ant')
    monkey = Monkey(name='Monkey')
    nemo = Nemo(name='Nemo')

    petstore.pets = [dog, ant, monkey, nemo]
    print("Pet list:")
    petstore.print_list()

    petstore.sort_by_price()
    print("Sorted pets by price")
    petstore.print_list()

    ls = petstore.find_pet_by_numberOfFood(numberOfFood=220)
    print("Pet name ")
    for pet in ls:
      print(pet.name)
