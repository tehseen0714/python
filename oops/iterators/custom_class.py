class mynumbers:
    def __init__(self,max):
        self.max=max
        self.num=1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=self.max:
            val=self.num
            self.num+=1
            return val
        else:
            raise StopIteration
        
numbers = mynumbers(7)
for n in numbers:
    print(n)
