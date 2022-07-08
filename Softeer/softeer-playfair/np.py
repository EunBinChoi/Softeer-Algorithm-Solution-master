import numpy as np

# reshape을 이용한 차원 확대 (1d -> 2d)
# shape을 바꿔주는 api
a = np.arange(9)

# 확장하고 싶은 차원에 1을 넣고 나머지 차원에 원래 원소 갯수를 넣음으로써 size는 유지하되 차원 확장
b = a.reshape((1, 9))
c = a.reshape((9, 1))

print(f"a: {a.shape}\n {a}\n")
print(f"b: {b.shape}\n {b}\n")
print(f"c: {c.shape}\n {c}\n")
print("=" * 50)

##############################################################################
# 실제 데이터를 다룰 때는 원래 원소 갯수를 알기 까다로울 때가 많음
# 해당 위치에 -1을 넣어주면 알아서 원소 갯수를 계산하고 1을 넣은 위치에 따라 차원을 확장하게 됨
a = np.arange(9)
b = a.reshape((1, -1))  # (1, 9)
c = a.reshape((-1, 1))  # (9, 1)

print(f"a: {a.shape}\n {a}\n")
print(f"b: {b.shape}\n {b}\n")
print(f"c: {c.shape}\n {c}\n")
print("=" * 50)

##############################################################################
# reshape을 이용한 차원 확대 (1d -> 3d)

# (9,) 형태의 1차원 row 벡터
# 1d row vector
a = np.arange(9)

# 2d row vector
a_2d = a.reshape((1, 9))  # 2d

# (1, 9)의 shape을 가진 row 벡터 행렬을 1개
# 3d row vector
a_3d = a.reshape((1, 1, 9))  # 3d

# (9, 1)의 shape을 가진 column 벡터 행렬을 1개
b = a.reshape((1, 9, 1))

# (1, 1)의 shape을 가진 행렬이 9개의 차원으로 구성됨
c = a.reshape((9, 1, 1))

print(f"a: {a.shape}\n {a}\n")
print(f"a_2d: {a_2d.shape}\n {a_2d}\n")
print(f"a_3d: {a_3d.shape}\n {a_3d}\n")
print(f"b: {b.shape}\n {b}\n")
print(f"c: {c.shape}\n {c}\n")
print("=" * 50)

#############################################################################
# reshape을 이용한 차원 확대 (1d -> 3d)

# (9,) 형태의 1차원 row 벡터
# 1d row vector
a = np.arange(9)

# 2d row vector
a_2d = a.reshape((1, -1))  # 2d

# (1, 9)의 shape을 가진 row 벡터 행렬을 1개
# 3d row vector
a_3d = a.reshape((1, 1, -1))  # 3d

# (9, 1)의 shape을 가진 column 벡터 행렬을 1개
b = a.reshape((1, -1, 1))

# (1, 1)의 shape을 가진 행렬이 9개의 차원으로 구성됨
c = a.reshape((-1, 1, 1))

print(f"a: {a.shape}\n {a}\n")
print(f"a_2d: {a_2d.shape}\n {a_2d}\n")
print(f"a_3d: {a_3d.shape}\n {a_3d}\n")
print(f"b: {b.shape}\n {b}\n")
print(f"c: {c.shape}\n {c}\n")
print("=" * 50)

##############################################################################
# 2d -> 3d
a = np.random.normal(size=(100, 200))

# * (asterisk): a.shape을 *로 unpacking
b = a.reshape((1, *a.shape))
c = a.reshape((*a.shape, 1))

print(a.shape)
print(b.shape)
print(c.shape)
print()

##############################################################################
# asterisk ex)
l1 = [1, 2, 3]
l2 = ['python']
l3 = [*l1, *l2]
a, *b, (c, *d) = l3
print(l1)
print(l2)
print(l3)
print(a)
print(b)
print(c)
print(d)
print()

# basic unpacking
# list, tuple, string, dictionary, set에 사용 가능
a, b, c = [1, 2, 3]
print(a, b, c)

a, b, c = (1, 2, 3)
print(a, b, c)

a, b, c = 'abc'
print(a, b, c)

a, b, c = {'a': 1, 'b': 2, 'c': 3}  # key returns
print(a, b, c)

a, b, c = {'a': 1, 'b': 2, 'c': 3}.keys()  # key returns
print(a, b, c)

a, b, c = {'a': 1, 'b': 2, 'c': 3}.values()  # value returns
print(a, b, c)

a, b, c = {'a': 1, 'b': 2, 'c': 3}.items()  # item returns
print(a, b, c)

# cf) set
# 참고로 set도 iterable 이기 때문에 unpacking이 가능
# set은 순서가 없는 데이터 타입이기 떄문에 unpacking을 하면 순서대로가 아닌 뒤죽박죽으로 값이 할당됨
# 사실상 unpacking이 의미가 없어 사용하지 않음
a, b, c = {'a', 'b', 'c'}
print(a, b, c)

# [ un-packing ]
# 1) *
# unpacking using *
# 1) *가 왼쪽 변수에 있을 경우
a, b, c = [1, 2, 3]
print(a, b, c)

# 변수는 3개인데 원소 값이 5개
# 3개 변수 안에 5개의 원소를 우겨넣을 수 있음
# *가 없는 변수가 값을 할당받고 할당받지 못한 나머지 값들을 모아서 무조건 리스트로 만듦
a, *b, c = [1, 2, 3, 4, 5]
print(a, type(a), ",", b, type(b), ",", c, type(c))

# 기존에 컨테이너 타입이 튜플이든 set이 오던 상관없이 항상 리스트 형태로 부여받음
a, *b, c = {1, 2, 3, 4, 5}
print(a, type(a), ",", b, type(b), ",", c, type(c))

# cf) 왼쪽 변수부분에는 *를 한번만 사용 가능, 두번 사용할 시 아래와 같이 오류남
# a, *b, *c = {1, 2, 3, 4, 5}
# print(a, type(a), ",", b, type(b), ",", c, type(c))

# 컨테이너 그 자체를 unpacking하는 *
# 만약에 리스트값을 각 변수에 할당받는데 값이 변수보다 많을 경우
li = [1, 2, 3]
print(*li)  # 리스트 자체를 분해
print(li)
print()

# 원하는 컨테이너를 넣어허 합칠 수 있음
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [*l1, *l2]  # extend한 것처럼 들어감, []
l4 = [l1, l2]  # append한 것 처럼 들어감, [[], []]
print(l1)
print(l2)
print("list:", l3, ",", "len()", len(l3))
print("list:", l4, ",", "len()", len(l4))
print()

# 튜플에 담은 예시
l1 = [1, 2, 3]
l2 = 'XYZ'
l3 = (*l1, *l2)
print(l3)
print()

# ex)
l1 = [1, 2, 3]
# l2 = *l1 # 그냥 사용은 불가 (값이 분리됨)
print(*l1)
# print(l2)

l1 = [1, 2, 3]
l2 = *l1,  # tuple
print(l1)  # list
print(l2)  # tuple
print()

# 2) **
# a, **b, c = {'a':1, 'b':2, 'c':3} # error
# print(a, b, c)

d1 = {'p': 1, 'y': 2}
d2 = {'t': 3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}
d = {*d1, *d2, *d3}  # 딕셔너리를 unpacking 한 후 (key 값만 값으로 가져옴) set의 형태로 값을 묶음 (h가 하나로 축소, set이니 무작위로 묶임)
print(d)

d = {**d1, **d2, **d3}  # 딕셔너리를 unpacking 한 후 (key, value를 한꺼번에 보기 위해서 사용함) set의 형태로 값을 묶음 (h가 하나로 축소, set이니 무작위로 묶임)
print(d)

# override
# 순서상 뒤에 정의된 값이 이전 값을 덮어씌우는 현상
d1 = {'a': 1, 'b': 2}
d2 = {'a': 10, 'c': 3, **d1}
d3 = {**d1, 'a': 10, 'c': 3}
print(d1)
print(d2)
print(d3)

# nested unpacking
# 겹겹이 쌓여있는 리스트를 unpacking하는 경우

# error
# li = [1, 2, [3, 4]]
# a, b, c, d = li # d는 아무것도 받지 않아서 오류 생김
# print(a, b, c, d)

li = [1, 2, [3, 4]]
a, b, (c, d) = li
print(a, b, c, d)
a, b, [c, d] = li
print(a, b, c, d)
print()

# *args
# 일반적인 * 사용
a, b, *c = 10, 20, 'a', 'b'
print(a, "->", type(a))
print(b, "->", type(b))
print(c, "->", type(c))  # 남은 값들을 리스트 형태로 부여 받음
print()

a, *b, c = 10, 20, 'a', 'b'
print(a, "->", type(a))
print(b, "->", type(b))
print(c, "->", type(c))  # 남은 값들을 리스트 형태로 부여 받음
print()



# 함수에 가변인자로 사용할 때에는 보편적으로 변수 이름을 *args 형태로 작성
def func1(a, b, *args):
    print(a, "->", type(a))
    print(b, "->", type(b))
    print(args, "->", type(args))  # 남은 값들을 튜플 형태로 부여 받음


func1(10, 20, 'a', 'b')
print()


# 함수에 가변인자로 사용할 때에는 보편적으로 변수 이름을 *args 형태로 작성
def func2(a, *args, b):
    print(a, "->", type(a))
    print(args, "->", type(args))
    print(b, "->", type(b))  # 남은 값들을 튜플 형태로 부여 받음

# required keyword-only argument
func2(10, 20, 'a', b = 'b')
print()

# 리스트의 원소값들을 자동으로 그 위치에 맞게 값을 할당
# 함수에도 적용하면 자동으로 unpacking하지 않음 (func3(li) -> func3(*li))
li = [10, 20, 30]
def func3(a, b, c):
    print(a, b, c)

func3(*li)
print()


##############################################################################
# 슬라이싱을 이용한 차원 확대
# 1d -> 2d
a = np.arange(9)

# 원래 차원은 :로 표시하고 새로 추가할 것을 np.newaxis 또는 None 사용 (내부적으로 np.newaxis == None)
# reshape((1, -1))과 같음
row_vec1 = a[np.newaxis, :]
row_vec2 = a[None, :]

print(f"row_vec1: {row_vec1}")
print(f"row_vec1.shape: {row_vec1.shape}")
print(f"row_vec2: {row_vec2}")
print(f"row_vec2.shape: {row_vec2.shape}")
print()

# reshape((-1, 1))과 같음
col_vec1 = a[:, np.newaxis]
col_vec2 = a[:, None]

print(f"col_vec1: {col_vec1}")
print(f"col_vec1.shape: {col_vec1.shape}")
print(f"col_vec2: {col_vec2}")
print(f"col_vec2.shape: {col_vec2.shape}")
print()

# 1d -> 3d
a = np.arange(9)
b = a[np.newaxis, np.newaxis, :]
c = a[np.newaxis, :, np.newaxis]
d = a[:, np.newaxis, np.newaxis]
print(f"a.shape: {a.shape}")
print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
print()

# 2d -> 3d
a = np.random.normal(size=(100, 200))
b = a[np.newaxis, :, :]
b = a[np.newaxis, ...]
c = a[:, :, np.newaxis]
c = a[..., np.newaxis]
d = a[:, np.newaxis, :]
print(f"a.shape: {a.shape}")
print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
print()

# expand_dims api를 이용한 차원 확대
# 1d -> 2d
a = np.arange(9)
b = np.expand_dims(a, axis=0) # 첫번째 차원에 새로운 축을 만들겠음 (row 위치에 1이 추가됨으로써 차원이 확장)
c = np.expand_dims(a, axis=1) # 두번째 차원에 새로운 축을 만들겠음 (col 위치에 1이 추가됨으로써 차원이 확장)
print(f"a.shape: {a.shape}")
print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print()

# 1d -> 3d
a = np.arange(9)
b = np.expand_dims(a, axis=(0,1))
b = np.expand_dims(a, axis=(1,0))
c = np.expand_dims(a, axis=(0,2))
c = np.expand_dims(a, axis=(2,0))
d = np.expand_dims(a, axis=(1,2))
d = np.expand_dims(a, axis=(2,1))
print(f"a.shape: {a.shape}")
print(f"b.shape: {b.shape}")
print(f"c.shape: {c.shape}")
print(f"d.shape: {d.shape}")
print()


# reshape | flatten을 이용한 차원 축소
# reshape을 이용하여 차원을 축소하고 싶을 때는 1을 빼주면 됨
a = np.ones(shape=(1, 10))

# 차원을 죽이는 다양한 방법
b = a.reshape((10,))
c = a.reshape((-1,))
d = a.flatten() # 무조건 1차원으로 만듦

print(f"a: {a}")
print(f"a.shape: {a.shape}")
print(f"b: {b}")
print(f"b.shape: {b.shape}")
print(f"c: {c}")
print(f"c.shape: {c.shape}")
print(f"d: {d}")
print(f"d.shape: {d.shape}")
print()

a = np.ones(shape=(1,3,4))
b = np.ones(shape=(3,4,1))
c = a.reshape(*a.shape[1:])
d = b.reshape(*b.shape[:-1])

print(f"a: {a}")
print(f"a.shape: {a.shape}")
print(f"b: {b}")
print(f"b.shape: {b.shape}")
print(f"c: {c}")
print(f"c.shape: {c.shape}")
print(f"d: {d}")
print(f"d.shape: {d.shape}")
print()

# dimension reduction using slicing
a = np.arange(9).reshape((3, 3))
b, c = a[1, :], a[:, 1]
print(f"a: {a}")
print(f"a.shape: {a.shape}")

# if you want to reduce specific dimension, you can write 1 at that location
print(f"b: {b}") # [3, 4, 5]
print(f"b.shape: {b.shape}") # (3, )
print(f"c: {c}") # [1, 4, 7]
print(f"c.shape: {c.shape}") # (3, )
print()

a = np.arange(9).reshape((1, -1))
b = np.arange(9).reshape((-1, 1))
c = a[0, :]
d = b[:, 0]
print(f"a: {a}")
print(f"a.shape: {a.shape}")
print(f"b: {b}")
print(f"b.shape: {b.shape}")
print(f"c: {c}")
print(f"c.shape: {c.shape}")
print(f"d: {d}")
print(f"d.shape: {d.shape}")
print()

a = np.ones(shape=(1, 3, 4))
b = np.ones(shape=(3, 4, 1))
c = a[0, ...]
d = b[..., 0]
print(f"a: {a}")
print(f"a.shape: {a.shape}")
print(f"b: {b}")
print(f"b.shape: {b.shape}")
print(f"c: {c}")
print(f"c.shape: {c.shape}")
print(f"d: {d}")
print(f"d.shape: {d.shape}")
print()

# squeeze api
# flatten(): n-d -> 1-d (3차원 이상일 경우에는 기존 shape을 망가뜨리기 때문에 문제 발생)
# squeeze(): 1이 아닌 값들의 shape을 유지하면서 1인 값들은 다 없애버림
a = np.ones(shape=(1, 3, 4))
b = np.squeeze(a)
c = a.squeeze()
print(f"a: {a}")
print(f"a.shape: {a.shape}")
print(f"b: {b}")
print(f"b.shape: {b.shape}")
print(f"c: {c}")
print(f"c.shape: {c.shape}")
print()

# np.swapaxes()
a = np.random.normal(size=(3,4,5,6))
b = np.swapaxes(a, 0, 1)
c = np.swapaxes(a, 0, 2)
d = np.swapaxes(a, 0, 3)
print(f"a: {a}")
print(f"a.shape: {a.shape}") # (3, 4, 5, 6)
print(f"b: {b}")
print(f"b.shape: {b.shape}") # (4, 3, 5, 6)
print(f"c: {c}")
print(f"c.shape: {c.shape}") # (5, 4, 3, 6)
print(f"d: {d}")
print(f"d.shape: {d.shape}") # (6, 4, 5, 3)
print()

a = np.random.normal(size=(3, 200, 100))
b = np.swapaxes(a, 0, -1) # 첫번쩨 차원과 마지막 차원을 바꿔라
print(f"a: {a}")
print(f"a.shape: {a.shape}") # (3, 200, 100)
print(f"b: {b}")
print(f"b.shape: {b.shape}") # (100, 200, 3)
print()

# np.moveaxis()
a = np.random.normal(size=(3, 4, 5, 6))
b = np.moveaxis(a, source=0, destination=1) # 0을 1위치로 옮겨라
c = np.moveaxis(a, source=0, destination=2) # 0을 2위치로 옮겨라
d = np.moveaxis(a, source=0, destination=-1) # 0을 -1위치로 옮겨라
print(f"a: {a}")
print(f"a.shape: {a.shape}") # (3, 4, 5, 6)
print(f"b: {b}")
print(f"b.shape: {b.shape}") # (4, 3, 5, 6)
print(f"c: {c}")
print(f"c.shape: {c.shape}") # (4, 5, 3, 6)
print(f"d: {d}")
print(f"d.shape: {d.shape}") # (4, 5, 6, 3)
print()

# np.transpose()
a = np.random.normal(size=(3, 4))
b = np.transpose(a)
c = a.T
print(f"a: {a}")
print(f"a.shape: {a.shape}") # (3, 4)
print(f"b: {b}")
print(f"b.shape: {b.shape}") # (4, 3)
print(f"c: {c}")
print(f"c.shape: {c.shape}") # (4, 3)
print()

a = np.random.normal(size=(3, 4, 5, 6, 7))
b = np.transpose(a)
c = a.T
print(f"a: {a}")
print(f"a.shape: {a.shape}") # (3, 4, 5, 6, 7)
print(f"b: {b}")
print(f"b.shape: {b.shape}") # (7, 6, 5, 4, 3)
print(f"c: {c}")
print(f"c.shape: {c.shape}") # (7, 6, 5, 4, 3)
print()

a = np.random.normal(size=(3, 4, 5))
b = np.transpose(a, axes=(0, 1, 2))
c = np.transpose(a, axes=(1, 2, 0))
d = np.transpose(a, axes=(2, 0, 1))
e = np.transpose(a, axes=(2, 1, 0))
print(f"a: {a}")
print(f"a.shape: {a.shape}") # (3, 4, 5)
print(f"b: {b}")
print(f"b.shape: {b.shape}") # (3, 4, 5)
print(f"c: {c}")
print(f"c.shape: {c.shape}") # (4, 5, 3)
print(f"d: {d}")
print(f"d.shape: {d.shape}") # (5, 3, 4)
print(f"e: {e}")
print(f"e.shape: {e.shape}") # (5, 4, 3)
print()


##############################################################################
# id(): identity operators (아이디 연산자)
# id: 양쪽 연산자가 동일한 object를 가르키는지 아닌지 검사
# is not: 양쪽 연산자가 다른 object를 가르키는지 아닌지 검사
# 동일한 객체 여부를 판별하는 연산자
# 객체를 입력값으로 받아서 객체의 고유값 (reference)를 반환하는 함수
# 파이썬이 객체를 구별하기 위해서 부여하는 고유주소 (숫자로써는 의미가 없음)
# 고유주소는 객체가 메모리 안에 위치해있는 주소를 말함
# 객체의 수명동안 유일하고 바뀌지 않는 특징이 있음
# 동일한 객체 여부를 판별할 때 사용
a = 10
b = 10
c = 11
print(a, 'id =', id(a))
print(b, 'id =', id(b))
print(c, 'id =', id(c))
print(f"a is b : {a is b}")
print(f"a == b : {a == b}")
print(f"b is c : {b is c}")
print(f"b == c : {b == c}")
print(f"a is c : {a is c}")
print(f"a == c : {a == c}")
print()

a = '한사람'
b = '한사람'
c = '두사람'
print(a, 'id =', id(a))
print(b, 'id =', id(b))
print(c, 'id =', id(c))
print(f"a is b : {a is b}")
print(f"a == b : {a == b}")
print(f"b is c : {b is c}")
print(f"b == c : {b == c}")
print(f"a is c : {a is c}")
print(f"a == c : {a == c}")
print()

d = c
print(c, 'id =', id(c))
print(d, 'id =', id(d))
print(f"c is d : {c is d}")
print(f"c == d : {c == d}")
print()

c = '세사람'
print(c, 'id =', id(c))
print(d, 'id =', id(d))
print(f"c is d : {c is d}")
print(f"c == d : {c == d}")
print()


##############################################################################
# python object copy

# 일반 복사 (copy)
# 원본 객체의 참조값까지 복사하기 떄문에 복사된 객체 원소가 달라지면 원본 객체도 달라짐
# 그저 객체할당으로 복사
a = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b = a
print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")

b[0] = 100
print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")

b[3][0] = 400
print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print()

# 얕은 복사 (shallow copy)
# 일반 copy와 달리 copy 라이브러리 임포트 후에 copy.copy() 메서드로 복사
# shallow copy는 원본 객체와 다른 참조값을 생성함 (일반 copy는 원본 객체와 같은 참조값 새성)
import copy
a = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b = copy.copy(a)

# 주소값이 다름
# 원본 객체를 건드리지 않고 사본을 만들 수 있음
print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")

b[0] = 100
print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")


# 얕은 복사이기 떄문에 중첩된 객체에 대해서 그대로 변경이 일어남
# 얕은 복사는 세부 객체까지 복사하지 못함 (세부 객체에 대해서는 동일한 주소값을 가리키고 있음)
b[3].append(650)
b[4][0] = 700
print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print()


# 깊은 복사 (deep copy)
# shallow copy는 중첩 객체 (2차 이상의 리스트)의 영역까지 복사하지 못함
# 깊은 복사는 이런 한계점을 넘어 중첩 객체에 대해서도 완벽히 복사할 수 있음
# copy.deepcopy() 메소드 사용
a = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
b = copy.deepcopy(a)

# 주소값이 다름
# 원본 객체를 건드리지 않고 사본을 만들 수 있음
print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")

b[0] = 100
print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")

b[3].append(650)
b[4][0] = 700
print(f"a: {a}, id(a): {id(a)}")
print(f"b: {b}, id(b): {id(b)}")
print()

# 깊은 복사는 새로운 메모리 공간을 사용하기 때문에 1억개의 원소를 지닌 리스트를 deepcopy 한다면 메모리 소요 심함
# 상황을 고려하여 개발자가 선택해야 함

##############################################################################
# numpy copy(), view(), base

# 1) assignment operator
# creating array
arr = np.array([2, 4, 6, 8, 10])

# assigning arr to nc (default)
# it is good for saving memory, but sharing address means you may not protect your original array
nc = arr

# both arr and nc have same id
# access same address
print("id of arr:", id(arr))
print("id of nc:", id(nc))

# updating nc
nc[0] = 12

# printing the values
print("original array- ", arr)
print("assigned array- ", nc)
print()


# 2) numpy view() (shallow copy)
# creating array
arr = np.array([2, 4, 6, 8, 10])

# creating view
v = arr.view()

# both arr and v have different id
# but share address of list, while variables have different id
print("id of arr:", id(arr))
print("id of v:", id(v))

# changing original array
# will effect view
arr[0] = 12


# printing array and view
print("original array- ", arr)
print("view- ", v)
print()


# 3) numpy copy() (deep copy)
# do not share address of list, as well as variables

# creating array
arr = np.array([2, 4, 6, 8, 10])

# creating copy of array
c = arr.copy()

# both arr and c have different id
print("id of arr:", id(arr))
print("id of c:", id(c))

# changing original array
# this will not effect copy
arr[0] = 12

# printing array and copy
print("original array- ", arr)
print("copy- ", c)
print()

# numpy base()
# check if reference of array
# creating array
arr = np.array([2, 4, 6, 8, 10])

# creating copy of array
c = arr.copy()

# creating view of array
v = arr.view()

# printing base attribute of copy and view
print(c.base)
print(v.base)
print()

# 4) flatten()
# assign new address and copy element to b
a = np.random.randint(0, 10, (2, 3))
print('[before]\n a', a)

b = a.flatten() # array -> vector
b[0] = -10
print('[after]\n a', a)
print('[after]\n b', b)
print()

# 5) ravel()
# share address of a with b
a = np.random.randint(0, 10, (2, 3))
print('[before]\n a', a)

b = a.ravel() # array -> vector
b[0] = -10
print('[after]\n a', a)
print('[after]\n b', b)
print()

# 6) base()
# base of flatten
a = np.arange(4)
b = a.flatten()
print('[before]\n b', b)

b[0] = 100
print('b.base:', b.base is a, '\n')
print('a:', a)
print('[after]\n a', a)
print()

# base of ravel
a = np.arange(4)
b = a.ravel()
print('[before]\n b', b)

b[0] = 100
print('b.base:', b.base is a, '\n')
print('a:', a)
print('[after]\n a', a)
print()

# 7) np.resize() vs np.reshape()
# np.reshape()
a = np.arange(10)
print(f"a ndarray: {a}, a.shape: {a.shape}")
print(f"b ndarray: {b}, b.shape: {b.shape}")

b = np.reshape(a, (2, 5))
print(f"a ndarray: {a}, a.shape: {a.shape}")
print(f"b ndarray: {b}, b.shape: {b.shape}")

b = a.reshape((2, 5))
print(f"a ndarray: {a}, a.shape: {a.shape}")
print(f"b ndarray: {b}, b.shape: {b.shape}")
print()

# np.resize()
a = np.arange(10)
print(f"a ndarray: {a}")
print(f"b ndarray: {b}")

b = np.resize(a, (2, 5)) # there has returnv value, original a is not changed
print(f"a ndarray: {a}")
print(f"b ndarray: {b}")

b = a.resize((2, 5)) # there has no return, original a is changed
print(f"a ndarray: {a}")
print(f"b ndarray: {b}")
print()

# if size of array is not match to size you want to resize
# np.reshape() -> error
# a = np.arange(10)
# b = np.reshape(a, (4, 4))
# b = a.reshape((4, 4))
# print(f"a ndarray: {a}, a.shape: {a.shape}")
# print(f"b ndarray: {b}, b.shape: {b.shape}")
# print()

# np.resize() -> no error
# a = np.arange(10)
# b = np.resize(a, (4, 4)) # element is rewritten by original element at left location
# print(f"a ndarray: {a}")
# print(f"b ndarray: {b}")
# print()

# exercise
print("rehshape()")
a = np.arange(6)
b = np.reshape(a, (3, 2))
print(f"a ndarray: {a}")
print(f"b ndarray: {b}")
print()
# share memory of a with b
b[2, 0] = 100
print(f"a ndarray: {a}")
print(f"b ndarray: {b}")
print()

print("reshape().copy()")
a = np.arange(6)
b = np.reshape(a, (3, 2)).copy()
print(f"a ndarray: {a}")
print(f"b ndarray: {b}")
print()
# does not share memory of a with b using copy() method
b[2, 0] = 100
print(f"a ndarray: {a}")
print(f"b ndarray: {b}")
print()

print("resize()")
a = np.arange(6)
b = np.resize(a, (3, 2))
print(f"a ndarray: {a}")
print(f"b ndarray: {b}")
print()
# share memory of a with b
b[2, 0] = 100
print(f"a ndarray: {a}")
print(f"b ndarray: {b}")
print()
##############################################################################

# 