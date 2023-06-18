# 럭키스트레이트
# 게임 아웃복서 캐릭터의 필살기는 특정조건일때만 사용 가능함
# 현재 캐릭터 점수 N을 반으로 나눠 완쪽 부분의 각 자릿수의 합과
# 오른쪽 부분 각 자릿수의 합을 더한값이 동일한 상황.
# 현재 점수 N 이 주어졌을 때 필살기 사용가능하다면 LUCKY
# 없다면 READY 출력
# 단, 자릿수는 무조건 짝수

n = input()
x = len(n) // 2
left = 0
for i in range(0, x):
    left += int(n[i])

right = 0
for i in range(x, len(n)):
    right += int(n[i])

if left == right:
    print("LUCKY")
else:
    print("READY")
