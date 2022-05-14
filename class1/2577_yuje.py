a = 1
for _ in range(3):
    a*=int(input())
data =[0]*10
while a >0:
    data[a%10]+=1
    a = a//10
for d in data:
    print(d)