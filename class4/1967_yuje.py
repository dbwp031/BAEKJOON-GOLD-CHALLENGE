# import sys
# from collections import deque
# input = sys.stdin.readline
# n = int(input())
# if n == 1:
#     print(0)
# else:
#     data = [[] for _ in range(n+1)]
#     for _ in range(n-1):
#         # 부모, 자식, 거리
#         a,b,c = map(int,input().split())
#         data[a].append([b,c])
#     level = []
#     que = deque([[1,1]])
#     # node , level
#     level.append([1,1])
#     # 각 노드의 level을 구해줌. (BFS)
#     while que:
#         node,now_level =que.popleft()
#         for child,_ in data[node]:
#             level.append([child,now_level+1])
#             que.append([child,now_level+1])
#     level.sort(key=lambda x:-x[1])
#     # print(max_level)
#     # 각 노드에 대한 현 노드 ~ 말단 노드(leaf) 까지의 최대 거리 구함.
#     # max_length 구함.(지름)
#     dp = [0]*(n+1)
#     max_length = 0
#     for node,node_level in level:
#         temp = []
#         if len(data[node])==0:
#             continue
#         for child,child_length in data[node]:
#             temp.append(dp[child]+child_length)
#             # 만약 자식 노드가 두개 이상이라면 가장 긴 두 지름을 구해서 더해보고 최대 지름을 구한다.
#             if len(temp)>=2:
#                 temp.sort(reverse=True)
#                 a,b=temp[0],temp[1]
#                 max_length = max(max_length,a+b)
#         dp[node]=temp[0]
#         # 만약 자식 노드가 한 줄기라면, 현재 최대 지름과 말단 ~ 현 노드의 길이를 비교한다.
#         if len(temp)==1:
#             max_length = max(max_length,dp[node])
#     # if max_length == 0:
#     #     print(dp[1])
#     print(max_length)

# BFS
# from collections import deque
# max_node = -1
# def bfs(start_node):
#     global n, max_node
#     visited =[False]*(n+1)
#     que = deque([[start_node,0]])
#     visited[start_node]=True
#     max_dist = 0

#     while que:
#         now, now_dist = que.popleft()
#         for child,child_dist in data[now]:
#             if not visited[child]:
#                 visited[child]=True
#                 que.append([child,now_dist+child_dist])
#                 if max_dist < now_dist+child_dist:
#                     max_dist = now_dist+child_dist
#                     max_node = child
#     return max_dist
                
# n = int(input())
# if n == 1:
#     print(0)
# else:
#     data = [[] for _ in range(n+1)]
#     for _ in range(n-1):
#         # 부모, 자식, 거리
#         a,b,c = map(int,input().split())
#         data[a].append([b,c])
#         data[b].append([a,c])
#     bfs(1)
#     print(bfs(max_node))

# DFS
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
maxDist = 0
for _ in range(n-1):
    a,b,c = map(int,input().split())
    tree[a].append((b,c))

def dfs(n,d):
    left,right = 0,0
    for toNode, w in tree[n]:
        r = dfs(toNode,w)
        if left<=right:
            left =max(left,r)
        else:
            right = max(right,r)
    global maxDist
    maxDist = max(maxDist,left+right)
    return max(left+d,right+d)
dfs(1,0)
print(maxDist)