import copy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def dfs(scnt, sum):
    global seq, N, ans
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    check = [[False for _ in range(N)] for _ in range(N)]
    dup = copy.deepcopy(seq)

    for i in range(2 * N, 3 * N):
        for j in range(N):
            val = dup[i][j]
            if val == 0 or check[i - 2 * N][j]: continue

            # initialization
            seq = copy.deepcopy(dup)
            minX = j
            maxX = j
            minY = i
            maxY = i
            q = []
            same = 1
            q.append(Point(j, i))
            check[i - 2 * N][j] = True

            while len(q) > 0:
                cx = q[0].x
                cy = q[0].y
                seq[cy][cx] = 0  # make it clear
                q.pop(0)
                minX = min(minX, cx)
                maxX = max(maxX, cx)
                minY = min(minY, cy)
                maxY = max(maxY, cy)

                for d in range(4):
                    nx = cx + dx[d]
                    ny = cy + dy[d]
                    if 0 <= nx < N and 2 * N <= ny < 3 * N and not check[ny - 2 * N][nx] and dup[ny][nx] == val:
                        check[ny - 2 * N][nx] = True
                        q.append(Point(nx, ny))
                        same += 1

            if scnt < 2:
                # make array disappear
                for k in range(minX, maxX + 1, 1):
                    for m in range(maxY, minY - 1, -1):
                        if seq[m][k] != 0: continue
                        jump = 0
                        for l in range(m - 1, -1, -1):
                            if seq[l][k]:
                                jump = m - l
                                break
                        if jump:
                            for u in range(m, jump - 1, -1):
                                seq[u][k] = seq[u - jump][k]
                                seq[u - jump][k] = 0
                dfs(scnt + 1, sum + same + (maxX - minX + 1) * (maxY - minY + 1))
            else:
                ans = max(ans, sum + same + (maxX - minX + 1) * (maxY - minY + 1))


if __name__ == '__main__':
    ans = 0
    N = int(input())
    seq = [[0 for _ in range(N)] for _ in range(3 * N)]
    for i in range(len(seq)):
        tmp: list = input().split()
        for j in range(len(seq[0])):
            seq[i][j] = int(tmp[j])
    dfs(0, 0)
    print(ans)
