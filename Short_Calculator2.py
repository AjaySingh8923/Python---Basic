# init method
class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print(self.a,self.b)
    def sum(self):
        return self.a+self.b
ajay=calculator(5,7)
print(ajay.sum())



# class calculator:
#     a=0
#     b=0
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def mul(self,a,b):
#         return a*b
#     def div(self,a,b):
#         return a+b    
    
# ajay=calculator()
# object = Call class
#  a=int(input("enter first num = "))
#  b=int(input("enter first numb = "))
#  ajay.a=a
#  ajay.b=b
# print(ajay.sum())
#  init method

