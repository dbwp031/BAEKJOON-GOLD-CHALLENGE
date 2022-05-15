import sys

input = sys.stdin.readline
n = int(input())
data = [0]*21
for _ in range(n):
    # print(input().split())
    s = input().strip()
    if s == 'all' or s == 'empty':
       oper = s
    else:
        oper,x = s.split()
        x = int(x) 
    if oper == 'add':
        data[x]=1
    elif oper == 'remove':
        data[x]=0
    elif oper == 'check':
        print(data[x])
    elif oper == 'toggle':
        data[x] = (data[x]+1)%2
    elif oper == 'all':
        data = [1]*21
    elif oper == 'empty':
        data = [0]*21
    # if not(s == 'all' or s == 'empty'):
    #     del x
    # del s
    # del oper
    
