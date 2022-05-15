# 피보나치 다이나믹 테이블
# dp = [-1]*41
# dp[0]=0
# dp[1]=1
# t = int(input())
# def fibo(n):
#     print(dp)
#     if n == 0:

#         return 0
#     elif n==1:
#         return 1
#     if dp[n]!= -1:
#         return dp[n]
#     dp[n] = fibo(n-1)+fibo(n-2)
#     return dp[n]
    
# for _ in range(t):
#     cnt0=cnt1=0
#     n = int(input())
#     fibo(n)
#     print(cnt0,cnt1)

dp=[[0,0] for _ in range(41)]
dp[0]=[1,0]
dp[1]=[0,1]

for i in range(2,41):
    dp[i][0]=dp[i-1][0]+dp[i-2][0]
    dp[i][1]=dp[i-1][1]+dp[i-2][1]
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n][0],dp[n][1])
