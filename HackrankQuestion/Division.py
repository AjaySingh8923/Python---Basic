"""
   Task
The provided code stub reads two integers,  and , from STDIN.

Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

No rounding or formatting is necessary.

Example
a=3
b=5

The result of the integer division a//b==0
The result of the float division is a//b=1.33 

"""
a = int(input("ENTER FIRST NUMBER : "))
b = int(input("ENTER SECOND NUMBBER :"))
d=a//b #Floor division
e=a/b
print(d)
print(e)
