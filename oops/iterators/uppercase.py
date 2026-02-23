class uppercase:
    def __init__(self,words):
        self.words=words
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index<len(self.words):
            result=self.words[self.index].upper()
            self.index+=1
            return result
        else:
            raise StopIteration

obj=uppercase([" python","java","c","c++"])
for word in obj:
    print(word)
