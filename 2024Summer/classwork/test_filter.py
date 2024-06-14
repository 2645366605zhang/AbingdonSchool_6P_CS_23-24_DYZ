import unittest
from profanity_filter import censor_0

class TestFilterResult(unittest.TestCase):

    def test1(self):
        self.assertEqual(censor_0("You are a dunderhead spoon muncher."), "You are a d********d spoon muncher.")
    
    def test2(self):
        self.assertEqual(censor_0("Oh lordy this is a load of poppycock poo"), "Oh l***y this is a load of p*******k p*o")

# class TestFilterMore(unittest.TestCase):
#     def test_return_type(self):
#         self.assertIsInstance(censor_0("blah"), str)
        
#     def test_exception(self):
#         self.assertRaises(TypeError, censor_0)
#         self.assertRaises(AttributeError, censor_0, 123)


if __name__ == '__main__':
    unittest.main()

