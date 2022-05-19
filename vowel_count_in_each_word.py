a=str(input())
c=0
for element in a:
    if element=='a' or element=='e' or element=='i' or element=='o' or element=='u':
        c+=1
    if element==' ':
        print(c,end=' ')
        c=0
print(c)