import copy
import sys


def inputData():
    _n = int(input())
    _tnw = [0] * _n  # [element for element in input().split()]

    for i in range(_n):
        _tnw[i] = input().split()
        _tnw[i][0] = int(_tnw[i][0])  # 입력 숫자 str -> int
    return _n, _tnw


def initTimeByLocation(_tnw: list) -> dict:
    _location = ['A', 'B', 'C', 'D']
    _time_by_loc = {_loc: [] for _loc in _location}
    _index_by_loc = {_loc: [] for _loc in _location}
    for i in range(len(_tnw)):
        _time_by_loc[_tnw[i][1]].append(_tnw[i][0])
        _index_by_loc[_tnw[i][1]].append(i)
    return _time_by_loc, _index_by_loc


def getCurrentTime(_time_by_loc: dict) -> int:
    _min_t = sys.maxsize
    for _key in _time_by_loc.keys():
        for _value in _time_by_loc[_key]:
            if _min_t > _value:
                _min_t = _value
    return _min_t


def getCurrentLocationAtSameTime(_time_by_loc: dict, _cur_time: int) -> list:
    _cur_inter_set = []  # intersection location
    for _key in _time_by_loc.keys():  # [(key, []), , , ,]
        for j in range(len(_time_by_loc[_key])):
            if _time_by_loc[_key][j] == _cur_time:
                if _key not in _cur_inter_set:
                    _cur_inter_set.append(_key)
                else:
                    _time_by_loc[_key][j] += 1
    return _cur_inter_set


def getValuesOfTimeByLocation(_time_by_loc: dict) -> list:
    _values = []
    for _key in _time_by_loc.keys():
        for _value in _time_by_loc[_key]:
            _values.append(_value)
    return _values


def getRightCarsAtSameTime(_cur_inter_set: list, _len_key: int) -> list:
    _right_cars = []
    _idx = 0
    while _idx < len(_cur_inter_set):
        _cur_car = _cur_inter_set[_idx]
        _right_car = getLocationOfRightCar(_cur_car, _len_key)

        if _right_car not in _right_cars:
            _right_cars.append(_right_car)

        _idx += 1
    return _right_cars


def getLocationOfRightCar(_car: str, _len_key: int) -> str:
    return chr(ord(_car)-1 + _len_key) if not chr(ord(_car)-1).isalpha() else chr(ord(_car)-1)


def getLocationOfPassedCar(_cur_inter_set: list, _len_key: int) -> list:
    _passed = []
    _count = 0 # infinite loop block (case when all car exist at intersection)
    for _cur_car in _cur_inter_set:
        _right_car = getLocationOfRightCar(_cur_car, _len_key)
        _count += 1
        if _right_car not in _cur_inter_set:
            _passed.append(_cur_car)

        while _right_car in _cur_inter_set:
            _cur_car = _right_car
            _right_car = getLocationOfRightCar(_cur_car, _len_key)
            _count += 1

            if _count == _len_key:
                return [['A', 'B', 'C', 'D'], []]

        if _cur_car not in _passed:
            _passed.append(_cur_car)

    _non_passed = list(set(_cur_inter_set) - set(_passed))
    return _passed, _non_passed


def increaseTime(_time_by_loc: dict, _non_passed_car: list) -> None:
    for _key in _time_by_loc.keys():
        if _key in _non_passed_car:
            if len(_time_by_loc[_key]) > 0:
                _time_by_loc[_key][0] += 1


if __name__ == '__main__':
    N, tnw = inputData() # input
    initial_time = tnw[0][0]
    cur_time = initial_time
    time_by_loc, index_by_loc = initTimeByLocation(tnw)
    passed_time = [-1 for _ in range(N)] # output
    while True:
        cur_inter_set = getCurrentLocationAtSameTime(time_by_loc, cur_time)
        right_cars = getRightCarsAtSameTime(cur_inter_set, len(time_by_loc.keys()))
        values = getValuesOfTimeByLocation(time_by_loc)

        if len(values) == 0:
            break # while loop exits

        # which car will pass the intersection
        # passed_car could be list
        passed_car, non_passed_car = getLocationOfPassedCar(cur_inter_set, len(time_by_loc.keys()))

        if len(passed_car) == 1:
            if len(time_by_loc[passed_car[0]]) > 0:
                passed_time[index_by_loc[passed_car[0]][0]] = cur_time
                time_by_loc[passed_car[0]].pop(0)
                index_by_loc[passed_car[0]].pop(0)

        elif len(passed_car) == 4:
            for pc in passed_car:
                if len(time_by_loc[pc]) > 0:
                    passed_time[index_by_loc[pc[0]][0]] = -1
                    time_by_loc[pc].pop(0)
                    index_by_loc[pc].pop(0)

        else:
            for pc in passed_car:
                if len(time_by_loc[pc]) > 0:
                    passed_time[index_by_loc[pc[0]][0]] = cur_time
                    time_by_loc[pc].pop(0)
                    index_by_loc[pc].pop(0)

        increaseTime(time_by_loc, non_passed_car)
        cur_time += 1

    for pt in passed_time:
        print(pt)


# shallow copy: 1d copy
# deep copy: 2d copy
