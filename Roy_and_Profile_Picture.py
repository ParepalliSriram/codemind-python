n=int(input())
a=int(input())
for i in range(0,a):
    b,c=map(int,input().split())
    if(b<n or c<n):
        print("UPLOAD ANOTHER")
    elif(b==c):
        print("ACCEPTED")
    else:
        print("CROP IT")