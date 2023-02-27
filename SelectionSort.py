n=int(input("Enter The Numbers To be inserted : "))
li=[]
for i in range (0,n):
    num = int(input("Enter The to Be Inserted = "))
    li.append(num)
print("List = ",li)

for i in range(0,len(li)):
    min=10000
    for j in range(i,len(li),1):
        if li[j]<min:
            min=li[j]
            index = j    # index value of min
    li[index],li[i]=li[i],li[index]   # Diect Swapiing
print("Selection Sorted List = ",li)