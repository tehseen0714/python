class animal:
    def sound(self):
        print("animals make sound")

class dog(animal):
    def bark(self):
        print("dog barks")

class cat(animal):
    def meow(self):
        print("cat meows")

d=dog()
d.sound()
d.bark()

c=cat()
c.sound()
c.meow()
