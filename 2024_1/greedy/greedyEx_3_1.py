# 거스름돈 종류: 500, 100, 50, 10원 (무한)
# 손님에게 거슬러 줘야할 돈이 N원일 때 동전의 최소 갯수? (단, N은 항상 10의 배수)
coinType = [500, 100, 50, 10]

# 내가 생각한 소스:  500의 나머지가 N인지 확인.. N이 아니면 몫 획득.. -> 10까지 감...
n = 1260
result = 0
for i in coinType:
    if n % i != n:  # 나누어 떨어지는지 확인
        result += n // i
        n -= (n // i) * i

# 답안..: 몫은 result에 넣고 나머지는 n에 다시 넣기..
n = 1260
result = 0
for coin in coinType:
    result += n // coin
    n %= coin

print(result)
