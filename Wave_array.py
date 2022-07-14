a=int(input())
b=list(map(int,input().split()))
for i in range(0,len(b)-2):
    if b[i]<b[i+1] and b[i+1]>b[i+2] or b[i]>b[i+1] and b[i+1]<b[i+2]:
        continue
    else:
        print("no")
        break
else:
    print("yes")