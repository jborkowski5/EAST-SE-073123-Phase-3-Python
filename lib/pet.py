#!/usr/bin/env python3
import ipdb
#✅ 1. Create a Pet class

class Pet:
        pass
        #✅ 2. Instantiate a few pet instances in ipdb 
        #✅ 2a. Compare the pet instances to demonstrate they are not the same object
        
        #✅ 3. Demonstrate __init__ 
        def __init__(self, name, age, breed, owner='No Owner'):
        #✅ 3a. Add parameters for attributes (NO OWNER YET, SEE 3D)
            self.name = name
            self.age = age
            self.breed = breed
            self.owner = owner
        #✅ 3b. use dot notation to access their attributes 
        #✅ 3c. update attributes with new values 
        #✅ 3d. add owner attribute with default value

        #✅ 4. Demonstrate INSTANCE methods
        #✅ 4a. Create a hello method that will print "Hello!"
        def hello(self):
            print('hello')
        #✅ 4b. Create a print_pet_details function that will print the pet attributes
        def print_pet_details(self):
            print(f'''
                    name: {self.name}
                    age: {self.age}
                    breed: {self.breed}
                    owner: {self.owner}
                ''')


    #✅ 5. Set constraints for updating properties (attributes that are controlled by methods)
class Owner:    
    #✅ 5d.  Add parameter to pass in name property value on instantiation
        def __init__ (self, name, age):
            self.name = name
            self.age = age
    #✅ 5a. Create get/set instance methods for name property 

        def get_name(self):
            print('getting name........')
            return self._name
    #✅ 5b. Create constraint to make sure the name is of type string
        def set_name(self, name):
            print('setting name........')
            if isinstance(name, str):
                self._name = name
                return self._name
            else:
                print('Not a string.....')
    #✅ 5c. Compile get_name, set_name under the same property name
        name = property(get_name, set_name)

        @property
        def get_age(self):
            return self.age
        @age.setter
        def age(self, age):
            print('Setting age.........')
            if(isinstance(age, int)):
                    self._age = age
                    return self._age
            else:
                print('Not a int.....') 
koda = Pet("koda", 2, "dog", 'joe')    
nip = Pet("nip", 6, "cat", 'dee')    
kaley = Pet("kaley", 32, "woman", 'wee')  
joe = Owner('Joe', 36)  
dee = Owner('dee', 45)  
wee = Owner('wee', 75)  
ipdb.set_trace()