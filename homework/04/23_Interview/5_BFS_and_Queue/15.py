'''
Дана матрица 0/1 (0 — путь, 1 — стена).
Найди длину кратчайшего пути из (0,0) в (n-1,m-1).
'''

from collections import deque


def shortest_path(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])

    if grid[0][0] == 1 or grid[n - 1][m - 1] == 1:
        return -1

    queue = deque([(0, 0, 1)])
    visited = {(0, 0)}
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        r, c, dist = queue.popleft()

        if r == n - 1 and c == m - 1:
            return dist

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1


# Тесты
grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
print(shortest_path(grid))  # 5
