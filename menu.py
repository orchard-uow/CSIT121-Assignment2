from pet_match import PetMatch
from pet_breed import PetBreed
from cat_breed import CatBreed
from dog_breed import DogBreed

class Menu:
    
    '''menu to display and react to user input'''
    
    def __init__(self):
        self.petmatch = PetMatch()
        
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

        cat_attributes = [
            'name', 'size', 'weight', 'coat',
            'energy', 'temperament', 'lifespan', 'colours'
        ]

        dog_attributes = [
            'name', 'size', 'weight', 'coat',
            'energy', 'temperament', 'lifespan', 'activities'
        ]

        breed_values = {}

        # Select pet type
        while True:
            pet_type = input('Enter pet type (Cat, Dog): ')

            try:
                if pet_type.lower() not in ['cat', 'dog']:
                    raise ValueError('Please enter Cat or Dog.')

                if pet_type.lower() == 'cat':
                    breed = CatBreed
                else:
                    breed = DogBreed

                breed_values['type'] = pet_type.capitalize()
                break

            except ValueError as e:
                print(e)

        # Select appropriate attributes
        if pet_type.lower() == 'cat':
            attributes = cat_attributes
        else:
            attributes = dog_attributes

        # Get values to set attributes
        for prop in attributes:

            while True:
                if prop == 'size':
                    value = input(f'Enter {prop}({breed.sizes}): ')
                elif prop == 'coat':
                    value = input(f'Enter {prop}({breed.coats}): ')
                else:
                    # default non validated attribute values
                    # can be left empty
                    value = input(f'Enter {prop}: ')

                try:
                    if prop == 'size':
                        if value.lower() not in breed.sizes:
                            raise ValueError(
                                f'Size must be one of {breed.sizes}'
                            )

                    if prop == 'coat':
                        if value.lower() not in breed.coats:
                            raise ValueError(
                                f'Coat must be one of {breed.coats}'
                            )

                    if prop == 'weight':
                        if value == '':
                            raise ValueError(
                                'A pet must weigh something.'
                            )

                    if prop == 'weight':
                        breed_values[prop] = value + 'kg'
                    elif prop == 'lifespan':
                        breed_values[prop] = value + 'yrs'
                    else:
                        breed_values[prop] = value
                    break

                except ValueError as e:
                    print(e)

        print(breed_values)
                    
        
if __name__ == '__main__':
    menu = Menu()
    menu.petmatch_menu_interface()           