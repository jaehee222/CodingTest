# 0과 1로만 이루어진 문자열 S
# S를 통일된 문자열로 만들고 싶음
# 연속된 하나 이상의 숫자를 잡고 모두 뒤집기
# 뒤집을 수 있는 최소의 횟수

# 청백전으로 연속된 0이 많은지 1이 많은지 !

S = input()
arr = [0,0]

tmp = int(S[0])
arr[tmp] += 1
for i in range(1, len(S)):
    if tmp != int(S[i]): # 연속이 끊겼을 때..
        tmp = int(S[i])
        arr[tmp] += 1

print(min(arr[0],arr[1]))
