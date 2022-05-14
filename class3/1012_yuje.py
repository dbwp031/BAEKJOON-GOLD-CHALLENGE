from collections import deque
t = int(input())
dx = [-1,0,1,0]
dy=[0,1,0,-1]
for _ in range(t):
  # 가로 세로 배추개수
  m,n,k = map(int,input().split())
  
  data = [[0]*m for _ in range(n)]
  visited = [[False]*m for _ in range(n)]
  
  for _ in range(k):
    x,y = map(int,input().split())
    data[y][x]=1
    
  count = 0
  for i in range(n):
    for j in range(m):
      if data[i][j] == 1 and visited[i][j]==False:
        que = deque([[i,j]])
        visited[i][j]=True
        count +=1
        while que:
          x,y = que.popleft()
          for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<=nx<=n-1 and 0<=ny<=m-1 and data[nx][ny]==1 and visited[nx][ny]==False:
              que.append([nx,ny])
              visited[nx][ny]=True

  print(count)

  