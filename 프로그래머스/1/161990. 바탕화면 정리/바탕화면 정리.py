def solution(wallpaper):
    
    lux = len(wallpaper)
    luy = len(wallpaper[0])
    rdx = 0              
    rdy = 0            
       
    i = 0
    for s in wallpaper:
        print("i : ", i)
        ix_l = s.find('#')  # '#'의 인덱스를 찾음
        ix_r = s.rfind('#')
        if ix_l != -1:  # '#'이 문자열에 있으면
            lux = min(lux, i)  # 최소 인덱스 값 갱신
            luy = min(luy, ix_l)
            rdx = max(rdx, i)
            rdy = max(rdy, ix_r)
        print(lux, luy, rdx+1, rdy+1)
        i += 1
    
    return lux, luy, rdx+1, rdy+1