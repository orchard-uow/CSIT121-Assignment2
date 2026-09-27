from pet_breed import PetBreed
from cat_breed import CatBreed
from dog_breed import DogBreed

from helper import snake_case

class PetMatch:
# #### constructor
    def __init__(self):
        self.pet_store = []

# #### add pet breed
    def add_pet_breed(self, pet):
        '''add pet to pet store'''
        self.pet_store.append(pet)


# #### search pet_store methods

    def search_pet_breed(self, **kwargs):
        '''search for pets that match an array of atrribute values'''
        pets = []

        # check if kwargs is empty
        if not kwargs:
            print("No pet breeds match this search criteria in kwargs{ }")
            return

        for pet in self.pet_store:
            match =True
            for key, value in kwargs.items():
                if getattr(pet, key).lower()  != value.lower():
                    match = False
                    break
            if match:
                pets.append(pet)
        if not pets:
            print("No pet breeds match this search criteria in []")
            return

        self.display_search_results(pets)
        self.export_search_results(pets, kwargs)

    def display_search_results(self, pets):
        for pet in pets:
            print(pet.display_breed_info())
        
    def export_search_results(self, pets, search_criteria):
        while True:
            report_option = input("Create a report file of search results (Y/N): ")
            try:
                if report_option.lower() not in ['y', 'n']:
                    raise ValueError("Enter Y or N")
                if report_option == 'n':
                    break
            except ValueError as e:
                print(e)
            else:
                report_name = snake_case(input("Enter report file name: "))
                file_name = report_name + '.txt'
                with open(file_name, 'w') as file:
                    file.write(f'PetMatch Summary: {search_criteria}')
                    file.write('\n')
                    for pet in pets:
                        file.write(str(pet))
                break
                

# #### show pet/s method/s    
    def show_all_pet_breeds(self):
        for pet in self.pet_store:
            print(pet)

    def show_pet_breed(self, name):
        for pet in self.pet_store:
            if pet.name.lower() == name.lower():
                print(pet)
                return pet
        return None

    def edit_pet_breed(self, petbreed, name, size, weight, coat, energy, temperament, lifespan, colours, activities):
        for pet in self.pet_store:
            if pet.id == petbreed.id:
                pet.name = name
                pet.size = size
                pet.weight = weight
                pet.coat = coat
                pet.energy = energy
                pet.temperament = temperament
                pet.lifespan = lifespan

                if pet.type.lower() == 'cat':
                    pet.colours = colours
                else:
                    pet.activities = activities
                    
                return

    def delete_pet_breed(self, name):
        for pet in self.pet_store:
            if pet.name.lower() == name.lower():
                self.pet_store.remove(pet)