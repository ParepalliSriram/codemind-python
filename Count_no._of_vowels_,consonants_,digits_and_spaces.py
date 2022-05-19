a=str(input())
V=0
C=0
D=0
S=0
for i in a:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        V+=1
    elif i.isnumeric():
        D+=1
    elif i==' ':
        S+=1
    else:
        C+=1
print("Vowels:",V)
print("Consonants:",C)
print("Digits:",D)
print("White spaces:",S)