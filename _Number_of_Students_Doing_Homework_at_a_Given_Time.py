a=int(input())
l=list(map(int,input().split()))
b=int(input())
l1=list(map(int,input().split()))
c=int(input())
count=0
for i in range(0,a):
    if(l1[i]>=c and l[i]<=c):
        count+=1
print(count)