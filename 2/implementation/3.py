# 왕실의 나이트
# 8x8 평면이며 나이트는 2가지 형태로만 이동가능
# 수평으로 두칸이동, 수직으로 한칸이동
# 수직으로 두칸이동, 수평으로 한칸이동.
# 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수

# 나이트가 이동할 수 있는 좌표..?
plan = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

nite = input()
x = ord(nite[0]) - 96 # 아스키코드를 숫자로 변환 a: 97
y = int(nite[1])
result = 0
for i in plan:
    tmpX = x + i[0]
    tmpY = y + i[1]
    if tmpX > 0 and tmpX <= 8 and tmpY > 0 and tmpY <= 8:
        result += 1

print(result)
