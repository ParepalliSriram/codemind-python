a=int(input())
arr=list(map(int,input().split()))
b=arr[0]
c=0
while(1):
    for i in range(0,a):
        if(arr[i]%b==0):
             c+=1;
    if(c==a):
      print(b)
      break
    c=0
    b-=1