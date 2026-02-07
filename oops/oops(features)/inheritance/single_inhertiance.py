class person:
    def __init__(self,name):
        self.name=name
    
    def show_name(self):
        print("name:",self.name)

class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll

    def show_details(self):
        print("roll no:",self.roll)

s=student("riyaz",101)
s.show_name()
s.show_details()