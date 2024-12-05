def solution(code):
    ret = []
    mode = 0
    
    for i in range(len(code)):
        if code[i] == '1':
            mode = (mode+1)%2
            continue
        else:
            if mode==0 :
                if i % 2 == 0:
                    ret.append(code[i])
                    continue
            elif mode==1 :
                if i % 2 == 1:
                    ret.append(code[i])
                    continue
    
    if "".join(ret) == "":
        return "EMPTY"
    else: 
        return "".join(ret)