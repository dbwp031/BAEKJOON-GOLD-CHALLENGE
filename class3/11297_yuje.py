# 최소 힙
import sys
input = sys.stdin.readline
data = []

n = int(input())

now = 0
for _ in range(n):
    x = int(input())
    if x == 0:
        if len(data)==0:
            print(0)
            continue
        else:
            print(data[0])
            data[0],data[-1]=data[-1],data[0]
            data.pop(-1)
            now = 0
            while True:
                left = now*2
                right = now*2 + 1
                
                if left >= len(data):
                    break
                elif right >= len(data):
                    son = left
                elif data[left] > data[right]:
                    son = left
                else:
                    son = right
                if data[son] > data[now]:
                    data[son],data[now]=data[now],data[son]
                    now = son
                else:
                    break
        continue

        
    data.append(x)
    now = len(data)-1
    while True:
        parent = now //2
        if data[now]>data[parent]:
            data[now],data[parent]=data[parent],data[now]
            now = parent
        else:
            break
        if now == 0:
            break
    