class Multiple_of_three:
    def __init__(self,limit):
        self.limit=limit
        self.num=3

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=self.limit:
            result=self.num
            self.num+=3
            return result
        else:
            raise StopIteration

obj=Multiple_of_three(15)
for i in obj:
    print(i)