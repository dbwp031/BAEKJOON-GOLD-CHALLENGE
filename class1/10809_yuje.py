string = input()
eng = [-1]*26
for i,s in enumerate(string):
    if eng[ord(s)-ord('a')] == -1:
        eng[ord(s)-ord('a')] = i

for e in eng:
    print(e,end=' ')