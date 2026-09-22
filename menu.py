from pet_match import PetMatch
from pet_breed import PetBreed
from cat_breed import CatBreed
from dog_breed import DogBreed
from pet_breed_input import PetBreedInput

class Menu:
    
    '''menu to display and react to user input'''
    
    def __init__(self):
        self.petmatch = PetMatch()
        self.breed_input = PetBreedInput()
        
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
            # exception handling
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
                        self.add_pet_breed()
                    case 2:
                        print("2. Search Pet Breeds")
                    case 3:
                        print("3. Show all Pet Breeds")
                    case 4:
                        print("4. Show a Pet Breed")
                    case 5:
                        print("5. Edit Pet Breed")
                    case 6:
                        print("6. Delete Pet Breed")
                    case 7:
                        print("7. Quit")

    def add_pet_breed(self):
        pet = self.breed_input.get_pet_breed_values()
        print(pet)
        print(pet.name)
        print(type(pet))
        # append pet to self.petmatch.pet_store

        

if __name__ == '__main__':
    menu = Menu()
    menu.petmatch_menu_interface()           