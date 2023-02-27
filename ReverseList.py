li=[]
n = int(input("Total Number  to Be Inserted = "))

for i in range(0 , n ) :
    num = int(input("Enter The to Be Inserted = "))
    li.append(num)
print("List = ",li)
li1=[]

print("Reversing The List")
for i in range (len(li)): #len(li) calculate length of Li list
    li1.append(li[len(li)-i-1])
print(li1)
