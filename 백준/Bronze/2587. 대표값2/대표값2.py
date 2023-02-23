import sys
import math

len_data = 5
data = [int(sys.stdin.readline()) for _ in range(len_data)]
data.sort()
print(sum(data)//len_data)
print(data[math.ceil(len_data/2-1)])