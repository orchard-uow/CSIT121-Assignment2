import unittest

# import PetMatch classes
from pet_breed import PetBreed
from dog_breed import DogBreed
from cat_breed import CatBreed
from pet_match import PetMatch

# import custom exceptions
from exceptions import InvalidSizeError

# PetMatch tests
class TestPetMatch(unittest.TestCase):
    
    def setUp(self):
        # print("\nSetting up PetMatch test ...")
        # default PetMatch
        self.pet_match = PetMatch()
        
        # CatBreed with only required attributes added
        self.cat1 = CatBreed("Cat", "Ragdoll", "Medium", "4-9kg" ) 

        # DogBreed with only required attributes added
        self.dog1 = DogBreed("Dog", "Border Collie", "Medium", "14-20kg" ) 

    def test_add_cat_to_pet_match_store(self):
        '''add CatBreed to PetMach.store[]\n'''
        self.pet_match.add_pet(self.cat1)
        # assertations
        self.assertEqual(len(self.pet_match.pet_store), 1)
        self.assertEqual(self.pet_match.pet_store[0].name, 'Ragdoll')
        # print(self.pet_match.pet_store[0])
        
    def test_add_dog_to_pet_match_store(self):
        '''add DogBreed to PetMach.store[]\n'''
        self.pet_match.add_pet(self.dog1)
        # assertations
        self.assertEqual(len(self.pet_match.pet_store), 1)
        self.assertEqual(self.pet_match.pet_store[0].name, 'Border Collie')
        # print(self.pet_match.pet_store[0])
        
    def test_display_pet_info(self):
        '''display pet info test\n'''
        result = self.cat1.display_breed_info()
        info = f"\nid: {self.cat1.id} type: {self.cat1.type}, name: {self.cat1.name}, size: {self.cat1.size}, weight: {self.cat1.weight}, coat: {self.cat1.coat}, energy: {self.cat1.energy}, temperament: {self.cat1.temperament}, lifespan: {self.cat1.lifespan}, colours: {self.cat1.colours}"
        self.assertEqual(result, info)
        
    def test_search_pet_by_term(self):
        ''' search pets in pet store that match search term\n'''
        # add pets to store
        self.pet_match.add_pet(self.cat1)
        self.pet_match.add_pet(self.dog1)
        self.assertEqual(len(self.pet_match.pet_store), 2)
        
        # search for pet in store
        self.pet_match.search_pet(self.cat1.size)
        # self.assertEqual()
   
#    todo: delete, show all pets in store
   
        
if __name__ == "__main__":
    unittest.main()
        