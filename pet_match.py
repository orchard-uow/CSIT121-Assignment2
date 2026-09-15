from pet_breed import PetBreed
from cat_breed import CatBreed
from dog_breed import DogBreed

class PetMatch:
    # constructor
    def __init__(self):
        self.pet_store = []

    # todo: dev tests to implete CRUD
    def add_pet(self, pet):
        '''add pet to pet store'''
        self.pet_store.append(pet)
       
    # needs fixing to store keys that matched as well 
    def search_pet(self, searchTerm):
        pets = []
        for pet in self.pet_store:
            for value in vars(pet).values():
                if searchTerm.lower() == str(value).lower():
                    pets.append(pet)
                    
        self.display_search_results(searchTerm, pets)
          
    def display_search_results(self, searchTerm, results):   
        print(f'Search term:{searchTerm}')
             
        for pet in results:
            print(pet.display_breed_info())