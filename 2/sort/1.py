# 위에서 아래로
# 큰수부터 작은수의 순서로 정렬
n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array, reverse=True)

for i in array:
    print(i, end=' ')
