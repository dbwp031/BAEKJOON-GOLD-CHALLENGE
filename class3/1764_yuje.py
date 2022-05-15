# # 듣도 / 보도
# import sys
# import heapq
# input = sys.stdin.readline

# n,m = map(int,input().split())

# heard = []
# see = []
# for _ in range(n):
#     x = input()
#     heapq.heappush(heard,[x,x])
# for _ in range(m):
#     x = input()
#     heapq.heappush(see,[x,x])

# h=s=None
# count = 0
# print(heard)
# while heard and see:
#     if h == None and s == None:
#         h = heapq.heappop(heard)
#         s = heapq.heappop(see)
#     if h == s:
#         count +=1
#     elif h < s:
#         h = heapq.heappop(heard)
#     else:
#         s = heapq.heappop(see)
# print(count)

# 듣도 / 보도
import sys
import heapq

input = sys.stdin.readline

n,m = map(int,input().split())

heard = []
see = []

for _ in range(n):
    heard.append(input().strip())
for _ in range(m):
    see.append(input().strip())
heard.sort()
see.sort()
hi = 0
si = 0

count = 0
data = []
while hi<len(heard) and si<len(see):
    if heard[hi] == see[si]:
        data.append(heard[hi])
        count +=1
        hi+=1
        si+=1
        continue
    elif heard[hi] < see[si]:
        hi+=1
    else:
        si+=1
print(count)
for d in data:
    print(d)