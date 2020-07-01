#!/usr/bin/python3
"""
Unittest for class BaseModel
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class BaseModelTest(unittest.TestCase):
    """ class BaseModel unittest """

    def test_print_id(self):
        """
        testing for id
        """
        b1 = BaseModel()
        print(b1.id)
        print(b1)

    def test_to_dict(self):
        """
        convert to dictionary
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        print(my_model)
        my_model.save()
        print(my_model)
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".
                  format(key, type(my_model_json[key]), my_model_json[key]))

    def test_init_base_model_dict(self):
        """
        testing for when the base model has a dictionary as a parameter
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        print(my_model.id)
        print(my_model)
        print(type(my_model.created_at))
        print("--")
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".
                  format(key, type(my_model_json[key]), my_model_json[key]))
        print("--")
        my_new_model = BaseModel(**my_model_json)
        print(my_new_model.id)
        print(my_new_model)
        print(type(my_new_model.created_at))
        print("--")
        print(my_model is my_new_model)

if __name__ == '__main__':
    unittest.main()
