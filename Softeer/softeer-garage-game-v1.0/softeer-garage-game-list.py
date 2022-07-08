import sys
import copy


def inputData() -> tuple:
    _n: int = int(input())
    _seq: list = [[0 for _ in range(_n)] for _ in range(3*_n)]
    for i in range(len(_seq)):
        _tmp: list = input().split()
        for j in range(len(_seq[0])):
            _seq[i][j]: int = int(_tmp[j])

    return _n, _seq


def initGarage(_n: int, _seq: list) -> tuple:
    _garage: list = [[0 for _ in range(_n)] for _ in range(_n)]
    _left_garage: list = [[0 for _ in range(_n)] for _ in range(2 * _n)]

    for i in range(_n):
        for j in range(_n):
            _garage[i][j]: int = _seq[2*_n + i][j]

    for i in range(2*_n):
        for j in range(N):
            _left_garage[i][j]: int = _seq[i][j]

    return _garage, _left_garage


def calDepth(_path: list) -> bool:
    _d: dict = {} # {0: 1, 1: 1}
    for _row, _col in _path:
        if _col not in _d.keys():
            _d[_col] = 1
        else:
            _d[_col] += 1
    return _d


def makeGaragewithDisappearBlock(_garage: list, _left_garage: list, _path: list) -> tuple:
    _new_garage_stacks = [[] for _ in range(len(_garage[0]))]
    _new_left_garage_stacks = [[] for _ in range(len(_left_garage[0]))]

    for _col in range(len(_garage[0])):
        for _row in range(len(_garage)):
            _new_garage_stacks[_col].append(_garage[_row][_col])

    for _col in range(len(_left_garage[0])):
        for _row in range(len(_left_garage)):
            _new_left_garage_stacks[_col].append(_left_garage[_row][_col])

    for _col in range(len(_new_garage_stacks)):
        for _row in range(len(_new_garage_stacks[_col])):
            if (_row, _col) in _path:
                _new_garage_stacks[_col].pop(_row)

                if len(_new_left_garage_stacks[_col]) > 0:  # disappear
                    _new_garage_stacks[_col].insert(0, _new_left_garage_stacks[_col].pop())

    _normal_row = len(_left_garage)
    for _col in range(len(_new_left_garage_stacks)):
        for _row in range(_normal_row - len(_new_left_garage_stacks[_col])):
            _new_left_garage_stacks[_col].insert(0, -1)

    _new_garage = copy.deepcopy(_garage)
    _new_left_garage = copy.deepcopy(_left_garage)
    for _col in range(len(_new_garage_stacks)):
        for _row in range(len(_new_garage_stacks[_col])):
            _new_garage[_row][_col] = _new_garage_stacks[_col][_row]

    for _col in range(len(_new_left_garage_stacks)):
        for _row in range(len(_new_left_garage_stacks[_col])):
            _new_left_garage[_row][_col] = _new_left_garage_stacks[_col][_row]

    return _new_garage, _new_left_garage


def calScoreofGarage(_path: list) -> int:
    _max_row: int = 0
    _max_col: int = 0
    _min_row: int = sys.maxsize
    _min_col: int = sys.maxsize

    for _p in _path:
        _cur_row = _p[0]
        _cur_col = _p[1]

        _max_row = max(_max_row, _cur_row)
        _max_col = max(_max_col, _cur_col)
        _min_row = min(_min_row, _cur_row)
        _min_col = min(_min_col, _cur_col)

    _disappear_car = len(_path)
    _square_row: int = _max_row-_min_row+1 if _max_row-_min_row > 0 else 1
    _square_col: int = _max_col-_min_col+1 if _max_col-_min_col > 0 else 1
    _score = (_square_row * _square_col) + _disappear_car

    return _score


def makeLocationSet(_n: int, _garage: list) -> list:
    _garage_set_color = []
    for i in range(_n):
        for j in range(_n):
            if _garage[i][j] not in _garage_set_color:
                _garage_set_color.append(_garage[i][j])

    _garage_set_loc = {_key: [] for _key in _garage_set_color} # ex) [4: [(0,0), (0,1)], 1: [(1, 0)], 2: [(1, 1)]]
    for i in range(_n):
        for j in range(_n):
            _garage_set_loc[_garage[i][j]].append((i, j))
    return _garage_set_color, _garage_set_loc


def calPath(_garage: list, _garage_set_color: list, _garage_set_loc: dict) -> dict:
    _direction: list = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 위, 아래, 왼쪽, 오른쪽
    _paths: dict = {_key: [] for _key in _garage_set_color} # ex) {4: [[(0, 0), (0, 1)], [(0, 1), (0, 0)]]
    for _color in _garage_set_color:
        for j in range(len(_garage_set_loc[_color])):
            _location: tuple = _garage_set_loc[_color][j]
            _initial_location: tuple = _location
            _current_location: tuple = _initial_location
            _path: list = [_current_location]

            k = 0
            while k < len(_direction):
                _row: int = _current_location[0] + _direction[k][0]
                _col: int = _current_location[1] + _direction[k][1]

                if (_row, _col) in _path:
                    k += 1
                    continue

                if 0 <= _row < N and 0 <= _col < N and _garage[_row][_col] == _color:
                    _path.append((_row, _col))
                    _current_location: tuple = (_row, _col)
                    k = 0
                else:
                    k += 1
            _paths[_color].append(_path)
    return _paths


class Node:
    def __init__(self, _is_root, _key, _garage, _left_garage, _path):
        self.__is_root = _is_root
        self.__key = _key
        self.__garage = _garage
        self.__left_garage = _left_garage
        self.__path = _path
        self.__score = 0
        self.__level = 0

    @property
    def is_root(self):
        return self.__is_root

    @is_root.setter
    def is_root(self, _is_root):
        self.__is_root = _is_root

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, _key):
        self.__key = _key

    @property
    def garage(self):
        return self.__garage

    @garage.setter
    def garage(self, _garage):
        self.__garage = _garage


    @property
    def left_garage(self):
        return self.__left_garage

    @left_garage.setter
    def left_garage(self, _left_garage):
        self.__left_garage = _left_garage

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, _path):
        self.__path = _path


    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, _score):
        self.__score = _score

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, _level):
        self.__level = _level

    def __str__(self) -> str:
        return "<Node Class> is_root = {0},\n key = {1},\n garage\n = {2},\n left_garage\n = {3},\n, " \
               "path\n = {4},\n score = {5},\n level = {6}\n"\
            .format(self.__is_root, self.__key, self.__garage, self.__left_garage, self.__path, self.__score, self.__level)


if __name__ == '__main__':
    N, seq = inputData()
    garage, left_garage = initGarage(N, seq)
    garage_set_color, garage_set_loc = makeLocationSet(N, garage)
    paths = calPath(garage, garage_set_color, garage_set_loc)

    simulation_N = 3
    stack = []
    visited = []

    # root
    for key, value in paths.items():
        for path in value:
            n = Node(True, key, garage, left_garage, path)
            n.score = calScoreofGarage(path)
            n.level = 1
            stack.append(n)

    scores = []
    scores_by_level = {level: 0 for level in range(1, simulation_N+1)}
    level_check = {level: False for level in range(1, simulation_N+1)}
    while stack:
        popNode = stack.pop()

        if popNode not in visited:
            if popNode.is_root:
                for le in level_check.keys():
                    level_check[le] = False
                    scores_by_level[le] = 0

            level_check[popNode.level] = True
            scores_by_level[popNode.level] = popNode.score

            if popNode.level != simulation_N:
                for le in range(popNode.level+1, simulation_N+1):
                    level_check[le] = False
                    scores_by_level[le] = 0

            else:
                if all(scores_by_level):
                    score = sum(scores_by_level.values()) if len(scores_by_level) > 0 else 0
                    scores.append(score)

            visited.append(popNode)
            garage, left_garage = makeGaragewithDisappearBlock(popNode.garage, popNode.left_garage, popNode.path)
            garage_set_color, garage_set_loc = makeLocationSet(N, garage)
            paths = calPath(garage, garage_set_color, garage_set_loc)

            for key, value in paths.items():
                for path in value:
                    newNode = Node(False, key, garage, left_garage, path)
                    newNode.score = calScoreofGarage(path)
                    newNode.level = popNode.level + 1

                    if newNode.level <= simulation_N:
                        stack.append(newNode)

    print(max(scores))