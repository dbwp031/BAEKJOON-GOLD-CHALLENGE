import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = []
for _ in range(n):
    data.append(list(map(int,input().split())))
dp = [[0]*n for _ in range(n)]

dp[0][0]=data[0][0]

for i in range(1,n):
    dp[0][i] = dp[0][i-1]+data[0][i]
for j in range(1,n):
    dp[j][0] = dp[j-1][0]+data[j][0]
for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]+data[i][j]


for _ in range(m):
    a,b,c,d = map(int,input().split())
    a-=1
    b-=1
    c-=1
    d-=1
    if b-1<0 and a-1<0:
        print(dp[c][d])
    elif  b-1<0:
        print(dp[c][d]-dp[a-1][d])
    elif a-1<0:
        print(dp[c][d]-dp[c][b-1])
    else:
        print(dp[c][d]-dp[c][b-1]-dp[a-1][d]+dp[a-1][b-1])
