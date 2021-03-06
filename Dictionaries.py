# Python Dictionaries
"""
Dictionaries are used to store data values in Key:value pairs.
A dicitionary is a collection that is ordered, changeable and does not allow duplicates.
They  are written in curly brackets and have keys and values
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
print(type(thisdict))
# Dictionary items
"""
The dictionary items are orderd, changeable and does not allow duplicates.
They are presented in key:value pairs and can be referred to by using key names for example
print the brand name of the example
"""
print(thisdict["brand"])
#Ordered and unorderd
"""As of python 3.7 and later dictionaries are orderd but as of python 3.6 and earlier dictionaries are unorderd.
When we say that items are orderd it means that the items have a defined order and that order will not change.
Unorderd means that the items do not have a defined order and you cannot refer to them by using index numbers.
"""
# Changeable
"""
Means that the items in a dictionary can be changed, i.e, they can be changed, added or removed from a dictionary once
it has been created.
"""
#Duplicates not allowed
"""
Dictionaries cannot have items with the same key
Duplicate values will overwrite exisiting values.
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2000
}
print(thisdict)
#print(type(thisdict))

# Dictionary length
"""
To determine the number of values in a dictionary use the len() method
"""
print(len(thisdict))
# Dictionary items- Data types
"""
Dictionary items can be of any data types
"""
thisdict = {
    "brand": "Ford",
    "Electric": False,
    "model": "Mustang",
    "year": 1964,
    "year": 2000,
    "colors": ["red", "White", "blue"]
}
print(thisdict)
print(type(thisdict))

# Accessing items in a dictionary
"""
Items in a dictionary can be accessed using the keys.
They can also be accessed using the get() method
"""
x = thisdict["model"]
print(x)

x = thisdict.get("model")
print(x)

# Get keys
"""
The keys() method will get you a list alll the keys in the dictionaries
"""
x = thisdict.keys()
print(x)
"""
The list of the keys is the view of the dictionary.
Meaning any changes made in the dictionary will be reflected in the keys list
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
x = car.keys()
print(x) #The list of keys before the change

car["color"] = "white"
print(x) # the list of keys after the change

# Get values
"""
The values() method will return a list of all the values in a list in a dictionary.
"""
x = thisdict.values()
print(x)
"""
The list list of the values is the view of the dictionary.
Meaning any changes made in the dictionary will be reflected in the values
"""
x = car.values()
print(x) # The list of the values before the change
car["year"] = 2000
print(x) # The list of values after the change.
"""
Let's add a new item to our dictionaries and see the list of values being updated as weel
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
x = car.values()
car["color"] = "red"
print(x)

# Get Items
"""
The items() method will return all the items in a dictionary, as tuples in a list
"""
x = thisdict.items()
print(x)
"""
The returned list is a view of items in a dictionary.
This means that any changes done in the dictionary will be
reflected in the items
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
x = car.values()
x = car.items()
print(x) # Before the change

car["year"] = 2020
print(x)# After the change

"""Add a new item in the dictionary and see how the items in the dictionary are updates"""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
x = car.values()

x = car.items()
car["color"] = "red"
print(x)

# Check if the key exists
"""
To determine if the key is available use the in keyword
Check if 'model' is available in the dictionary
"""
thisdict = {
    "brand": "Ford",
    "Electric": False,
    "model": "Mustang",
    "year": 1964,
    "year": 2000,
    "colors": ["red", "White", "blue"]
}

if "model" in thisdict:
    print("Yes, model key exists in this dictionary")

# Change values in a dictionary
"""
You can change the values of a specific item by referring to it key
"""
thisdict = {
    "brand": "Ford",
    "Electric": False,
    "model": "Mustang",
    "year": 1964,
    "year": 2000,
    "colors": ["red", "White", "blue"]
}
thisdict["year"] = 2018
print(thisdict)

# Update dictionaries
"""
The update() method will update the dictionaries with the items from a given argument.
The object must be a dictionary or an iterable object with key:value pairs
Example, update the year of the car using the update method
"""
thisdict.update({"year": 2020})
print(thisdict["year"])

# Remove items from the dictionary
"""
There are several methods of removing items from a dictionay.
The pop() removes the item with a specified key name
"""
thisdict.pop("model")
print(thisdict)

"""
popitem removes the last inserted item, (in versions before 3.7 used to remove a random item)
"""
thisdict.popitem()
print(thisdict)

"""
del keyword removes the item with the specified key
"""
del thisdict["model"]
print(thisdict)

"""
The del keyword can also delete the entire dictionary
del thisdict
print(thisdict) will return an error because "thisdict" no longer exists
clear() method empties the dictionary
thidict.clear()
print(thisdict) will return an empty dictionary
"""

# Nested Dictionaries
"""
A dictionary can contain dictionaries as show in the programs below
"""
myFamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007 
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myFamily)

# Nested Dictionaries
"""
A dictionary can contain dictionaries as show in the programs below.
"""
# We can aslo create dictionaries outside and create another big dictionary that will contain all of them
child1 = {
    "name": "Emil",
    "year": 2004
}

child2 = {
    "name": "Tobias",
    "year": 2007
}

child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(child1)
print(child2)
print(child3)
print(myfamily)