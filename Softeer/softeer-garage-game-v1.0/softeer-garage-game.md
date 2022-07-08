## [인증평가(2차) 기출] Garage game
- 난이도 3/5
- 정답률 10.00%
- https://softeer.ai/practice/info.do?idx=1&eid=540

### 제약조건
- 1 ≤ N ≤ 15
- 색상 번호는 1 이상 10<sup>9</sup>이하의 자연수




--------------------------------------------------------

#### 복잡도
- 시간 복잡도 - 알고리즘 수행 시간
- 공간 복잡도 - 알고리즘의 메모리 사용량

#### 시간 복잡도
- 코딩 테스트 문제의 시간제한은 대략 5초
- python이 초당 2천만번 연산이 가능하다고 가정하는 것이 좋음 (5초에 1억번) 
(20,000,000 == 2*10^7)

ex) 시간제한이 1초인 문제를 만났을 떄, 일반적인 기준은 다음과 같음:
- N의 범위가 500인 경우: 시간 복잡도가 O(N^3)인 알고리즘을 설계하면 문제를 해결할 수 있음
- N의 범위가 2,000인 경우: 시간 복잡도가 O(N^2)인 알고리즘을 설계하면 문제를 해결할 수 있음
- N의 범위가 100,000인 경우: 시간 복잡도가 O(NlogN)인 알고리즘을 설계하면 문제를 해결할 수 있음
- N의 범위가 10,000,000인 경우: 시간 복잡도가 O(N)인 알고리즘을 설계하면 문제를 해결할 수 있음


#### 연산 횟수에 따른 시간 복잡도
- 연산 횟수가 5억
- C언어 - 1 ~ 3초
- python - 5 ~ 15초 (pypy는 때떄로 C보다 빠름)


#### 파이썬의 자료구조
- list, tuple: O(n) (선형 순회)
- set, dict: O(1) ~ O(n) 
(hash를 통해 저장하므로 접근시간은 O(1), 단 해쉬의 충돌이 많아 성능이 떨어지는 경우 O(n)

--------------------------------------------------------



 
### 입력형식
- 입력으로는 차고 격자 칸의 가로, 세로 길이인 N이 첫 줄에 주어짐
- 다음 3N개의 줄에 N개의 자연수가 주어짐
- 각 자연수는 차고 칸에 있는 자동차의 색상 번호임


 
### 출력형식
- 주어진 조건에서 게임을 3차례 시뮬레이션 했을 때 얻을 수 있는 가장 큰 점수를 출력


### 입력예제1
2  
1 1   
2 2  
1 1  
3 3  
4 4  
1 2  


### 출력예제1
15


### 입력예제2
3  
8 5 1  
9 6 1  
10 7 1  
11 1 3  
12 1 3  
13 1 3  
1 2 2  
1 2 2  
1 2 2  



### 출력예제2
36
