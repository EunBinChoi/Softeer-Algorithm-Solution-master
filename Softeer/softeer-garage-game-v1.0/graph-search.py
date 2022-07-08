"""
DFS (Depth-First Search: 깊이 우선 탐색)와 BFS (Breadth-First Search: 너비 우선 탐색)는
그래프의 정점을 방문하는 그래프 탐색 (Graph Search or Graph Traversal: 그래프 운행) 방법
보통 python에서 그래프는 아래와 같이 딕셔너리를 활용해서 인접 리스트로 구현하는 경우가 많음

ex) DFS는 스택이나 재귀로 BFS는 큐로 구현
"""

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: []
}

"""
[ DFS (깊이 우선 탐색) ]
임의의 한쪽 방향으로 갈 수 있을 때까지 가다가 더이상 갈 수 없게 되면 가장 가까운 갈림길로 돌아와서
그곳으로 다른 방향으로 다시 탐색을 진행하는 것을 말함
이때, 갈림길로 돌아가기 위해서는 스택이 필요하지만 재귀함수 호출로 묵시적인 스택 사용이 가능
"""

"""
[ DFS 재귀 구현 ]
DFS를 재귀로 구현하는 경우의 수도 코드는 다음과 같음
정점을 방문하되 방문되었다고 표시하고 해당 정점의 인접 간선을 모두 탐색하는 것
해당 정점이 방문되지 않았다면 해당 정점에 대해서 다시 DFS를 호출하는 형태
정점의 인접 간선을 하나하나씩 타고 들어간 후 탐색이 불가능하면 빠져나와 다른 인접 간선을 이와 동일한 방식으로 탐색

DFS(G, v)
    visit v;
    mark v as visited;
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not marked as visited then 
            recursively call DFS(G, w)
    
def recursive_dfs(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if not w in visited:
            visited = recursive_dfs(w, visited)
    return visited
"""

"""
[ DFS 스택 구현 ]
스택을 이용하는 경우에는 반복문을 이용해서 구현할 수 있음
스택을 이용해 모든 인접 간선을 추출하고 다시 도착점인 정점을 스택에 삽입하는 구조로 구현 가능

DFS(G, v)
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not marked as visited then
            mark v as visited
            for all edges from v to w in G.adjacentEdges(v) do
                S.push(w)

스택에 한 번에 모든 인접 간선의 정점을 push하기 때문에 BFS로 오해하기 쉬우나 
여기서 염두해야할 점은 stack에 push될 때가 아니라 
pop하면서 방문을 check하는 구조이기 때문에 정점 방문 순서로 본다면 dfs가 맞음
스택의 LIFO 구조를 잘 활용한 것

def iterative_dfs(start_v):
    visited = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
return visited
        
"""

"""
[ 효율성 ]
- 공간 복잡도
 : 그래프와 visited, stack을 모두 고려해야 함
 : 인접 행렬로 구현하는 경우에는 하나의 정점과 모든 정점 간의 연결 관계를 표현: O(n * n)
 : 인접 리스트의 경우에는 그래프 내 정점 개수 n, 간선 개수 m라고 가정: O(n + m)
 : DFS의 효율성에 대해 말할 경우 stack, visited는 모두 O(n)의 공간 복잡도를 가지고 있음 (정점의 개수: n)
 
- 시간 복잡도
 : 인접 행렬로 구현하는 경우에는 하나의 정점과 모든 정점 간의 연결 관계를 표현: O(n * n)
 : 인접 리스트의 경우에는 그래프 내 정점 개수 n, 간선 개수 m라고 가정: O(n + m)
   -> 정점 방문 & 해당 정점의 인접 정점 방문
 : 모든 정점을 다 탐색해야되기 때문에 시간 복잡도와 공간 복잡도는 같음
"""

"""
[ BFS (너비 우선 탐색) ]
시작 정점으로부터 거리 가까운 정점들을 먼저 차례로 방문하고 멀리 떨어져있는 정점을 나중에 방문하는 운행 방법
(점차 영역을 넓혀나간다고 생각하기 쉬움)

BFS는 DFS보다 쓰임새는 적지만 다익스트라 알고리즘과 같이 최단 경로 탐색시 많이 활용됨
BFS는 보통 큐를 통해 구현
    
BFS(G, v)
    let Q be a queue
    mark v as visited
    while Q is not empty do
        v := Q.dequeue()
"""