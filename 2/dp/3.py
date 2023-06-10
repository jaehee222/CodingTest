# 바닥공사
# 가로길이 n, 세로길이 2
# 1x2, 2x1, 2x2의 덮개를 이용해 채우기위한 모든 경우의 수를 796796으로 나눈 나머지

n = int(input())

d = [0] * 1001

# d[i-1] 에 1x2 놓기, d[i-2] 에 2x1 2개, 2x2 1개 놓기
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2])

print(d[n] % 796796)
