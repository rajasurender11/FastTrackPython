
my_list = [4,2,5,7,9,1]
my_list_sorted =  sorted(my_list)
print(my_list_sorted)
print(my_list_sorted[0])
length_of_list = len(my_list_sorted)
print(my_list_sorted[length_of_list-1])
#write a program to find the smallest number in a list ,
# dont use any built in function
smallest_number = my_list[0] #4 #2
for i in my_list: #4<4 2<4 5<2 7<2
    if(i<smallest_number):
        smallest_number =i
print(f"smallest number is {smallest_number}")


largest_number = my_list[0] #4 #2
for i in my_list: #4<4 2<4 5<2 7<2
    if(i>largest_number):
        largest_number =i
print(f"largest number is {largest_number}")


