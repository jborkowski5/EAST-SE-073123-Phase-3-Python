# Sequence Types

# Creating Lists
#✅ 1. Create a list of 10 pet names
pet_names = ['momo', 'sally', 'gizmo', 'nip', 'bear', 'doggy', 'brownie', 'EJ', 'ari', 'koda']


#------------------------ Reading Information from Lists
#✅ 2. Return the first pet name 

(pet_names[0])

#✅ 3. Return the last value
(pet_names [-1])

#✅ 4. Return all pet names beginning from the 3rd index

(pet_names[3:10])

#✅ 5. Return all pet names before the 3rd index

(pet_names[0:3])

#✅ 6.  Return all pet names beginning from the 3rd index and up to (exclusive of) the 7th
(pet_names[3:7])

#✅ 7. Find the index of a given element

(pet_names.index('koda'))

#✅ 8. Reverse the original list

(pet_names.reverse())
('after reverse', pet_names)

#✅ 9. Return the frequency of a given element 

(pet_names.count('nip'))

#---------------------------------- Updating Lists
#✅ 10. Change the first element to all uppercase

pet_names[0] = pet_names[0].upper()





#---------------------------------- Adding items to list
#✅ 11. Append a new name to the list

pet_names.append('yo mamma')


#✅ 12. Add a new name at a specific index

pet_names.insert(-1, "CoCo")


#✅ 13. Add two lists together 

added_list = [1, 2, 3] + [4, 5, 6]




#---------------------------------- Removing 
#✅ 14. Remove the final element from the list

pet_names.pop()

#✅ 15. Remove element by specific index

pet_names.pop(5)

#✅ 16. Remove a specific element 

pet_names.remove('KODA')


#✅ 17. Remove all pet names from the list

pet_names.clear()


#---------------------------------- Tuple 
#✅ 18. Create a Tuple of pet 10 ages 

pet_ages = [3, 6, 9, 16, 12, 3, 4, 32, 81, 2]

#✅ 19. Print the first pet age

(pet_ages[0])

#---------------------------------- Testing Changeability 
#✅ 20. Attempt to remove an element with .pop (should error)

# pet_ages.pop()

#✅ 21. Attempt to change the first element (should error)

# pet_ages[0] = "yo mama"


#---------------------------------- Tuple Methods
#✅ 21. Return the frequency of a given element

(pet_ages.count(81))

#✅ 22. Return the index of first matching element 

(pet_ages.index(81))


#✅ 23. Create a range 

range_1 = range(0, 10, 2)
range_2 = range(2, 5, 1)
for i in range_1:



#---------------------------------- Demo Sets
#✅ 24. Create a set of 3 pet foods



# Demo Dictionaries 
#---------------------------------- Creating 
#✅ 25.  Create a dictionary of pet information with the keys name, age and breed

    koda = {'name': 'koda', 'age': 99, 'breed': 'black lab'}


#✅ 26.  Use dict to create a dictionary of pet information with the keys name, age and breed

koda_dict = dict(name='koda', age= 99, breed='black lab')
(koda_dict)


#---------------------------------- Reading
#✅ 27. Print the pet attribute of name using bracket notation

(koda['age'])

#✅ 28. Print the pet attribute of age using .get

(koda.get('age'))


#---------------------------------- Updating 
#✅ 29. Update the pets age to 12

koda['goals'] = 12


#✅ 30. Update the other pets age to 26






#---------------------------------- Deleting
#✅ 30. Delete a pets age using the del keyword 

del koda['goals']

#✅ 31. Delete the other pets age using the .pop, returns removed value

(koda.pop('age'))


#✅ 32. Delete the last item in the pet dictionary using popitem()

koda.popitem()





#---------------------------------- Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
]


#✅ 33. loop through a range of 10 and print every number within the range
for i in range (1, 10):
    pass
i=1
while(i<10):
    #print(i)
    i+=1



#✅ 34. loop through a range between 50 and 60 that iterates by 2 and print every number

    # for i in range (50, 60, 2):
    #     print(i)


#✅ 35. Loop through the pet_info list and print every dictionary  

for pet in pet_info:
    #print(pet)
    
#✅ 36. Create a function that takes a list as an argument. 
    # The function should use a for loop to loop through the list and print every item in the list 
    # Invoke the function and pass it pet_names as an argument

    def print_info(lst=pet_info):
        for pet in pet_info:
            print(pet)
    # print_info()        
    # print_info(pet_info)



#✅ 37. Create a function that takes a list as an argument.(simple example) 
def counter(info=pet_info):
    # The function should define a counter and set it to 0
    counter = 0
    # Create a while loop 
    while(counter < len(info)):
    
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
        counter += 1
    # return the counter 
    return counter
#print(counter(pet_info))

#✅ 38. Create a function that updates the age of a given pet
def update_age(info, name, age):
        # The function should take a list of dicts, name and age as parameters 
        # Create a index variable and set it to 0
        cur_index = 0
        # Create a while loop. 
        while(cur_index < len(info) and info[cur_index].get('name') != name):
            cur_index += 1
            # The loop will continue so long as the list does not contain a name matching the name param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found update the items age with the new age
        if(cur_index >= len(info)):
            print('error')
        else:    
            info[cur_index]['age'] = age
        # else return 'pet not found'
update_age(pet_info, 'Meow Meow Beans', 0)        
#print(pet_info)

#✅ 39. Use list comprehension to return a list containing every pet name from pet_info changed to uppercase

pet_names_upper = [pet.get('name').upper() for pet in pet_info]

#✅ 40. Use list comprehension to find a pet named spot

find_pet = [pet for pet in pet_info if pet.get('name') == 'spot']

#✅ 41. Use list comprehension to find all of the pets under 3 years old

age_pet = [pet for pet in pet_info if pet.get('age') < 25]
print(age_pet)

#✅ 43. Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
