def solution(absolutes, signs):
    li = [a if s else -a for a,s in zip(absolutes, signs)]  
    return sum(li)
        