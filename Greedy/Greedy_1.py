# 공백으로 숫자 구분하기
# map(f,iterable) : 함수 f와 반복 가능한 자료형(iterable)을 입력받아서 자료형의 각 요소를 f가 수행한 결과를 묶어서 돌려줌
N,M,K = map(int, input().split(' '))

# N개의 자연수를 입력받음
# list : 반복 가능한 자료형을 입력받아 리스트로 돌려줌
arrN = list(map(int,input().split(' ')))

# sort : 리스트 정렬
arrN.sort()

# 가장 큰 수
max = arrN[len(arrN)-1]

# 두번째로 큰 수
max2 = arrN[len(arrN)-2]

maxCnt = M/(K+1)*K
maxCnt += M%(K+1)

result = int((maxCnt * max) + ((M-maxCnt)*max2))

print(result)
