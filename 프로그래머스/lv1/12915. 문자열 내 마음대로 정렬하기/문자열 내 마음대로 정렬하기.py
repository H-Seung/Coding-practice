def solution(strings, n):
    strings.sort()
    for i in range(1, len(strings)):
        for j in range(i,0,-1):
            if strings[j][n] < strings[j-1][n]:
                strings[j], strings[j-1] = strings[j-1], strings[j]
    return strings
