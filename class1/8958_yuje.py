n = int(input())
for _ in range(n):
    string = input()
    score = 0
    count = 0
    for s in string:
        if s == "O":
            count+=1
            score +=count
        else:
            count = 0
    print(score)    