class calculator:
    def sum(self,a,b):
        print("Sum=",a+b)
    def sub(self,a,b):
        print("sub=",a-b)    
    def mul(self,a,b):
        print("mul=",a*b) 
    def div(self,a,b):
        print("div=",a/b)    
        
ajay=calculator() #object = Call class
a=int(input("enter first num = "))
b=int(input("enter first numb = "))

c=input("enter your operation you want to perform +,-,/,* =")
if c == "+" :
    ajay.sum(a,b)  
elif c == "-" :
    ajay.sub(a,b)  
elif c == "*" :
    ajay.mul(a,b)  
elif c == "/" :
    ajay.div(a,b)    
else :
    pass                
        