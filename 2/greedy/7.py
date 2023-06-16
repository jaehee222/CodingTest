# 문자열 뒤집기
# 0과 1로만 이루어진 문자열 S
# 문자열에 있는 모든 숫자가 모두 가게 하고 싶다.
# 다솜이가 할 수 이쓴 행동은 연속된 하나 이상의 숫자를 잡고 모두를 뒤집는 것 (0->1 or 1->0)

# 연속된 문자열을 세서 비교 (0이 많은지 1이 많은지)

s = input()

arr = [0] * 2  # arr[0] == 연속된 0의 갯수 # arr[1] == 연속된 1의 갯수
oldarr = int(s[0])
arr[int(s[0])] += 1
for i in range(len(s)):
    # 연속되지 않았을 때
    if oldarr != int(s[i]):
        arr[int(s[i])] += 1
        oldarr = int(s[i])

result = min(arr[0], arr[1])
print(result)
