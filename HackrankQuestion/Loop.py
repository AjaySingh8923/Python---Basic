"""
Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example
n=3
The list of non-negative integers that are less than n =3 is [0,1,2] . Print the square of each number on a separate line.
                   0
                   1
                   4

Input Format
The first and only line contains the integer n.
Constraints
1<=n<=20

Output Format
Print n lines, one corresponding to each i.

Sample Input 0
        5
Sample Output 0
0
1
4
9
16

"""
n = int(input())
for n in range(0, n): 
      print(n*n)
"""
n = int(input())
for n in range(0, n):
      i = n ** 2
      print(i)
"""