
import sys
MOD = int(1e9+7)

def square(x,n):
    if n == 1:
        return x
    else:
        c = square(x,n//2)
        if n %2==0:
            return (c*c) % MOD
        else:
            return (c*c*x )%MOD

    
t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    # DIV = square(10,9) +7
    if n <= 2:
        print(1)
    else:
        print(square(2,n-2)%MOD)