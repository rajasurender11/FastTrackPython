"""
emp_id = 10
emp_name = "surender"
m1=50
m2=60
m3=70
result = m1+m2+m3
print(result)
"""
emp_id = 10
emp_name = "surender"
m1=50
m2=60
m3=70
i1=90

#invoke by using its name
def add_marks(a,b,c):
    print("Inside add_marks")
    result = a+b+c
    print(result)
    return result

def method1():
    print("This is method1")

def method2(a,b):
    c=a+b
    print(f"value of c is {c}")

def method3():
    print("Hi")

def method4():
    print("This is method 4")
    method3()
"""
calling place
args --> it is something at the calling place , 2 and 3 are args 
parameters --> It is something at the called place(function side), a and b are paramters
a <- 2
b <- 3
hardcoded 89,78
dynamic n1
"""
r= add_marks(m1,m2,m3)
method1()
method2(89,99)
print(r)
method4()
print("program ended ")

n1= 25000
interest_rate = 7


