# N: 행, M: 열
N, M = map(int,input().split())

result = 0
# for (반복문)
# for 변수 in 리스트(또는 튜플, 문자열...)
# range(1,11) 으로 숫자리스트를 만들어 줄 수도 있다 (1이상 11미만)
for i in range(N):
    listM = list(map(int,input().split(" ")))
    listM.sort()
    # if elif (조건문)
    if i == 1:
        result = listM[0]
    elif result < listM[0]:
        result = listM[0]

print(result)
