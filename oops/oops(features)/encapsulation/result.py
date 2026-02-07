class result:
    def __init__(self):
        self.marks=0

    def add_marks(self,marks):
     if marks<=100:
        self.marks=marks
     else:
        print("invalid marks")

    def show_marks(self):
       print("marks:",self.marks)

r=result()
r.add_marks(99)
r.show_marks() 