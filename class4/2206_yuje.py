from collections import deque

n,m=map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input())))
visited = [[[False]*2 for _ in range(m)] for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

distance = int(1e9)

# x,y,broke,count
que = deque([[0,0,0,0]])
visited[0][0][0]=True
while que:
    x,y,broke,count = que.popleft()
    if x == n-1 and y == m-1:
        distance=count+1
        break
    for i in range(4):
        nx = x +dx[i]
        ny = y + dy[i]
        if 0<=nx<=n-1 and 0<=ny<=m-1:
            if data[nx][ny] == 1 and broke == 0 and not visited[nx][ny][broke]:
                que.append([nx,ny,1,count+1])
                visited[nx][ny][1]=True
            elif data[nx][ny] == 0 and not visited[nx][ny][broke]:
                que.append([nx,ny,broke,count+1])
                visited[nx][ny][broke]=True
if distance == 1e9:
    print(-1)
else:
    print(distance)



# 내가 dfs를 잘 구현 못해서인지, 애초에 안되는 것인지, dfs로는 시간초과가 뜸.
# import sys
# sys.setrecursionlimit(100000)

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]
# distance = int(1e9)
# def dfs(x,y,broke,count):
#     global n,m,distance
#     if x<0 or y<0 or x>=n or y>=m or visited[x][y]:
#         return
#     if x == n-1 and y == m -1:
#         distance = min(distance,count+1)
#     if data[x][y] == 1 and broke ==1 :
#         return
#     elif data[x][y] == 1:
#         visited[x][y]=True
#         data[x][y] = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx,ny,1,count)
#         visited[x][y]=False
#         data[x][y]=1

#     else:
#         visited[x][y]=True
#         for i in range(4):
#             nx = x +dx[i]
#             ny = y+ dy[i]
#             dfs(nx,ny,broke,count+1)
#         visited[x][y]=False


         

# n,m=map(int,input().split())
# data = []
# for _ in range(n):
#     data.append(list(map(int,input())))
# visited = [[False]*(m) for _ in range(n)]

# dfs(0,0,0,1)

# if distance == 1e9:
#     print(-1)
# else:
#     print(distance)

# n,m=map(int,input().split())
# data = []
# for _ in range(n):
#     data.append(list(map(int,input())))
# visited = [[[False]*2 for _ in range(m)] for _ in range(n)]

# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# distance = int(1e9)

# def dfs(x,y,broke,count):
#     global n,m,distance
#     if x<0 or y<0 or x>=n or y>=m or visited[x][y][broke]:
#         return
#     if x == n-1 and y == m -1:
#         distance = min(distance,count+1)
#     if data[x][y] == 1 and broke ==1:
#         return
#     elif data[x][y] == 1:
#         visited[x][y][broke]=True
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             dfs(nx,ny,1,count)
#         visited[x][y][broke]=False

#     else:
#         visited[x][y][broke]=True
#         for i in range(4):
#             nx = x +dx[i]
#             ny = y+ dy[i]
#             dfs(nx,ny,broke,count+1)
#         visited[x][y][broke]=False


# dfs(0,0,0,1)

# if distance == 1e9:
#     print(-1)
# else:
#     print(distance)