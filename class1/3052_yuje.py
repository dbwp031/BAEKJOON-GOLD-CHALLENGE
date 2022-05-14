data = [0]*42
count=  0
for _ in range(10):
    n = int(input())
    if data[n%42] ==0:
        count+=1
        data[n%42]=1
print(count)