import math
def dist(x,y):
    return math.sqrt(x*x+y*y)
x=int(input("Enter value of x:"))
y=int(input("Enter value of y:"))
print("Distance from origin is:",dist(x,y))