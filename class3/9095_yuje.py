# bfs 혹은 dfs로 구현 가능할듯
from collections import deque
t = int(input())
for _ in range(t):
    count = 0
    n = int(input())
    # bfs 로 구현
    que = deque([n])
    while que:
        node = que.popleft()
        for i in range(1,4):
            if node - i > 0:
                que.append(node-i)
            elif node - i == 0:
                count+=1
    print(count)
