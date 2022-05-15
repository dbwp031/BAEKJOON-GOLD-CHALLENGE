from collections import deque
n = int(input())
visited = [False]*(n+1)
que=deque([[n,0]])
while que:
    num,count = que.popleft()
    
    if num == 1:
        print(count)
        break
    if not visited[num]:
        visited[num]=True
        if num%3==0:
            que.append([num//3,count+1])
        if num%2==0:
            que.append([num//2,count+1])
        que.append([num-1,count+1])