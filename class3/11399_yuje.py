# n = int(input())
# data = list(map(int,input().split()))
# data.sort()
# time = 0
# for i in range(n):
#     time += data[i]*(n-i)
# print(time)
n = int(input())
data = list(map(int,input().split()))
data.sort()
time = 0
accu = 0
for d in data:
    accu +=d
    time += accu
print(time) 