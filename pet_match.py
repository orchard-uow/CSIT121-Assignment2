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

        # check if kwargs is empty
        if kwargs == {}:
            print("No pet breeds match this search criteria")
            return

        for pet in self.pet_store:
            match =True
            for key, value in kwargs.items():
                if getattr(pet, key).lower()  != value.lower():
                    match = False
                    break
            if match:
                pets.append(pet)

        self.display_search_results(pets)

        

    def display_search_results(self, pets):       
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