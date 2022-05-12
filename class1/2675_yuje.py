t = int(input())
for _ in range(t):
    n,string = input().split()
    for s in string:
        for _ in range(int(n)):
            print(s,end='')
    print()