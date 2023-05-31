# 개미전사
n = int(input())
array = list(map(int, input().split()))

# 100까지 이므로 데이터값 100으로 셋팅..
d = [0] * 100
d[0] = array[0]

# 둘중의 최대값이여야 하므로..
d[1] = max(array[0], array[1])

# i-1 현재 창고 바로 앞을 털면 인접한 현재를 털지 못함
# i-2 현재 창고 앞앞을 털었으니까 현재 창고 털 수 있음 (그래서 array[i]를 더해주는것) 
# - 약탈 할 수 있는 창고의 갯수를 알려주지 않았기 때문에 많이 털수록 크니까 더해준것
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])
