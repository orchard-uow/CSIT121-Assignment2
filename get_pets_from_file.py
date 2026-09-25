from cat_breed import CatBreed
from dog_breed import DogBreed
# from pet_match import PetMatch

cat_attributes = [
    'type', 'name', 'size', 'weight', 'coat',
    'energy', 'temperament', 'lifespan', 'colours'
]

dog_attributes = [
    'type', 'name', 'size', 'weight', 'coat',
    'energy', 'temperament', 'lifespan', 'activities'
]

class AddPetBreeds:
    # when APB object created pass PM object to it
    def __init__(self, petmatch):
        # store PM object in APB object
        self.pet_match = petmatch

    def add_pet_breeds_from_external_file(self):
        '''open text file to read pet data. 
        Turn data into pet breed objects. 
        Save into PetMatch pet store'''

        # open & read petbreeds.txt
        with open('petbreeds.txt', 'r') as file:
            # read one line at a time - 1 pet per line
            for line in file:
                # remove whitespace & turn into list
                # needed help to work this strip split out ???
                data = line.strip().split(', ')
                data = [item.strip() for item in line.split(',')]
                # print(data)

                # check if breed is cat or dog
                # assign appropriate attributes and class
                if data[0].lower() == 'cat':
                    attributes = cat_attributes
                    breed = CatBreed
                else:
                    attributes = dog_attributes
                    breed = DogBreed

                # create empty dict to store breed attributes
                breed_values = {}

                # match each attribute with value from file
                for i in range(len(attributes)):
                    breed_values[attributes[i]] = data[i]

                # researched how to unpack a dict k:v pairs as object parameters
                pet = breed(**breed_values)

                # print(type(pet))

                # append pet to petmatch pet store
                self.pet_match.pet_store.append(pet)

