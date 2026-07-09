from typing import TypedDict

class Person(TypedDict):

    name: str
    age: int

new_person: Person = {'name':'nitish', 'age':35}

print(new_person)

#This is the example of the type dict in python. TypedDict is a way to define a dictionary with specific key-value types. In this example, we define a TypedDict called Person with two keys: 'name' of type str and 'age' of type int.