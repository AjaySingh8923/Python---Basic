"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.

"""

arry=[]
n=int(input("Number of input you want to Insert : "))
for i in range (0,n):
    ajy=int(input("Enter The Numbers : "))
    arry.append(ajy)
    
for i in range (0,n):
    if arry[0]<arry[i]:
        arry[0]=arry[i]
    elif arry[1]<arry[0] and arry[1]<arry[i] :
         arry[1]=arry[i]
print(arry[1])



"""
      *************ANOTHER METHOD**********
                   CORRECT ONE 
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

arr.sort()
count = arr.count(max(arr))

for i in range(count):
    arr.remove(max(arr))

print(arr[-1])






"""

"""
    In C
    
    
  #include <stdio.h>
  int main() {
  int n;
  double arr[100];
  printf("Enter the number of elements (1 to 100): ");
  scanf("%d", &n);

  for (int i = 0; i < n; ++i) {
    printf("Enter number%d: ", i + 1);
    scanf("%lf", &arr[i]);
  }

  // storing the largest number to arr[0]
  for (int i = 1; i < n; ++i) {
    if (arr[0] < arr[i]) {
      arr[0] = arr[i];
    }
  }

  printf("Largest element = %.2lf", arr[0]);

  return 0;
}
    """