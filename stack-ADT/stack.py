class Stack(object) :
    def __init__(self,limit=10):
        self.items = []
        self.limit = limit
    def isEmpty(self) :
        return self.items == []
    def size(self) :
        return len(self.items)
    def display(self) :
        print(f"Stack Elements : {self.items}")
    def push(self,item) :
        if len(self.items) >= self.limit :
            print("Stack Overflow")
        else :
            self.items.append(item)
    def pop(self,item) :
        if len(self.items) <= self.limit :
            print('Stack Underflow')
        else :
            return self.items.pop(item)
    def peek(self) :
        if self.size() <= 0 :
            print("Stack Underflow")
        else :
           return self.items[-1]

