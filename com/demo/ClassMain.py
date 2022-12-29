#self --> current instance or current obj
id = 256145

def add(a,b):
    return a+b

class Employee:
    emp_name = "surender"

    def __init__(self,a):
        self.emp_name = a

    def method1(self,d):
        print("This is method 1")
        print(d)

if __name__ == "__main__":
   data = 999
   r = add(2,3)
   print(r)
   obj1 = Employee("surender") # object creation __init__ default #constructor
   print(obj1.emp_name)
   obj1.method1(data)#999
   obj2 = Employee("raja")
   print(obj2.emp_name)
   obj2.method1(9+90)