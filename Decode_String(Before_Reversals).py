z=int(input())
for i in range(z):
    a,b=map(int,input().split())
    s1=input()
    for k in range(b-1,0,-1):
        s2=s1[0:k+1]
        s2=s2[::-1]
        s1=s1[k+1:]
        s1=s2+s1
    print(s1)