# 곱하기 또는 더하기
# 각자리가 0~9로만 이루어진 문자열 S가 있음
# 왼쪽부터 오른쪽으로 모든 숫자 확인하며 x 또는 + 연산자를 넣어 가장 큰수를 구하는 프로그램

# 1 또는 0이 나오면 더하는게 무조건 이득, 2이상은 곱하는게 무조건 이득임
s = input()
number = int(s[0])
for i in range(1, len(s)):
    numberTmp = int(s[i])
    if numberTmp == 1 or numberTmp == 0 or number == 0:
        number += numberTmp
    else:
        number *= numberTmp

print(number)
