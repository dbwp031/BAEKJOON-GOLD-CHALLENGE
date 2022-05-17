# 벨만-포드 알고리즘
# 나는 거리에서 bfs로 구하려고 했는데, 그러면 visited 오류가 나기 때문에 불가능하다.
# 이는 벨만-포드 알고리즘을 사용해 푸는 문제이다. : 가중치에 음수가 존재할 때, 한 노드에 대한 전체 노드의 최단 거리들
# 다익스트라와 다르게 가중치가 음수여도 사용가능하다.
# 매번 모든 간선을 확인하여 노드간 최단 거리를 확인해주어야 한다.

tc = int(input())
for _ in range(tc):
    n,m,w = map(int,input().split())
    if n == 1:
        print("NO")
    else:
        data = [[1e9]*(n+1) for _ in range(n+1)]
        edges = []
        for _ in range(m):
            a,b,c = map(int,input().split())
            edges.append([a,b,c])
            edges.append([b,a,c])
        for _ in range(w):
            a,b,c = map(int,input().split())
            edges.append([a,b,-c])

        temp = [int(1e9)]*(n+1)
        canWorm = False
        for i in range(1,n+1):
            distance = temp[:]
            distance[i]=0
            for a in range(1,n+1):
                for b in range(len(edges)):
                    cur_node = edges[b][0]
                    next_node = edges[b][1]
                    edge_cost = edges[b][2]

                    if distance[cur_node]!= 1e9 and distance[next_node]>distance[cur_node]+edge_cost:
                        distance[next_node]= distance[cur_node]+edge_cost
                        if a == n:
                            canWorm = True
            if canWorm:
                break
        if canWorm:
            print("YES")
        else:
            print("NO")                        


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