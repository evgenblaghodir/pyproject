"""x = 25
num = input("enter num ")
print(num)
if (x==num):
    print ("correct")
else:
    print("wrong\n")
age = input("enter age\t")
print(age)
if (int(age) <= 4 ):
    print("baby")
elif(int(age) > 4 and int(age) <= 12):
    print("child")
elif(int(age) >12 and int(age) <=21):
    print("tenager")
else:
    print("you are big")
"""
german_cars = ["bmw", "opel", "audi", "vw"]
all_cars = ["ford", "land rover", "jeep", "vw", "seat", "bmw", "opel", "audi", "bugatti"]

if 'lada' in all_cars:
    print ("yes")
else:
    print ("no")
for item in all_cars:
    if item in german_cars:
        print(item +" german car")
    else:
        print(item + " not german car")