from abc import ABC, abstractmethod

class PetBreed(ABC):
    # class variables
    next_pet_id = 1
    type = ['cat', 'dog']
    sizes = ['small', 'medium', 'large']
    coats = ['hairless', 'short', 'medium', 'long']

    # constructor
    def __init__(self, type, name, size, weight, coat, energy, temperament, lifespan):
        self.type = type
        self.name = name
        self.size = size
        self.weight = weight
        self.coat = coat
        self.energy = energy
        self.temperament = temperament
        self.lifespan = lifespan

    @abstractmethod
    def display_breed_info(self):
        pass