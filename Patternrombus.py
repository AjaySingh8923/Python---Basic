num = int(input("Enter the number "))
""" for i in range(1):
    for j in range(1):
            print("*",end="")

     
for i in range(num): 
        for j in range(num-i):
            print(" ",end="")   #   *
        for k in range(i):      #  **
             print("*",end="")  # ***  
               
        for j in range(i):
            print("",end="")   #   *
        for k in range(i):      
             print("*",end="")         
        print() 
     
for i in range(num):
    for j in range(i):
            print(" ",end="")
    for j in range(num-i):
            print("*",end="")
    for j in range(i):
            print("",end="")   #   *
    for k in range(num-i):      
            print("*",end="")         
    print() """
    
# MAIN CODE
for i in range(num-1):
        for j in range(num-i):
            print(" ",end="")
        for j in range(i+1):
            print("* ",end="")
        print()  
    
for i in range(num):
        for j in range(i+1):
            print(" ",end="")
        for j in range(num-i):
            print("* ",end="")
        print()  


        