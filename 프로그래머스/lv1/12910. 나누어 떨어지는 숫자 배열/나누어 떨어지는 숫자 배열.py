def solution(arr, divisor):
    li = [a for a in arr if a % divisor == 0 ]
    if not li:
        li.append(-1)
    li = sorted(li)
    return li
