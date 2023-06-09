# 큰 수의 법칙..
# 주어진 수를 M번 더해 가장 큰수를 만든다. (N: 주어진 숫자의 갯수)
# 특정한 수는 연속으로 K번까지만 더할 수 있다.

n, m, k = map(int, input().split())
array = list(map(int, input().split()))

# k+1을 하나의 덩어리로 생각.. 덩어리는 가장 큰 숫자 k개 두번째로 큰 숫자 1개로 구성.
# 나머지는 모두 가장 큰 숫자로 구성함.

# 정렬.
array.sort()
max_number = array[n - 1]
secMax_number = array[n - 2]

result = (m // (k + 1)) * ((max_number * k) + secMax_number) + (m % (k + 1) * max_number)

print(int(result))
