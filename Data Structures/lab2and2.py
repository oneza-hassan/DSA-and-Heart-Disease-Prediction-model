
#lab1
'''
list = [100, 25, 54, 33, 2]
max=list[0]
min=list[0]
for num in list:
    if num> max:
        max=num
for num in list:
    if num< min:
        min=num
print (max)
print(min)
'''

#lab2 online classes
'''
a=5
b=6
'''
'''
x = 'Cake'
z1 = x[2:]
print(z1)
print(str.capitalize('cookie'))
print(x.isdigit())
print(x.replace('k', "s"))
print(x)
y='ca'
print(x.find(y))
x = 4
y = 2
z = (x==y) # Comparison expression (Evaluates to false)
if z: # Conditional on truth/false value of 'z'
    print("Cookie")
else:
    print("No Cookie")
i = 4.0
print(type(i))
x = 2
y = "The Godfather: Part "
#fav_movie = y + x
#print(fav_movie) #Traceback (most recent call last)
fav_movie = y + str(x)
print(fav_movie)
x=2
y=2
print(x+y)

#type codes for python array
import array as arr
a=arr.array('H',[1,2,3])
print(a)
print(type(a)) 
        
my_array = arr.array('u', ['\u0061', '\u0062'])
print(my_array)
list_num = [1,2,45,6,7,2,90,23,435]
list_num.insert(4, 22)
print(list_num)
#Remove the first occurence
x = 'Cookie'
x=list(x)
print(x)
x.remove('o')
print(x)

z=(1+2j)
print(type(z))

print([(x, y) for x in [1,2,3] for y in [2,1,3] if x <= y])
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])

i=2
while True:
    if i%3==0:
        break
    print(i)
    i+=2

a=[10,23,56,[78]]
a[3][0]=95
a[1]=34
print(a)

#for and else block
l=["abc","z"]
for i in l:
    print(i)
    print(l)
else:
    print("the end")

#here the else block will not run since the loop was terminated early using a break statement
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed successfully")
'''
'''
l1=[1,33,22,44,31]

evennum=[i for i in l1 if i%2==0]
print(evennum)
if evennum:
    print("List contains an even number")
hasevnum=False
l=[]
for i in l1:
    print(i)
    if (i%2)==0:
        print("list contain an even num")
        print(i)
        hasevnum=True
       #break #if we put break here it will only detect the first even number and tell us if the list has even num or not
        
        l.append(i)
if not hasevnum:
    print("list doesnot contain even num")
else:
    print(l)


list=[1,33,22,44,31,44,23]

for i in range(len(list)):
    x=list[i]
    print(x)

for i in range(0,5,2):
    x=list[i]
    print(x)

i = 0
while i < 5:
    print(i)
    i += 1
print()

i = 2
while i < 5:
    print(i)
    i += 1

for i in range(7):
    j = 0
    while j < i:
        print(j, end=' ')
        j += 1
    print()
a="python"
print(min(a))

for i in range(0,3):
    print()

import array
list_input=[int(x) for x in input("enter the int input for list").strip().split(" ")]
print()
print("entered array element: ", list_input)
my_array=array.array("i",list_input)
print("display the array : ", my_array)
'''