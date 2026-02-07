class shape:
    def area(self):
        print("area of the shape")

class rectangle(shape):
    def area(self):
        l=10
        b=11
        print("area of the recatngle:",l*b)

class square(shape):
    def area(self):
        a=10
        print("area of the square:",a*a)

class circle(shape):
    def area(self):
        r=10
        print("area of the circle:",3.14*r*r)

s=shape()
r=rectangle()
sq=square()
c=circle()

s.area()
r.area()
c.area()
sq.area()
