# 숫자 0~9로 이루어진 문자열 S
# 왼쪽->오른쪽으로 숫자 확인하여 x 혹은 +를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하기
# -> 0이나 2를 제외하고는.. 다 곱하는게 이득 아닌가?

S = input()

result = int(S[0])
for i in range(1, len(S)):
    tmpNumber = int(S[i])
    if tmpNumber == 0 or tmpNumber == 1 or result == 0 or result == 1:
        result += tmpNumber
    else:
        result *= tmpNumber

print(result)
