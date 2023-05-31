n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if (d[j - array[i]] != 10001): # array 끼리의 연산으로 만들어 질 수 있는 숫자인지의 여부
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)   #m원 만드는 방법 없을 때
else:
    print(d[m])
