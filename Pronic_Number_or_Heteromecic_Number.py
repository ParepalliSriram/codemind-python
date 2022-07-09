a=int(input())
for i in range(0,a+1):
    if i*(i+1)==a:
        print("YES")
        break
else:
    print("NO")