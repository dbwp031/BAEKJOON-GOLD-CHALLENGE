# 기존 dp로 풀면 O(n) => 시간 초과
import sys
n = int(sys.stdin.readline().strip())
MOD = int(1e9 + 7)
n %= MOD

dp = [0]* (n+1)
dp[0]= 0
dp[1]= 1
def f(n):
    print(n)
    if n == 1 or n == 2:
        return 1
    if dp[n]!=0:
        return dp[n]
    dp[n]=f(n-1)+f(n-2)
    return dp[n]
print(f(n))