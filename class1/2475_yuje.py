data = list(map(int,input().split()))
a = 0
for d in data:
    a+= (d)**2
print(a%10)