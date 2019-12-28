def cube(number):
  print(number*number*number)

def by_three(number):
  if(number%3 == 0):
    print(cube(number))
  else:
    print("False")
number=6
cube(number)
by_three(number)