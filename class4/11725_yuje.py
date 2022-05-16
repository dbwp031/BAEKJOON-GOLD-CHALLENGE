import sys
input = sys.stdin.readline

n = int(input())
# 이 방법은 간선의 즉시 부모 - 자식을 결정할 수 있을 때만 성립 가능하다.
# parent = [i for i in range(n+1)]

# for _ in range(n-1):
#     a,b = map(int,input().split())
#     if a == 1 or parent[a]!= a: # a가 1이거나 a의 부모가 결정되어 있을 때
#         parent[b]= a
#     else:
#         parent[a]=b
# for i in range(2,n+1):
#     print(parent[i])

parent = [i for i in range(n+1)]

data = []
for _ in range(n-1):
    data.append(map(int,input().split()))
answer = None
def dfs(parent,i):
    global answer
    if i == len(data):
        answer = parent
        return True
    a,b=data[i]
    if a == 1 or parent[a]!= a:
        parent[b]=a
        return dfs(parent,i+1)
    elif b == 1 or parent[b]!=b:
        parent[a]=b
        return dfs(parent,i+1)
    else:
        parent[a]=b
        dfs(parent,i+1)
        parent[a]=a
        parent[b]=a
        dfs(parent,i+1)
        parent[b]=b