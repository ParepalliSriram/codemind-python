a=int(input())
def pal(a):
    c=0
    while a!=0:
        b=a%10
        a=a//10
        c=c*10+b
    return c
from array import *
arr=array("i",[])
for i in range(0,a):
    x=int(input())
    arr.append(x)
for i in range(0,a):
    if arr[i]==pal(arr[i]):
        print("True")
    else:
        print("False")