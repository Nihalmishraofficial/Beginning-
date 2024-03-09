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
obj.add(40,30)    
obj.sub(1000,100)
obj.mul(10,20)
obj.div(10,20) 
        