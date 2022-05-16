n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int,input())))
visited = [[False]*n for _ in range(n)]

dx = [-1,0,1,0]
dy = [0,1,0,-1]

idx = 0
result = []
def dfs(x,y,house_num):
    if (not (0<=x<=n-1 and 0<=y<=n-1) )or visited[x][y]:
        print(x,y)
        global idx
        house_num -=1
        result[idx]=house_num
        return
    visited[x][y]=True
    for i in range(4):
        dfs(x+dx[i],y+dy[i],house_num+1)
        
result = []
count = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == 1 and visited[i][j]==False:
            count+=1
            result.append(0)
            dfs(i,j,0)
            idx+=1
print(count)
for i in result:
    print(i)