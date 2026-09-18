import unittest

# import PetMatch classes
from pet_breed import PetBreed
from dog_breed import DogBreed
from cat_breed import CatBreed

# import custom exceptions
from exceptions import InvalidSizeError

# dog tests
class TestDog(unittest.TestCase):
    
    def setUp(self):
        print("\nDog test ...")
        # DogBreed with all attributes added
        self.dog1 = DogBreed("Dog", "Alaskan Malimut", "Giant", "38-56kg", "Medium", "High", "Alaskan Malamutes are known for their friendly and affectionate temperament",  "The average lifespan of an Alaskan Malamute is around 10 to 14 years.", "Agility, Dog Sledding, Obedience, Rally Obedience, Therapy")

        # DogBreed with only required attributes added
        self.dog2 = DogBreed("Dog", "Border Collie", "Medium", "14-20kg" ) 

    def test_if_dog_exists(self):
        self.assertIsInstance(self.dog1, DogBreed)
        self.assertIsInstance(self.dog2, DogBreed)

    def test_optional_attributes(self):
        self.assertEqual(self.dog1.coat, "Medium")
        self.assertEqual(self.dog2.coat, "")

    # these validation tests may be better handled in menu with exceptions
    # def test_invalid_size(self):
    #     with self.assertRaises(InvalidSizeError):
    #         # DogBreed with invalid size raises an error
    #         self.dog3 = DogBreed("Dog", "Border Collie", "gigantic", "14-20kg" ) 

    # def test_invalid_coat(self):
    #     with self.assertRaises(InvalidSizeError):
    #         # DogBreed with invalid size raises an error
    #         self.dog3 = DogBreed("Dog", "Border Collie", "gigantic", "14-20kg" ) 

# cat tests
class TestCat(unittest.TestCase):
    
    def setUp(self):
        print("\nCat test ...")
        # CatBreed with all attributes added
        self.cat1 = CatBreed("Cat", "Norwegian Forest Cat", "Large", "6-10kg", "Long", "Medium", "Norwegian Forest Cats are known for their gentle and friendly temperament",  "The average lifespan of a Norwegian Forest Cat ranges from 12 to 16 years.", "White, black, blue, red, cream and silver, plus various patterns and shadings")

        # CatBreed with only required attributes added
        self.cat2 = CatBreed("Cat", "Ragdoll", "Medium", "4-9kg" ) 

    def test_if_Cat_exists(self):
        self.assertIsInstance(self.cat1, CatBreed)
        self.assertIsInstance(self.cat2, CatBreed)

    def test_optional_attributes(self):
        self.assertEqual(self.cat1.coat, "Long")
        self.assertEqual(self.cat2.coat, "")




# run unit tests
if __name__ == "__main__":
    unittest.main()