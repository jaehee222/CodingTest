# 만들 수 없는 금액
# 동빈이는 N개의 동전을 가지고 있다.
# 동빈이가 만들 수 없는 양의 정수의 최솟값?
n = int(input())
data = list(map(int, input().split()))

data.sort()

result = 1
for i in data:
    # result가 i보다 작으면 만들 수 없는 숫자임
    if result < i:
        break
    result += i # i를 더해주는 이유는.. 이전과 i까지는 이전 조합으로 다 만들 수 있기때문..

print(result)
