class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "obj 1 is less than obj2"
        else:
            return "obj 2 is greater"
    def __eq__(self,other):
        if(self.a==other.a):
            return "both are equal"
        else:
            return "they are not equal"
obj1=A(3)
obj2=A(4)
print("Passed value:",obj1.a,obj2.a)
print(obj1<obj2)
obj3=A(4)
obj4=A(4)
print("Passed values:",obj3.a,obj4.a)
print(obj3==obj4)