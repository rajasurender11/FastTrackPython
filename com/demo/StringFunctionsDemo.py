emp_name = "surender"
salary = "50000"
emp_details = "100|surender|TCS|CHN"

num = 90
#write a program to check whether this num is odd or even
num_list = ["surender","raja","ajay"]

length_emp_name =  len(emp_name)
print(f" length of {emp_name} is {length_emp_name}")

print(emp_name[0])
print(emp_name[1])
print(emp_name[7])

c1 = emp_name[7]
print(c1)

#substring in String ex : surender sure
print(emp_name[0:3]) #0 1 2
print(emp_name[0:4]) #0 1 2 3
print(emp_name[1:4]) #1 2 3
print(emp_name[3:5]) #3 4
print(emp_name[0:]) # from 0th index till end of string
print(emp_name[4:])# from 4th index till end of string
print(emp_name[:5])# from 0th index till 4th index
s1 = emp_details[0:6]
print(s1)
emp_details = "100|surender|TCS|CHN|IND"
#delimiter --> |
emp_arr =emp_details.split("|")
print(emp_arr)
print(emp_arr[1])
print(emp_arr[2])
print(f"length of list {len(emp_arr)}")

company_details = "TCS,CHN|OMR"
print(company_details.split(","))
print(company_details.split("|"))


upper_emp_name = emp_name.upper()
print(upper_emp_name)

s2 = "DATA"
s2.lower()
print(s2.startswith("T"))
print(s2.endswith("A"))
s3 =s2.replace("A","M")
print(s3)

r = emp_name + " " + salary
print(r)



