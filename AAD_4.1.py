# a female rabbit generates a new pair at every second month.
# How many pairs there will be by end of year.

import sys
sys.setrecursionlimit(10000000)
print("The recursion limit: ",sys.getrecursionlimit())

count = 0
def pair(n):
    global count
    count += 1
    if n <= 1:
        return n
    else:
        return pair(n-1)+pair(n-2)

num = int(input("Enter no. of months: "))
print("No. of pairs are",pair(num))
print("No. of count is ", count)






def pair(n2):
    r0=0
    r1=1
    count = 0
    for i in range(n2):
        r0,r1= r1, r0+r1
        count += 1
    print("No. of pairs are ",r0)
    print("No. of count is ",count)
num2 = int(input("Enter no. of months: "))
pair(num2)
print("The result is stated above")
