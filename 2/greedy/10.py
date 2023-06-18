def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    # 음식을 다 먹은 뒤이므로
    if sum(food_times) <= k:
        return -1
    
    # 몇바퀴 돌 수 있는지 확인
    x = k // len(food_times)
    time = x * len(food_times)
    
    # 돌았던 바퀴 수 만큼 빼줌
    if (x >= 1):
        for i in range(len(food_times)):
            food_times[i] -= x
    
    idx = 0
    while time <= k:
        # 이미 다 먹은 음식은 빼줌
        if food_times[idx] == 0:
            idx += 1
            continue
        food_times[idx] -= 1
        time += 1
        idx += 1
        if idx == len(food_times):
            idx = 0
    
    return idx
