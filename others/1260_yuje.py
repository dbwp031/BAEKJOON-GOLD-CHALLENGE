from collections import deque
# dfs에 대한 탈출조건, 변수 설정하는 데에 어려움을 겪고 있다.
n,m,v= map(int,input().split())
data = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)
for i in range(n+1):
    data[i]=sorted(data[i])

#dfs()
visited = [False]*(n+1)
def dfs(node):
    if visited[node]:
        return
    print(node,end = ' ')
    visited[node]=True # 얘는 들어가고 나서(출력하고 나서) visited 처리
    for next in data[node]:
        if not visited[next]:
            dfs(next)
dfs(v)
print()
# bfs
visited = [False]*(n+1)
que = deque([v])
visited[v]=True
while que:
    node = que.popleft()
    print(node,end=' ')
    for next in data[node]:
        if not visited[next]:
            que.append(next)
            visited[next]=True # 얘는 들어가기 전에(출력학 전에) visited 처리


