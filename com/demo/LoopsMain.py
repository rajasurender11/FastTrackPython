#while
#for loop

def print_Hi():
    print("HI")


n=0
while(n<3):# n= 0 0<3 n= 1 1<3 n =2  n = 3
    print_Hi()
    n =n+1

n1 = 3 #6
result = 0
i = 1
while(i<=n1): #1<=3 true  result = 1 i = 2 2<=3
  result = result +i
  i= i+1
print(f"result is {result}")
print("program ends ")

my_list = [2,3,4,8,9]
print(len(my_list))
len_of_list = len(my_list)
i =0
sum_total = 0
while(i<len_of_list):#0<5 1<5 2<5 3<5 4<5 5<5(faalse)
    sum_total = sum_total+my_list[i]
    i=i+1

print(sum_total)

print("**************FOR********************")
s_total =0
for i in my_list:
    print(i)
    s_total = s_total +i
print(f"s_total {s_total}")

my_num_list = [87,6,3,22]

for i in my_num_list:
    if(i%2 == 0):
        print(f"{i} is EVEN")
    else:
        print(f"{i} is ODD")

my_range = list(range(10))
print(my_range)

my_range1 = list(range(2,50,2))
print(my_range1)


if(len(my_num_list)<=3):
    for i in my_num_list:
        print(i)

print(__name__)

