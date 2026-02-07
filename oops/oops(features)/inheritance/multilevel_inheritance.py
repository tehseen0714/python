class grandparent:
    def grand(self):
        print("grandparent class")

class parent(grandparent):
    def pt(self):
        print("parent class")

class child(parent):
    def chld(self):
        print("child class")

obj=child()
obj.grand()
obj.pt()
obj.chld()