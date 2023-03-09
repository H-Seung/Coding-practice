def solution(n):
    cnt = 0 # 방법의 수
    for i in range(1,n//2+1):  # 시작점
        tmp_res = i
        for j in range(i+1,n//2+2):  # 나머지 더하는 부분들
            tmp_res += j
            if tmp_res == n:
                cnt += 1
                continue
            if tmp_res > n:
                break
    cnt += 1
    return cnt