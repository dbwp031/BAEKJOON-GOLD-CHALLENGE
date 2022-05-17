# 2차원 dp 그래프 그려서 머리대로(논리대로?) 먼저 표를 작성한 후, 점화식을 유도해냈다.

a = input()
b = input()
if len(a)==0 or len(b) ==0:
    print(0)
else:
    dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

    for i in range(1,len(a)+1):
        for j in range(1,len(b)+1):
            if a[i-1]==b[j-1]:
                # 위 -> 아래: 위에거 / 왼 -> 오: 왼쪽꺼 / 대각선: 현재 인덱스 추가
                dp[i][j] = max(dp[i-1][j-1]+1,dp[i][j-1],dp[i-1][j])
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    # for d in dp:
    #     print(d)
    print(dp[len(a)][len(b)])