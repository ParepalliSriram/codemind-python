a=int(input())
for i in range(0,a):
    b,c=map(int,input().split())
    for k in range(0,c+10):
        if((k*k)%c==b):
            print(k)
            break;
    else:
        print("-1")