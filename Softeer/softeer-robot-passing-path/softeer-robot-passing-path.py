import copy
import sys


class Point:
    def __init__(self, _x, _y):
        self.__x = _x
        self.__y = _y

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

    def __str__(self):
        return "[{0}] x = {1}, y = {2}".format(self.__class__.__name__, self.__x, self.__y)


class Robot:
    global H, W

    def __init__(self, _sp, _p, _d, _v=None):
        self.__start = copy.deepcopy(_sp)
        self.__current = copy.deepcopy(_p)
        self.__direct = _d

        if not _v:
            self.__visited = copy.deepcopy([[False for _ in range(W)] for _ in range(H)])
        else:
            self.__visited = _v

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, _sp):
        self.__start = _sp

    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, _p):
        self.__current = _p

    @property
    def direct(self):
        return self.__direct

    @direct.setter
    def direct(self, _d):
        self.__direct = _d

    @property
    def visited(self):
        return self.__visited

    @visited.setter
    def visited(self, _visited):
        self.__visited = _visited

    def __str__(self):
        return "[{0}] start point = {1}, current point = {2}, direct = {3}, visited = {4}"\
            .format(self.__class__.__name__, self.__start, self.__current, self.__direct, self.__visited)


def inputData():
    _H, _W = map(int, sys.stdin.readline().split())
    _grid = [list(sys.stdin.readline().rstrip()) for _ in range(_H)]
    return _H, _W, _grid


"""
  (-1, 0): 로봇이 바라보는 방향 (서) ("<")
  (0,  1): 로봇이 바라보는 방향 (남) ("v")
  (1,  0): 로봇이 바라보는 방향 (동) (">")
  (0, -1): 로봇이 바라보는 방향 (북) ("^")
"""


def getDirectStr(_direct):
    _x, _y = _direct.x, _direct.y
    if _x == -1 and _y == 0:
        return "<"
    elif _x == 0 and _y == 1:
        return "v"
    elif _x == 1 and _y == 0:
        return ">"
    else:
        return "^"


def goStraight(_robot, _grid):
    _robot_copy = Robot(copy.copy(_robot.start), copy.copy(_robot.current), copy.copy(_robot.direct),
                        copy.deepcopy(_robot.visited))
    _sp = _robot_copy.start  # instance ref
    _p = _robot_copy.current # instance ref
    _d = _robot_copy.direct # list ref
    _v = _robot_copy.visited # list ref

    for i in range(2):
        _p.x = _p.x + _d.x
        _p.y = _p.y + _d.y

        if 0 <= _p.x < len(_grid[0]) and 0 <= _p.y < len(_grid):
            if not _v[_p.y][_p.x] and _grid[_p.y][_p.x] == '#':
                _v[_p.y][_p.x] = True
            else:
                return False
        else:
            return False
    else:
        return _robot_copy


def goStraightAfterTurnLeft(_robot, _grid):
    _robot_copy = Robot(copy.copy(_robot.start), copy.copy(_robot.current), copy.copy(_robot.direct),
                        copy.deepcopy(_robot.visited))
    _sp = _robot_copy.start  # instance ref
    _p = _robot_copy.current  # instance ref
    _d = _robot_copy.direct
    if _d.x == -1 and _d.y == 0:
        _d = Point(0, 1)
    elif _d.x == 0 and _d.y == 1:
        _d = Point(1, 0)
    elif _d.x == 1 and _d.y == 0:
        _d = Point(0, -1)
    elif _d.x == 0 and _d.y == -1:
        _d = Point(-1, 0)
    _robot_copy.direct = _d
    _v = _robot_copy.visited  # list ref

    for i in range(2):
        _p.x = _p.x + _d.x
        _p.y = _p.y + _d.y

        if 0 <= _p.x < len(_grid[0]) and 0 <= _p.y < len(_grid):
            if not _v[_p.y][_p.x] and _grid[_p.y][_p.x] == '#':
                _v[_p.y][_p.x] = True
            else:
                return False
        else:
            return False
    else:
        return _robot_copy


def goStraightAfterTurnRight(_robot, _grid):
    _robot_copy = Robot(copy.copy(_robot.start), copy.copy(_robot.current), copy.copy(_robot.direct),
                        copy.deepcopy(_robot.visited))
    _sp = _robot_copy.start  # instance ref
    _p = _robot_copy.current  # instance ref
    _d = _robot_copy.direct
    if _d.x == -1 and _d.y == 0:
        _d = Point(0, -1)
    elif _d.x == 0 and _d.y == -1:
        _d = Point(1, 0)
    elif _d.x == 1 and _d.y == 0:
        _d = Point(0, 1)
    elif _d.x == 0 and _d.y == 1:
        _d = Point(-1, 0)
    _robot_copy.direct = _d
    _v = _robot_copy.visited  # list ref

    for i in range(2):
        _p.x = _p.x + _d.x
        _p.y = _p.y + _d.y

        if 0 <= _p.x < len(_grid[0]) and 0 <= _p.y < len(_grid):
            if not _v[_p.y][_p.x] and _grid[_p.y][_p.x] == '#':
                _v[_p.y][_p.x] = True
            else:
                return False
        else:
            return False
    else:
        return _robot_copy


def goStraightAfterTurnLeftLeft(_robot, _grid):
    _robot_copy = Robot(copy.copy(_robot.start), copy.copy(_robot.current), copy.copy(_robot.direct),
                        copy.deepcopy(_robot.visited))
    _sp = _robot_copy.start  # instance ref
    _p = _robot_copy.current  # instance ref
    _d = _robot_copy.direct
    if _d.x == -1 and _d.y == 0:
        _d = Point(1, 0)
    elif _d.x == 0 and _d.y == -1:
        _d = Point(0, 1)
    elif _d.x == 1 and _d.y == 0:
        _d = Point(-1, 0)
    elif _d.x == 0 and _d.y == 1:
        _d = Point(0, -1)
    _robot_copy.direct = _d
    _v = _robot_copy.visited  # list ref

    for i in range(2):
        _p.x = _p.x + _d.x
        _p.y = _p.y + _d.y

        if 0 <= _p.x < len(_grid[0]) and 0 <= _p.y < len(_grid):
            if not _v[_p.y][_p.x] and _grid[_p.y][_p.x] == '#':
                _v[_p.y][_p.x] = True
            else:
                return False
        else:
            return False
    else:
        return _robot_copy


def checkAllVisited(_visited, _grid):
    for _y in range(len(_grid)):
        for _x in range(len(_grid[0])):
            if _grid[_y][_x] == '#':
                if not _visited[_y][_x]: return False
    return True


if __name__ == '__main__':
    H, W, grid = inputData()
    """
      (-1, 0): 로봇이 바라보는 방향 (서) ("<")
      (0,  1): 로봇이 바라보는 방향 (남) ("v")
      (1,  0): 로봇이 바라보는 방향 (동) (">")
      (0, -1): 로봇이 바라보는 방향 (북) ("^")
    """
    directions = [Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)]

    # start points which consist of the start point which can go straight at least twice for reducing complexity
    robots = []
    for h in range(H): # y direction
        for w in range(W): # x direction
            for d in range(len(directions)):
                sp = Point(w, h) # set start point
                if grid[sp.y][sp.x] == '#':
                    robot = Robot(_sp=sp, _p=copy.copy(sp), _d=directions[d])
                    ret = goStraight(robot, grid)
                    if ret:
                        ret.visited[sp.y][sp.x] = True
                        robots.append(ret)

    answers = []
    minCommand = ''
    minCommandLength = sys.maxsize
    for rb in robots:
        stack = [rb]
        command = 'A'

        while stack:
            popRobot = stack.pop(0)

            ret = goStraight(popRobot, grid)
            if ret:
                command += "A"
                stack.append(ret)
                continue

            ret = goStraightAfterTurnLeft(popRobot, grid)
            if ret:
                command += "LA"
                stack.append(ret)
                continue

            ret = goStraightAfterTurnRight(popRobot, grid)
            if ret:
                command += "RA"
                stack.append(ret)

            ret = goStraightAfterTurnLeftLeft(popRobot, grid)
            if ret:
                command += "LLA" # same as RRA
                stack.append(ret)

        if checkAllVisited(popRobot.visited, grid):
            if len(command) < minCommandLength:
                y, x = popRobot.start.y+1, popRobot.start.x+1
                directStr = getDirectStr(popRobot.direct)
                minCommand = command
                minCommandLength = len(command)

    print(y, x)
    print(directStr)
    print(minCommand)
