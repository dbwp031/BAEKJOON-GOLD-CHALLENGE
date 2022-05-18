

# 분할 정복이면 직접 과정 혹은 식 써가며 분할 제곱꼴을 찾아야 함.
# 이게 dictionary로 하면 어짜피 logn만큼만 저장하니 메모리 크게 사용하지 않음.

import sys
n = int(sys.stdin.readline().strip())
MOD = int(1e9 + 7)
# n%=MOD

dp={}
dp[0]=0
dp[1]=1
dp[2]=1
dp[3]=2
dp[4]=3
dp[5]=5
dp[6]=8

def f(n):
    if n<=6:
        return dp[n]
    if n in dp.keys():
        return dp[n]
    if n % 2 == 1:
        left = (n+1)//2
        right = (n-1)//2
        if left not in dp.keys():
            dp[left] = f(left)%MOD
        leftv = (dp[left] **2)
        if right not in dp.keys():
            dp[right]= f(right)%MOD
        rightv = (dp[right]**2)
        dp[n]=(leftv+rightv)%MOD
        return dp[n]
    if n % 2 == 0:
        left = n//2
        right = n//2-1
        if left not in dp.keys():
            dp[left]=f(left)%MOD
        leftv = (dp[left]**2)
        if right not in dp.keys():
            dp[right]= f(right)%MOD
        rightv = (2*dp[left]*dp[right])
        dp[n]=(leftv+rightv)%MOD
        return dp[n]
print(f(n))


# # 기존 dp로 풀면 O(n) => 시간 초과
# import sys
# n = int(sys.stdin.readline().strip())
# MOD = int(1e9 + 7)
# n%=MOD

# dp = [0,1,1,2,3,5,8]
# dp.extend([0]*(n))
# def f(n):
#     if n<=6:
#         return dp[n]
#     if dp[n]!=0:
#         return dp[n]
#     if n % 2 == 1:
#         left = (n+1)//2
#         right = (n-1)//2
#         if dp[left] == 0:
#             dp[left] = f(left)%MOD
#         leftv = (dp[left] **2)%MOD
#         if dp[right] == 0:
#             dp[right]= f(right)%MOD
#         rightv = (dp[right]**2)%MOD
#         dp[n]=(leftv+rightv)%MOD
#         return dp[n]
#     if n % 2 == 0:
#         left = n//2
#         right = n//2-1
#         if dp[left]==0:
#             dp[left]=f(left)%MOD
#         leftv = (dp[left]**2)%MOD
#         if dp[right] == 0:
#             dp[right]= f(right)%MOD
#         rightv = (2*dp[left]*dp[right])%MOD
#         dp[n]=(leftv+rightv)%MOD            
#         return dp[n]
# print(f(n))

# 기존 dp로 풀면 O(n) => 시간 초과
# import sys
# sys.setrecursionlimit(int(1e6))
# n = int(sys.stdin.readline().strip())
# MOD = int(1e9 + 7)
# n%=MOD
# dp = [0,1,1,2,3,5,8]
# def f(n):
#     if n<=6:
#         return dp[n]
#     if n % 2 == 1:
#         left = (n+1)//2
#         right = (n-1)//2
#         left = ((f(left))**2)
#         right = ((f(right))**2)
#         return (left+right)%MOD
#     if n % 2 == 0:
#         a = n//2
#         b = n//2 - 1
#         a = f(a)
#         b =f(b)
        
#         return (a*(a+2*b))%MOD
# print(f(n))

# import sys
# n = int(sys.stdin.readline().strip())
# MOD = int(1e9 + 7)
# dp = [0,1,1,2,3,5,8]
# def f(n):
#     if n<=6:
#         return dp[n]
#     if n % 2 == 1:
#         temp = f(n//2)
#         left = temp
#         right = temp - n//2
#         print(left,right)
#         return (2*left*right)%MOD
#     if n % 2 == 0:
#         temp = f(n//2)
#         left = temp*temp
#         right = 2*temp*(temp-n//2)
#         return (left + right)%MOD
# print(f(n))
