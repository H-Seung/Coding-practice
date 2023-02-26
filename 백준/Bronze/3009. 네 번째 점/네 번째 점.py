import sys

data = [tuple(map(int,sys.stdin.readline().split())) for _ in range(3)]
x_ls = [data[i][0] for i in range(3)]
y_ls = [data[i][1] for i in range(3)]

for i in range(3):
    if x_ls.count(x_ls[i]) == 1:
        x = x_ls[i]
    if y_ls.count(y_ls[i]) == 1:
        y = y_ls[i]
print(f'{x} {y}')