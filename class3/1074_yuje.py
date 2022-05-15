n,r,c= map(int,input().split())

line = 2**(n-1)
block = line*line
answer = 0
while True:
    if line == 0:
        break
    cnt =( r // line ) * 2 + (c // line)
    answer += block*cnt
    r %=line
    c %=line
    line //=2
    block = line*line
# answer += 
print(answer)