n = int(input()) #1~1000
li = []
if n>=1 and n<=1000:
    for i in range(1,abs(n+1)):
        li.append(int(input()))
    li = sorted(li)
else:
    raise ValueError
for i in range(n):
    print(li[i])