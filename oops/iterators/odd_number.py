class odd:
    def __init__(self,limit):
        self.limit=limit
        self.num=1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num<=self.limit:
            result=self.num
            self.num+=2
            return result
        else:
            raise StopIteration
        
odd=odd(9)
for i in odd:
    print(i)