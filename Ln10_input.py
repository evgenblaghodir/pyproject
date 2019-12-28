"""
name = input("enter your name")
print("Privet "+name)


num1 = input("enter number num1")
num2 = input("enter number num2")
print(int(num1) + int(num2))
"""
message=''
count = 0
while True:
    message = input("Enter pass")
    if (message == 'secret'):
        print("correct")
        break
    elif (message == 'exit'):
        break
    else:
        print("invalid")
        count+=1
        if (count==3):
            print("3 tymes incorect")
            break