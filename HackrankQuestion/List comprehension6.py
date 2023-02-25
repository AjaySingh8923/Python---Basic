
x = int(input())
y = int(input())
z = int(input())
n = int(input())
li=[]
# li = [expression for item in iterable if condition == True]
# li = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k) != n]
for i in range(x+1):
         for j in range(y+1):
             for p in range(z+1):
                 if i+j+p != n:
                     li.append([i,j,p])                  
print(li)

