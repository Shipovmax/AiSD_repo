def is_solvable(maze: list[str]) -> bool:
    rows, cols = len(maze), len(maze[0])

    def cell(r: int, c: int) -> str | None:
        return maze[r][c] if 0 <= r < rows and 0 <= c < cols else None

    def neighbors(r: int, c: int) -> list[tuple[int, int]]:
        return [
            (r + dr, c + dc)
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if cell(r + dr, c + dc) not in (None, '#')
        ]

    def find_char(ch: str) -> tuple[int, int] | None:
        return next(
            ((r, c) for r in range(rows) for c in range(cols) if maze[r][c] == ch),
            None
        )

    def bfs(queue: list[tuple[int, int]], visited: frozenset) -> bool:

        if not queue:
            return False

        current, *rest = queue

        if cell(*current) == 'X':
            return True

        new_visited = visited | {current}
        new_nodes = [n for n in neighbors(*current) if n not in new_visited]

        return bfs(rest + new_nodes, new_visited)

    start = find_char('S')
    return start is not None and bfs([start], frozenset())


# test
if __name__ == "__main__":
    maze_solvable = [
        "S...",
        "####",
        "...X",
    ]
    print(is_solvable(maze_solvable))  # False

    maze_with_path = [
        "S.#.",
        ".##.",
        "...X",
    ]
    print(is_solvable(maze_with_path))  # True

    maze_blocked = [
        "S...",
        "....",
        ".##.",
        ".#X#",
        ".###",
    ]
    print(is_solvable(maze_blocked))  # False

    maze_trivial = [
        "SX",
    ]
    print(is_solvable(maze_trivial))  # True