n = int(input())
data = list(map(int,input().split()))
data.sort()
time = 0
for i in range(n):
    time += data[i]*(n-i)
print(time)