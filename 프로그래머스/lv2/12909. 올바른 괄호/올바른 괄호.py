def solution(s):
    left=[]
    right=[]
    li=list(s)
    for i in range(len(li)):
        if li[i]=="(":
            left.append("(")
        else:
            right.append(")")
        if len(left)>0 and len(right)>0:
            left.pop()
            right.pop()
        if len(left)<len(right):
            print(i,left,right)
            return False
    if len(left)==len(right):
        return True
    return False