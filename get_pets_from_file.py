import json
from cat_breed import CatBreed
from dog_breed import DogBreed

# cat_attributes = [
#     'type', 'name', 'size', 'weight', 'coat',
#     'energy', 'temperament', 'lifespan', 'colours'
# ]

# dog_attributes = [
#     'type', 'name', 'size', 'weight', 'coat',
#     'energy', 'temperament', 'lifespan', 'activities'
# ]

class AddPetBreeds:
    # when APB object created pass PM object to it
    def __init__(self, petmatch):
        # store PM object in APB object
        self.pet_match = petmatch

    def add_pet_breeds_from_external_file(self):
        '''open JSON file to read and create 
        pet breed objects. 
        Save them into PetMatch pet store'''

        # open & read petbreeds.json
        with open('petbreeds.json', 'r') as file:
            # convert JSON into objects
            data = json.load(file)

            # loop through data
            for pet_breed_data in data:
                # check if breed is a cat or a dog
                if pet_breed_data["type"].lower() == "cat":
                    breed = CatBreed
                else:
                    breed = DogBreed

                # create pet breed object
                pet = breed(**pet_breed_data)

                # append to PetMatch pet_store
                self.pet_match.pet_store.append(pet)

