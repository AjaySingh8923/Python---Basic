n = int(input("Enter the Number : "))
"""
#  METHOD 1
if n%2!=0 :
   print("Weird")
else :
    if n >= 2 and n <= 5:
        print ("Not Weird" )
    elif n >= 6 and n <= 20:
        print ("Weird")
    elif n > 20:
        print ("Not Weird")
"""
# METHOD 2
if n%2 ==0 :
    if n >= 2 and n <= 5:
        print ("Not Weird" )
    elif n >= 6 and n <= 20:
        print ("Weird")
    elif n > 20:
        print ("Not Weird")
else :
   print("Weird")

