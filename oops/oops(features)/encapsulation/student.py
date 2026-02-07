class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
 
    def display(self):
        print("name:",self.name)
        print("marks:",self.marks)

s1=student("Riyaz",90)
s1.display()