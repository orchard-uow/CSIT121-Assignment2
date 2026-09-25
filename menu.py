from pet_match import PetMatch
from pet_breed import PetBreed
from cat_breed import CatBreed
from dog_breed import DogBreed
from pet_breed_input import PetBreedInput
from get_pets_from_file import AddPetBreeds

class Menu:
    
    '''menu to display and react to user input'''
    
    def __init__(self, petmatch):
        self.petmatch = petmatch
        self.breed_input = PetBreedInput()
        # pass self.petmatch object to 
        # allows to share same PetMatch object
        self.add_pet_breeds = AddPetBreeds(self.petmatch)
        # call APB to add pet objects to same pet store
        self.add_pet_breeds.add_pet_breeds_from_external_file()


    def petmatch_menu(self):
        '''display menu for users to choose'''
        print()
        print("PetMatch Menu")
        print("1. Add Pet Breed")
        print("2. Search Pet Breeds")
        print("3. Show all Pet Breeds")
        print("4. Show a Pet Breed")
        print("5. Edit Pet Breed")
        print("6. Delete Pet Breed")
        print("7. Quit")
        print()
        
    def petmatch_menu_interface(self):
        '''user interface for menu display.
        user to enter an option number'''
        while True:
            self.petmatch_menu()
            # option exception handling
            try:
                p_m_option = int(input('Enter an option number: '))
                
                if p_m_option < 1 or p_m_option > 7:
                    raise ValueError('Option must be between 1 and 7')
                
            except ValueError as e:
                if str(e) != 'Option must be between 1 and 7':
                    print("Please enter a number.")
                else:
                    print(e)
                    
            else:
                # match sim to switch in js
                match p_m_option:
                    case 1:
                        print("1. Add Pet Breed")
                        self.add_pet_breed()
                    case 2:
                        print("2. Search Pet Breeds")
                    case 3:
                        print("3. Show all Pet Breeds")
                        self.show_all_pet_breeds()
                    case 4:
                        print("4. Show a Pet Breed")
                    case 5:
                        print("5. Edit Pet Breed")
                    case 6:
                        print("6. Delete Pet Breed")
                    case 7:
                        print("7. Quit")

    def add_pet_breed(self):
        # refactored pet input sequence into PetBreedInput class
        pet = self.breed_input.get_pet_breed_values()

        # append pet to self.petmatch.pet_store
        self.petmatch.pet_store.append(pet)
        print(len(self.petmatch.pet_store))
        
    def show_all_pet_breeds(self):
        self.petmatch.show_all_pet_breeds()
        

if __name__ == '__main__':
    # create a PetMatch object - contains pet_store[]
    petmatch = PetMatch()
    # pass/provide PetMatch object into menu 
    # to share with other classes as needed
    menu = Menu(petmatch)
    # run interface
    menu.petmatch_menu_interface()           