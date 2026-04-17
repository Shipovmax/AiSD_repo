def is_solvable(maze: list[str]) -> bool:
    rows = len(maze)
    cols = len(maze[0])

    start = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
                break

    def dfs(r: int, c: int, visited: set) -> bool:
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        if (r, c) in visited:
            return False
        if maze[r][c] == '#':
            return False
        if maze[r][c] == 'X':
            return True

        visited.add((r, c))
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if dfs(r + dr, c + dc, visited):
                return True
        return False

    return dfs(*start, set())