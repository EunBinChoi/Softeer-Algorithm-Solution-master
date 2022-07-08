from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    color: int


def inputData():
    _seq = []
    while True:
        _data = input()
        if _data: _seq.append(_data)
        else: break

    _points = []
    for i in range(len(_seq)):
        if i == 0:
            _s = _seq[i].split()
            _num_of_points, _num_of_colors = int(_s[0]), int(_s[1])
        else:
            _s = _seq[i].split()
            _points.append(Point(int(_s[0]), int(_s[1]), int(_s[2])))

    return _num_of_points, _num_of_colors, _points


if __name__ == '__main__':
    num_of_points, num_of_colors, points = inputData()
    stack = points.copy()

    point_by_color = {point: [] for point in points}

    while stack:
        p1 = stack.pop()
        