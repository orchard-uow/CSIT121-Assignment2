# import base class
from pet_breed import PetBreed

class DogBreed(PetBreed):

    sizes = PetBreed.sizes + ['giant']
    coats = PetBreed.coats + ['double', 'wiry', 'smooth', 'rough']

    # constructor
    def __init__(self, type, name, size, weight, coat="", energy="", temperament="", lifespan="", activities=""):
        super().__init__(type, name, size, weight, coat, energy, temperament, lifespan)
        
        self.activities = activities

    def __str__(self):
        return (f"\nid: {self.id} type: {self.type}, name: {self.name}, size: {self.size}, weight: {self.weight}, coat: {self.coat}, energy: {self.energy}, temperament: {self.temperament}, lifespan: {self.lifespan}, activities: {self.activities}"
)
    def display_breed_info(self):
        return self.__str__()

