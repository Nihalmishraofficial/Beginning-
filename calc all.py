class calc:
    a=10
    b=20
    def add(self,a,b):
        self.a=a
        self.b=b
        print(self.a+self.b)
    def sub(self,a,b):
        self.a=a
        self.b=b
        print(self.a-self.b)
    def mul(self,a,b):
        self.a=a
        self.b=b
        print(self.a*self.b)
    def div(self,a,b):
        self.a=a
        self.b=b
        print(self.a/self.b)
obj=calc()
obj.add()    
obj.sub()
obj.mul()
obj.div() 
        
