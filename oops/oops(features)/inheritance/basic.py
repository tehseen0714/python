class parent:
    def display_parent(self):
        print("this is parent class")

class child(parent):
    def display_child(self):
        print("this is child class")
obj=child()
obj.display_parent()
obj.display_child()
