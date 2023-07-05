n = int(input())
li = [str(input()) for _ in range(n)]
res = ['?' for _ in range(len(li[0]))]
for i in range(len(li[0])): # 단어 길이
	if n == 1:
		res = li
		break
	for j in range(n-1): # 단어 개수
		if li[j][i] == li[j+1][i]:
			res[i] = li[j][i]
		else: 
			res[i] = '?'
			break
print("".join(res))
