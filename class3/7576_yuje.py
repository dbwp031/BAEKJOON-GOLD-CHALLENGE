from collections import deque
m,n =map(int,input().split())
data = []
for _ in range(n):
  data.append(list(map(int,input().split())))
# visited = [[False]*m for _ in range(n)]

que = deque()
for i in range(n):
  for j in range(m):
    if data[i][j]==1:
      que.append([i,j,0])
      # visited[i][j]= True
dx = [-1,0,1,0]
dy = [0,1,0,-1]
last_day = 0
while que:
  x,y,day = que.popleft()
  last_day = day
  for d in range(4):
    nx = x + dx[d]
    ny = y + dy[d]
    if 0<=nx<=n-1 and 0<=ny<=m-1 and data[nx][ny]==0:
      data[nx][ny]=1
      que.append([nx,ny,day+1])

all1 = True
for i in range(n):
  for j in range(m):
    if data[i][j]==0:
      all1=False
      break
if all1 == True:
  print(last_day)
else:
  print(-1)
  