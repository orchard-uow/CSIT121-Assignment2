from pet_breed import PetBreed
from cat_breed import CatBreed
from dog_breed import DogBreed

class PetMatch:
    # constructor
    def __init__(self):
        self.pet_store = []

    def add_pet_breed(self, pet):
        '''add pet to pet store'''
        self.pet_store.append(pet)

    def search_pet_breed(self, **kwargs):
        '''search for pets that match an array of atrribute values'''
        pets = []

        for pet in self.pet_store:
            for key, value in kwargs.items():
                # use getAttr() of key in object
                if getattr(pet, key).lower() == value.lower():
                    pets.append(pet)
        # display results
        self.display_search_results(pets)
        # return pets          
        return pets

    def display_search_results(self, pets):   
        # todo: add search title with      
        for pet in pets:
            print(pet.display_breed_info())

    def show_all_pet_breeds(self):
        for pet in self.pet_store:
            print(pet)

    def show_pet_breed(self, name):
        for pet in self.pet_store:
            if pet.name.lower() == name.lower():
                print(pet)
                return pet

    def edit_pet_breed(self, petbreed):
        for pet in self.pet_store:
            if pet.id == petbreed.id:
                pet.name = petbreed.name
                pet.size = petbreed.size
                pet.weight = petbreed.weight
                # add other attributes later
                return

    def delete_pet_breed(self, name):
        for pet in self.pet_store:
            if pet.name.lower() == name.lower():
                self.pet_store.remove(pet)