# N개의 동전을 이용하여 만들 수 없는 양의 정수금액 중 최솟값?

n = int(input())
coin = list(map(int, input().split()))
coin.sort()

result = 1
index = 0
for i in coin:
    if result < i:
        break
    result += i # 이전 ~ i까지의 조합은 다 만들 수 있다

print(result)
