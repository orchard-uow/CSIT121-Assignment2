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
        # instantiate PetMatch object
        self.pet_match = PetMatch()

        # reset PetBreed id to 1 before each test
        PetBreed.next_pet_id = 1
        
        # CatBreed with only required attributes added
        self.cat1 = CatBreed("Cat", "Ragdoll", "Medium", "4-9kg" ) 
        self.cat2 = CatBreed("Cat", "Norwegian Forest Cat", "Large", "6-10kg" ) 

        # DogBreed with only required attributes added
        self.dog1 = DogBreed("Dog", "Border Collie", "Medium", "14-20kg" ) 
        self.dog2 = DogBreed("Dog", "Alaskan Malamute", "Giant", "38-56kg" ) 
        self.dog3 = DogBreed("Dog", "Australian Terrier", "Small", "5-7kg" ) 


    def test_add_cat_to_pet_match_store(self):
        '''add CatBreed to PetMach.store[]\n'''
        self.pet_match.add_pet_breed(self.cat1)
        # assertations
        self.assertEqual(len(self.pet_match.pet_store), 1)
        self.assertEqual(self.pet_match.pet_store[0].name, 'Ragdoll')
        # print(self.pet_match.pet_store[0])


    def test_add_dog_to_pet_match_store(self):
        '''add DogBreed to PetMach.store[]\n'''
        self.pet_match.add_pet_breed(self.dog1)
        # assertations
        self.assertEqual(len(self.pet_match.pet_store), 1)
        self.assertEqual(self.pet_match.pet_store[0].name, 'Border Collie')
        # print(self.pet_match.pet_store[0])


    def test_display_pet_info(self):
        '''display pet info test\n'''
        # display breed info for 2 pets
        result = self.cat1.display_breed_info()
        result1 = self.dog1.display_breed_info()
        # expected results for cat1 display
        info = f"\nid: {self.cat1.id} type: {self.cat1.type}, name: {self.cat1.name}, size: {self.cat1.size}, weight: {self.cat1.weight}, coat: {self.cat1.coat}, energy: {self.cat1.energy}, temperament: {self.cat1.temperament}, lifespan: {self.cat1.lifespan}, colours: {self.cat1.colours}"
        # test single display
        self.assertEqual(result, info)
        # test 2 display outputs are different 
        # to demonstrate ploymorphism between two different 
        # calling the same function for different outcomes
        self.assertNotEqual(result, result1)
        

    # search for pets tests
    # test if search mthod reached with no kwargs
    def test_search_for_pet_reached(self):
        '''test to see if search function reached'''
        result = self.pet_match.search_pet_breed()
        self.assertEqual(result, []) 

    # test search 1 pet returned using 1 **kwargs
    def test_search_size_small_pet(self):
        '''test for search pet size small'''
        # add 2 pets
        self.pet_match.add_pet_breed(self.dog2) # Alaskan Malamute
        self.pet_match.add_pet_breed(self.dog3) # Australian Terrier

        # search with 1 kwarg
        result = self.pet_match.search_pet_breed(size='small')
        # print(result)

        # test result has 1 pet returned 
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].size.lower(), 'small')

    # test search - 2 pets returned from 2 **kwargs
    def test_search_with_two_kwargs_for_two_results(self):
        '''test for 2 results wt 2 kwargs'''
        # add 4 pets
        self.pet_match.add_pet_breed(self.cat1) # Ragdoll
        self.pet_match.add_pet_breed(self.dog3) # Australian Terrier
        self.pet_match.add_pet_breed(self.dog1) # Border Collie
        self.pet_match.add_pet_breed(self.dog2) # Alaskan Malamute
        # test that there are 4 pets in store
        self.assertEqual(len(self.pet_match.pet_store), 4)

        # search with 2 kwargs
        result = self.pet_match.search_pet_breed(type='Cat', name='Border Collie')
        # print(result)
        # print(result[0]) # Ragdoll 
        # print(result[1]) # Border Collie

        # test result has 1 pet returned 
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].type.lower(), 'cat')
        self.assertEqual(result[1].name.lower(), 'border collie')     

    # show PetBreeds in pet_store[] all and single  
    # test show all PetBreeds
    def test_show_all_petbreeds_in_petstore(self):
        '''test show all petbreeds in petstore'''
        # add 2 pets to petstore
        self.pet_match.add_pet_breed(self.cat1)
        self.pet_match.add_pet_breed(self.cat2)
        # test if 2 breeds in petstore
        self.assertEqual(len(self.pet_match.pet_store), 2) 
        # test reach show all breeds in petstore
        # result = self.pet_match.show_all_pet_breeds()
        # self.assertEqual(len(result),2)

    # test show specific PetBreed
    def test_show_petbreed_in_petstore(self):
        '''test show individual petbreed'''
        # add 2 pets to petstore
        self.pet_match.add_pet_breed(self.cat1)
        self.pet_match.add_pet_breed(self.cat2)
        name = self.cat1.name
        # call show breed method
        result = self.pet_match.show_pet_breed(name)
        #test show method
        self.assertEqual(result, self.cat1)


    # edit breed
    def test_edit_pet_breed(self):
        '''test edit pet breed method using pet object as argument'''
        # add pet to pet store
        self.pet_match.add_pet_breed(self.cat1)
        #  edit added pet
        updated_cat = CatBreed(
            "Cat",
            "Persian",
            "Medium",
            "4-8kg"
        )
        updated_cat.id = self.cat1.id
        # call edit petbreed method
        self.pet_match.edit_pet_breed(updated_cat)
        # test to see if updated cat exists
        result = self.pet_match.show_pet_breed('Persian')
        self.assertEqual(result.name, 'Persian')
        self.assertEqual(result.size, 'Medium')
        self.assertEqual(result.weight, '4-8kg')

    # delete breed
    def test_delete_pet_breed_from_petstore(self):
        '''test delete pet breed from petstore'''
        # add pet to pet store
        self.pet_match.add_pet_breed(self.cat1)
        # test pet store has 1 pet breed
        self.assertEqual(len(self.pet_match.pet_store), 1)
        # call delete pet breed with cat1.id argument
        self.pet_match.delete_pet_breed(self.cat1.name)
        # test pet store has 0 pet breed
        self.assertEqual(len(self.pet_match.pet_store), 0)
#    todo:  delete, 
   
        
if __name__ == "__main__":
    unittest.main()
        