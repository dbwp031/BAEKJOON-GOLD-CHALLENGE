from collections import deque
a,b = map(int,input().split())
dp = [-1]*100001

que = deque([[a,0]])
dp[a] = 0

while que:
  pos, time = que.popleft()
  if pos == b:
    print(time)
    break
  if pos-1>=0 and dp[pos-1] == -1:
    dp[pos-1] = time+1
    que.append([pos-1,time+1])
  if pos+1<=100000 and dp[pos+1] == -1:
    dp[pos+1] = time+1
    que.append([pos+1,time+1])
  if pos*2<=100000 and dp[pos*2] == -1:
    dp[pos*2] = time+1
    que.append([pos*2,time+1])
