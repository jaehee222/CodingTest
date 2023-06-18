# 문자 재정렬
# 알파벳 대문자와 숫자(0~9) 로만 이루어진 문자열이 있다.
# 알파뱃을 오름차순으로 정렬하여 출력, 그 뒤엔 모든 숫자를 더한 값을 출력

s = input()

number = 0
alpabets = []

# 아스키코드 영문은 65부터이므로 나눠서 생각한다.
for i in range(len(s)):
    asciiCode = ord(s[i])
    if asciiCode >= 65:
        alpabets.append(asciiCode)
    else:
        number += int(s[i])

alpabets.sort()
for i in alpabets:
    print(chr(i), end='')
print(number)
