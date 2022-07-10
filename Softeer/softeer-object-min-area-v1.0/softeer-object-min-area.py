import copy
import sys


class Point:
    def __init__(self, _x, _y, _color):
        self.__x = _x
        self.__y = _y
        self.__color = _color

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, _x):
        self.__x = _x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, _y):
        self.__y = _y

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, _color):
        self.__color = _color

    def __str__(self):
        return "[{0}] x = {1}, y = {2}, color = {3}".format(self.__class__.__name__, self.__x, self.__y, self.__color)

def inputData() -> tuple:
    _num_of_points, _num_of_colors = (int(s) for s in input().split())
    _points = [None for _ in range(_num_of_points)]

    for i in range (_num_of_points):
        x, y, c = (int(s) for s in input().split())
        _points[i] = Point(x, y, c)

    return _num_of_points, _num_of_colors, _points


def existAtLeastOneColor(p1: Point, p2: Point, _num_of_points: int, _num_of_color: int, _points: list) -> bool:
    _checker = {p.color: False for p in _points}
    _checker[p1.color] = True
    _checker[p2.color] = True

    _point_by_colors = {p.color: [] for p in _points}
    for p in _points:
        _point_by_colors[p.color].append((p.x, p.y))

    for key in _point_by_colors.keys():
        for value in _point_by_colors[key]:
            if p1.x <= value[0] <= p2.x and p1.y <= value[1] <= p2.y:
                _checker[key] = True
            elif p1.x <= value[0] <= p2.x and p2.y <= value[1] <= p1.y:
                _checker[key] = True
            elif p2.x <= value[0] <= p1.x and p1.y <= value[1] <= p2.y:
                _checker[key] = True
            elif p2.x <= value[0] <= p1.x and p2.y <= value[1] <= p1.y:
                _checker[key] = True

    return all(_checker.values())


def calArea(p1: Point, p2: Point) -> int:
    return abs(p1.x - p2.x) * abs(p1.y - p2.y)


def combination(_num_of_points, _num_of_colors, _points):
    _pts = copy.deepcopy(_points)
    _min_area = sys.maxsize
    
    for i in range(len(_pts)):
        for j in range(len(_pts)):
            if i != j and existAtLeastOneColor(_pts[i], _pts[j], _num_of_points, _num_of_colors, _points):
                _min_area = min(_min_area, calArea(_pts[i], _pts[j]))
    return _min_area


if __name__ == '__main__':
    num_of_points: int
    num_of_colors: int
    points: list
    num_of_points, num_of_colors, points = inputData()

    min_area = combination(num_of_points, num_of_colors, points)
    print(min_area)
        