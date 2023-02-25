li=[]
n = int(input("Total Number  to Be Inserted = "))

for i in range(0 , n ) :
    num = int(input("Enter The to Be Inserted = "))
    li.append(num)
print("List = ",li)

b=int(input("Enter The to Find In List = "))
for i in range (0,n):
    if li[i]==b :
        print("Number",i)
else :
     print("-1")
    
