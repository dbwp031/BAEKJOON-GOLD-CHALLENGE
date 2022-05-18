n,m = map(int,input().split())
edges = []
for _ in range(m):
    edges.append(list(map(int,input().split())))
INF = int(1e9)
distance = [INF]*(n+1)
distance[1]=0
orbit = False

for node in range(1,n+1):
    for edge in edges:
        s,e,dist = edge
        if distance[s] != INF and distance[e]>distance[s]+dist:
            distance[e]=distance[s]+dist
            if node == n:
                orbit = True
if orbit == True:
    print(-1)
else:
    for i in range(2,n+1):
        if distance[i]==INF:
            print(-1)
        else:
            print(distance[i])