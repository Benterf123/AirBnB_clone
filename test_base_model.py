#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
f = my_model_json
print(f)
print("JSON of my_model:")
for key in f.keys():
    print("\t{}: ({}) - {}".format(key, type(f[key]), f[key]))
