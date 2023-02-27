# First method is Iteration method

# Second Recursion = when a Function Call Itself
def factorial(num):
    if num == 1:   # Base Condition
        return 1
    else:
        return num*factorial(num-1)

num=int(input("Enter Num = "))
print("Factorial = ",factorial(num))

# m=list(input("number"))
# print (m)                          STRING LIST