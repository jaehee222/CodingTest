N, K = map(int, input().split())

cnt = 0
tmp = 0
while True:
    # K에 나누어 떨어지는 숫자로 만듬
    tmp = (N // K) * K
    # 나머지.. 나누어 떨어진다면 N-tmp는 0이 됨
    cnt += N - tmp

    # N은 나누어 떨어지는 숫자가 됐으므로 tmp와 값이 같아진 상태..
    N = tmp

    # 나머지만 남게 될 경우
    if N < K: break

    N = N//K
    cnt += 1

#N은 나머지의 값이 되었으므로.. 1로 만들어준다고 생각
cnt += (N - 1)
print(int(cnt))
