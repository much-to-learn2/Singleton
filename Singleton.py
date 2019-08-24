"""
Python Singleton class

The first time the Singleton class is created, instance is None and so 
the instance is created by 
#    cls.instance = super().__new__(cls)

Once an instance exists, the Singleton.instance attribute will point to 
that singular instance. Therefore, creating "new" Singleton instances becomes:
#    def __new__(cls):
#        return cls.instance
Clearly, creation of a new reference to Singleton will now point back to the 
original Singleton.instance that was created

Usage:

>>> x = Singleton()
>>> y = Singleton()
>>> x is y
True
>>> x.instance is y
True
>>> Singleton.instance is x
True
>>> Singleton.instance is y.instance
True

"""

import doctest

# The inheritance from object is shown explicitly here because of the call
# to super(), which in this case will reference object
class Singleton(object):
    
    # Set the class attribute "instance" to None -
    # No instances of the Singleton class exist yet
    instance = None 

    # define protocol for creation of new class
    def __new__(cls):
        if not cls.instance: 
            # if an instance of Singleton does not yet exist, create it
            # and assign it's value to Singleton.instance.
            # Singleton.instance will now reference this class instance
            cls.instance = super().__new__(cls)
         
        # return the instance
        return cls.instance 

