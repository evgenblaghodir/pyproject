import random

cars = ["BMW", "VW", "SEAT", "SKODA", "ZAZ"]

for item in cars:
    print(item.lower())

mylist = list(range(1, 10))
print(mylist)
new_mylist = []
for x in mylist:
    y=random.choice([8,4,1,8])
    x = x*y
    print(x)
    new_mylist.append(x)
print(new_mylist)
yyy=len(new_mylist)
print("count"+ str(yyy))
temp = mylist[0]
count = 0
print("---------------------")
temp = 0
min = 0
count = 0
sort_list = []
for x in range(0, len(new_mylist)):

   for y in range(0, len(new_mylist)):
        if (new_mylist[x] < new_mylist[y]):
            temp= new_mylist[x]
            new_mylist[x] = new_mylist[y]
            new_mylist[y] = temp





print("sorted")
print(new_mylist)

new_mylist2 = new_mylist[1:3]
print(new_mylist2)
cars2 = cars[-2]
print(cars)
print(cars2)
cars3 = cars[:]
cars.append("bugatti")
print(cars)
print(cars3)

