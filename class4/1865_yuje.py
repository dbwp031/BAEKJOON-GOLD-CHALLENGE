# 벨만-포드 알고리즘
# 나는 거리에서 bfs로 구하려고 했는데, 그러면 visited 오류가 나기 때문에 불가능하다.
# 이는 벨만-포드 알고리즘을 사용해 푸는 문제이다. : 가중치에 음수가 존재할 때, 한 노드에 대한 전체 노드의 최단 거리들
# 다익스트라와 다르게 가중치가 음수여도 사용가능하다.
# 매번 모든 간선을 확인하여 노드간 최단 거리를 확인해주어야 한다.
# 이게 모든 정점의 시작점을 0으로 설정하면 모든 노드에 대한 순환을 파악할 수 있네? 대신 최단거리는 파악하지 못하고, 순환만 파악할 수 있네?
# 왤까?ㅋㅋ
tc = int(input())
for _ in range(tc):
    n,m,w = map(int,input().split())
    edges = []
    for _ in range(m):
        a,b,c=map(int,input().split())
        edges.append([a,b,c])
        edges.append([b,a,c])
    for _ in range(w):
        a,b,c = map(int,input().split())
        edges.append([a,b,-c])
    INF = int(1e9)
    distance = [0]*(n+1)
    # 어느 노드에서 하더라도 n번째 업데이트 있따 => 순환 있다.
    orbit = False
    distance[1]=0                     
    for node in range(1,n+1):
        for edge in edges:
            s,e,dist = edge
            if distance[s]!=INF and distance[e]>distance[s]+dist:
                distance[e]=distance[s]+dist
                if node == n:
                    orbit = True
    if orbit:
        print("YES")
    else:
        print("NO")
    print(distance)


# from collections import deque


# tc = int(input())

# def bfs(target):
#     # 노드 시간
#     visited = [False]*(n+1)
#     que = deque([[target,0]])
#     visited[target]=True
#     start_flag = True
#     while que:
#         node, time = que.popleft()
#         print(node,time)
#         if node == target and start_flag == False:
#             return time
#         if start_flag:
#             start_flag == False
#         for i in range(1,n+1):
#             if data[node][i] !=1e9 and not visited[i]:
#                 que.append([i,time+data[node][i]])
#                 visited[i]=True
#     return 1e9
# for _ in range(tc):
#     n,m,w = map(int,input().split())
#     data = [[1e9]*(n+1) for _ in range(n+1)]
#     for _ in range(m):
#         a,b,c = map(int,input().split())
#         data[a][b]=min(data[a][b],c)
#         data[b][a]=min(data[b][a],c)
#     for _ in range(w):
#         a,b,c = map(int,input().split())
#         data[a][b]=min(data[a][b],-c)
#     canWorm = False
#     for i in range(1,n+1):
#         print(f"bfs({i}):",bfs(i))
#         if bfs(i) <0:
#             canWorm=True
#             break
#     if canWorm:
#         print('YES')
#     else:
#         print('NO')            