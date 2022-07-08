def getPassedCarAtCurrentTime(cur_inter, len_key) -> tuple:
    passed = []  # 현재 시간에 통과할 수 있는 차량 리스트
    # 1 2 3
    # 1: 1 -> 2 -> 3
    # 2: 2 -> 3
    # 3: 3
    for i in range(len(cur_inter)):
        cur_car = cur_inter[i]
        right_car = getLocationofRightCar(cur_car, len_key)
        while right_car in cur_inter:
            cur_car = right_car
            right_car = getLocationofRightCar(cur_car, len_key)

        if cur_car not in passed:
            passed.append(cur_car)

    non_passed = cur_inter.copy()
    for pa in passed:
        if pa in non_passed:
            non_passed.remove(pa)

    return passed, non_passed


# 교차로 우선순위 차량 확인 (나의 오른쪽 차량의 교차로 번호가 반환)
# B > C (B출C출), A > B (A출B출), C > D (C출D출), D > A (D출A출), A=C, B=D
def getLocationofRightCar(car: str, len_key: int) -> str:
    return chr(ord(car) - 1 + len_key) if not chr(ord(car) - 1).isalpha() else chr(ord(car) - 1)


# 주어진 시간이 있을 때 현재 교차로 상황
def getCurrentLocationAtCurrentTime(cur_time: int, time_by_loc: dict) -> list:
    cur_inter = []  # intersection location
    for key in time_by_loc.keys():  # [(key, []), , , ,]
        for j in range(len(time_by_loc[key])):
            if time_by_loc[key][j] == cur_time:
                # if key not in cur_inter:
                cur_inter.append(key)
    return cur_inter


if __name__ == '__main__':
    N = int(input())  # N 입력받기

    lst_tw = [[] for _ in range(N)]  # tw 저장하는 리스트 생성, 설명 필요
    tnw = [0] * N  # [element for element in input().split()]

    for i in range(N):
        tnw[i] = input().split()
        tnw[i][0] = int(tnw[i][0])  # 입력 숫자 str->int

    time_by_loc = {'A': [], 'B': [], 'C': [], 'D': []}
    index_by_loc = {'A': [], 'B': [], 'C': [], 'D': []}
    for i in range(len(tnw)):  # 2
        time_by_loc[tnw[i][1]].append(tnw[i][0])
        index_by_loc[tnw[i][1]].append(i)

    # shallow copy: 1d copy
    # deep copy: 2d copy
    cur_time = tnw[0][0]
    passed_time = [-1 for _ in range(N)]

    idx = 0
    while True:
        # cur_inter = 3, 4, 5
        cur_inter = getCurrentLocationAtCurrentTime(cur_time, time_by_loc)

        if len(cur_inter) == 0:
            break
        elif len(cur_inter) >= 4:
            break

        passed_car, non_passed_car = getPassedCarAtCurrentTime(cur_inter, len(time_by_loc.keys()))
        if len(passed_car) == 1:
            if len(time_by_loc[passed_car[0]]) > 0 and len(index_by_loc[passed_car[0]]) > 0:
                passed_time[index_by_loc[passed_car[0]][0]] = cur_time
                time_by_loc[passed_car[0]].pop(0)
                index_by_loc[passed_car[0]].pop(0)
        else:
            for pc in passed_car:
                if len(time_by_loc[pc[0]]) > 0 and len(index_by_loc[pc[0]]) > 0:
                    passed_time[index_by_loc[pc[0]][0]] = cur_time
                    time_by_loc[pc[0]].pop(0)
                    index_by_loc[pc[0]].pop(0)

        cur_time += 1

        # non-passed car += 1
        for key in time_by_loc.keys():
            if key in non_passed_car:
                time_by_loc[key][0] += 1

    for pt in passed_time:
        print(pt)