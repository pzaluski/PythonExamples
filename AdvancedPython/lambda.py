"""Example 1"""
def calc(x):
    return x*2

#to samo co wyzej
calc2=lambda x:x*2

print(calc(3))
print(calc2(3))


"""Example 2"""
#lambda multiagrs
def add(x,y):
    return x+y
def minus(x,y):
    return x-y
print(add(15,5))
print(minus(15,5))


#to samo lambda
result=lambda x,y: (x+y,x-y)
print(result(15,5))