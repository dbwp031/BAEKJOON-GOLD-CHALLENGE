import sys
from collections import deque
input =sys.stdin.readline

v = int(input())
data = [[] for _ in range(v+1)]
for _ in range(v):
    temp = list(map(int,input().split()))
    left = temp[0]
    for i in range(1,len(temp)-1,2):
        right = temp[i]
        dist = temp[i+1]
        data[left].append([right,dist])
far_node = None
def bfs(start_node):
    global far_node
    distance = 0
    visited = [False]*(v+1)
    que = deque([[start_node,0]])
    visited[start_node]=True
    while que:
        now_node,now_dist = que.popleft()
        for child,child_dist in data[now_node]:
            if not visited[child]:
                visited[child]=True
                temp_dist = now_dist + child_dist
                if distance < temp_dist:
                    distance=temp_dist
                    far_node = child
                que.append([child,temp_dist])
    return distance
bfs(1)
print(bfs(far_node))            