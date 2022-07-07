a=int(input())
b=[a]
b=list(map(int,input().split()))
if a%2!=0:
    b.append(0)
print(*b)