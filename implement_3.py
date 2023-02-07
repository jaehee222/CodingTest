# 나이트의 현재 위치
X = input()

# 이동 할 수 있는 경우의 수
cnt = 0
case = [[-2, -1], [-2, 1], [2, -1], [2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2]]
tmp = ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

for i in case:
    for j in range(len(tmp)):
        # 나이트 위치 계산 하기 위해... 숫자로 바꾸기
        if X[0] == tmp[j]: break
    tmpX = int(X[1]) + i[1]
    tmpY = j + 1 + i[0]
    if (tmpX >= 1 and tmpX <= 8 and tmpY >= 1 and tmpY <= 8): cnt += 1

print(cnt)
