# 시각
# 정수 N이 입력되면 0시0분0초~N시 59분59초까지 모든 시각중 3이 하나라도 포함되는 모든 경우의 수.

n = int(input())

hour = 0
minute = 0
second = 0
result = 0
while True:
    second += 1
    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0
    time = str(hour) + str(minute) + str(second)
    # 숫자의 위치 반환. 없으면 -1
    if time.find('3') != -1:
        result += 1
    if time == str(n) + '5959':
        break

print(result)
