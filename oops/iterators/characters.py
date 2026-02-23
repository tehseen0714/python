class character:
    def __init__(self,text):
        self.text=text
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index<len(self.text):
            result=self.text[self.index]
            self.index+=1
            return result
        else:
            raise StopIteration

obj=character("hello")
for ch in obj:
    print(ch)
