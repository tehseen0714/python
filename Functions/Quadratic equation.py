import math
def quad_roots(a,b,c):
    d=b*b-4*a*c
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    return root1,root2
a=int(input("Enter the value for a:"))
b=int(input("Enter the value for b:"))
c=int(input("Enter the value for c:"))
r1,r2=quad_roots(a,b,c)
print("root 1:",r1)
print("root 2:",r2)