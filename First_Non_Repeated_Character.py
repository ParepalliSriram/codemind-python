a=int(input())
for i in range(0,a):
    b=int(input())
    c=str(input())
    d=0
    for j in c:
        for k in c:
            if j==k:
                d+=1
        if d==1:
            print(j)
            break
        d=0
    else:
        print("-1")
        