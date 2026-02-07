class father:
    def skill1(self):
        print("father:driving")

class mother:
    def skill2(self):
        print("mother:cooking")

class child(father,mother):
    def skill3(self):
        print("child:coding")

obj=child()
obj.skill1()
obj.skill2()
obj.skill3()
