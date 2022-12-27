#list in python is collection of elements
#list is mutable (changable)
id = 90
my_number_list = [2,2,2,3,4,8]
my_number_list[0]
my_number_list[1]
my_str_list = ["surender","raja","python"]
my_mixed_list = [4,"surender",7.8]

for a in my_mixed_list:
    print(a)

print(my_number_list)
my_number_list.append(10) #add a new element to the end of list
print(my_number_list)
my_number_list.insert(3,7) # add a new element at a specific index
print(my_number_list)
my_number_list.remove(8)# removing a element
print(my_number_list)
my_number_list.pop(0)#removing a element at a specific index
print(my_number_list)



#tuple immutable (cannot change it )

my_number_tuple = (4,7,8)
my_str_tuple = ("surender","hadoop","sql")
my_mixed_tuple = (2,8.9,"python")

for i in my_number_tuple:
    print(i)

temp_list = list(my_number_tuple)
temp_list.append(77)
updated_tuple = tuple(temp_list)
print(updated_tuple)

#set , it will not have duplicates curely braces
#mutable , add, insert, pop

my_num_set = {2,2,2,2,3,3,4}
print(my_num_set)
my_num_set.add(5)
print(my_num_set)
my_num_set.pop()
print(my_num_set)
my_num_set.remove(5)
print(my_num_set)

#Dictionary  Key : value pair ,mutable

d = {1:"one",
     2:"two"}

d1 = {"CHN":"CHENNAI",
      "BNG":"BANGALORE"}

print(d[1])
print(d1["BNG"])

"""
for key in d: # Iterates just through the keys, ignoring the values
for key, value in d.items(): # Iterates through the pairs
for key in d.keys(): # Iterates just through key, ignoring the values
for value in d.values(): # Iterates just through value, ignoring the keys
"""
for i in d.keys():
    print(i)



for value in   d1.values():
    print(value)

d.update({3:"Three"})

for i,j in d.items():
    print(f"{i} --> {j}")

d.update({2:"TWOOOO"})

for i,j in d.items():
    print(f"{i} --> {j}")