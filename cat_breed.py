# import base class
from pet_breed import PetBreed

class CatBreed(PetBreed):

    # constructor
    def __init__(self, type, name, size, weight, coat="", energy="", temperament="", lifespan="", colours=""):
        super().__init__(type, name, size, weight, coat, energy, temperament, lifespan)
        self.colours = colours

    def __str__(self):
        return (f"\nid: {self.id} type: {self.type}, name: {self.name}, size: {self.size}, weight: {self.weight}, coat: {self.coat}, energy: {self.energy}, temperament: {self.temperament}, lifespan: {self.lifespan}, colours: {self.colours}")

    def display_breed_info(self):
        return self.__str__()

