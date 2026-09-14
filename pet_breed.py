from abc import ABC, abstractmethod

# import custom exceptions
from exceptions import InvalidSizeError

class PetBreed(ABC):
    # class variables
    next_pet_id = 1
    type = ['cat', 'dog']
    sizes = ['small', 'medium', 'large']
    coats = ['hairless', 'short', 'medium', 'long']

    # constructor
    def __init__(self, type, name, size, weight, coat="", energy="", temperament="", lifespan=""):
        self.id = self.next_pet_id
        self.next_pet_id += 1
        self.type = type
        self.name = name
        self.size = size
        self.weight = weight
        self.coat = coat
        self.energy = energy
        self.temperament = temperament
        self.lifespan = lifespan

        # these validation tests may be better handled in menu with exceptions
        # if self.size.lower() not in self.sizes:
        #     raise InvalidSizeError("Not an accepted size")      
        
    @abstractmethod
    def display_breed_info(self):
        pass