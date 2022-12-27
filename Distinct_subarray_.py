a=int(input())
b=int(input())
l=[]
count=0
for i in range(a,b+1):
    l.append(i)
for i in range(0,len(l)):
    for k in range(0,len(l)):
        if(sum(l[i:k+1])%2!=0):
            count+=1
print(count)