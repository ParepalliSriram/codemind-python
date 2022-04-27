a=int(input())
count=0
for i in range(1, a+1):
    b=1/i
    count=count+b
print(format(count,".2f"))