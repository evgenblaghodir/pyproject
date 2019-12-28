def summa(x, y):
    return x+y


x=summa(3,2)
print(x)

def fact(n):
    summa=1
    for i in range(1,n+1):
        summa=summa*i
    return summa


print(fact(3))

for i in range(1, 10):
    print(str(i)+"! = " + str(fact(i)))