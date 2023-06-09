# 거스름돈 500/100/50/10 동전 무한개. 손님에게 거슬러 줘야할 돈 N원. 최소동전의 갯수 구하라
N = int(input())
coin = [500, 100, 50, 10]

result = 0
remainingChange = N
for i in coin:
    # // : 몫, %: 나머지
    result += int(remainingChange // i)
    remainingChange = remainingChange % i

print(result)
