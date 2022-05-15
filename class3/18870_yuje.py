import sys
n = int(input())
data = list(map(int,sys.stdin.readline().strip().split()))
sorted_data = sorted(data)
dic = {}
count = 0
before = None
for i in range(n):
    item = sorted_data[i]
    if before == item:
        continue
    else:
        dic[item] = count
        count+=1
        before = item
for d in data:
    print(dic[d],end=' ')