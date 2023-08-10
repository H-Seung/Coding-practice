def solution(a, b):
    M=[31,29,31,30,31,30,31,31,30,31,30,31]
    result = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    n = (sum(M[:a-1])+b)%7
    return result[n]

import datetime
a=5 
b=24
t = 'MON TUE WED THU FRI SAT SUN'.split()
print(t[datetime.datetime(2016, a, b).weekday()])