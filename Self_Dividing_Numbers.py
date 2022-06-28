def s_d_n(a):
    b=a
    while a:
        c=a%10
        a=a//10
        if b%c!=0:
            return 0
            break
    return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if i<10:
        print(i,end=' ')
    elif i%10==0:
        continue
    else:
        if s_d_n(i):
            print(i,end=' ')