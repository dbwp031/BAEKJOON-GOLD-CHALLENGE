# 포켓몬 개수, 
import sys 
n,m= map(int,input().split())
dicName = {}
dicNum = {}
for i in range(1,n+1):
    s = sys.stdin.readline().strip()
    dicName[s]=i
    dicNum[i]=s
for _ in range(m):
    x = sys.stdin.readline().strip()
    if x.isdigit():
        x = int(x)
        print(dicNum[x])
    else:
        print(dicName[x])