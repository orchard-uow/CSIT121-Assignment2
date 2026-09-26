

class SearchPetBreedCriteria:
    '''Get search criteria from user input.
    Only allow search for mandatory pet breed 
    fields: type, name, size'''
    def search_pet_breeds(self):
        search_criteria = {}

        # while True:
        pet_type = input('Enter pet type (Cat, Dog): ').strip()
        if pet_type:
            search_criteria['type'] = pet_type.lower().capitalize()

        pet_name = input('Enter pet name: ').strip()
        if pet_name:
            search_criteria['name'] = pet_name.lower().capitalize()

        pet_size = input('Enter pet size: ').strip()
        if pet_size:
            search_criteria['size'] = pet_size.lower().capitalize()

        return search_criteria
