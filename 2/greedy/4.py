# 1이 될때까지
# N에서 1을 뺀다.
# N을 K로 나눈다. - N이 K로 나누어 떨어질때만..
# N이 1이될때까지 수행하는 최소 횟수?

# 무조건 나눌 수 있을때 나누는 것이 이득! . 나머지를 한번에 빼주면 반복문 횟수 줄어듦
n, k = map(int, input().split())

idx = 0
tmp = 0
while True:
    if n % k == 0:
        n //= k
        idx += 1
    if n < k: # 1이거나 1보다 작을 경우..
        break
    tmp = n - n % k
    idx += n % k
    n = tmp

print(idx)
