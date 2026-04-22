import tkinter as tk
from tkinter import messagebox

MAZE = ["S----", "##---", "---##", "----X"]

CELL = 60


def solve_maze(maze: list[str]) -> list[str]:
    rows = len(maze)
    cols = len(maze[0])

    start = None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == "S":
                start = (r, c)
                break

    DIRS = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
    }

    def dfs(r: int, c: int, visited: set, path: list) -> list | None:
        if not (0 <= r < rows and 0 <= c < cols):
            return None
        if (r, c) in visited:
            return None
        if maze[r][c] == "#":
            return None
        if maze[r][c] == "X":
            return path

        visited.add((r, c))

        for direction, (dr, dc) in DIRS.items():
            result = dfs(r + dr, c + dc, visited, path + [direction])
            if result is not None:
                return result

        visited.discard((r, c))
        return None

    result = dfs(*start, set(), [])
    return result if result is not None else []


def run_maze_gui():
    maze = MAZE
    rows = len(maze)
    cols = len(maze[0])

    root = tk.Tk()
    root.title("Лабиринт — задача 7")
    root.resizable(False, False)

    canvas = tk.Canvas(root, width=cols * CELL, height=rows * CELL, bg="white")
    canvas.pack()

    COLORS = {
        "S": "#4CAF50",
        "X": "#F44336",
        "-": "#FFFFFF",
        "#": "#424242",
        "P": "#90CAF9",
    }

    cell_ids = {}

    def draw_maze(highlight_cells=None):
        canvas.delete("all")
        for r in range(rows):
            for c in range(cols):
                char = maze[r][c]
                x1, y1 = c * CELL, r * CELL
                x2, y2 = x1 + CELL, y1 + CELL

                if (
                    highlight_cells
                    and (r, c) in highlight_cells
                    and char not in ("S", "X")
                ):
                    color = COLORS["P"]
                else:
                    color = COLORS.get(char, "#FFFFFF")

                rect = canvas.create_rectangle(
                    x1, y1, x2, y2, fill=color, outline="#BDBDBD", width=1
                )
                cell_ids[(r, c)] = rect

                if char in ("S", "X"):
                    canvas.create_text(
                        x1 + CELL // 2,
                        y1 + CELL // 2,
                        text=char,
                        font=("Arial", 18, "bold"),
                        fill="white",
                    )

    def on_solve():
        path = solve_maze(maze)

        if not path:
            messagebox.showinfo("Результат", "Лабиринт непроходим!")
            return

        r, c = None, None
        for row in range(rows):
            for col in range(cols):
                if maze[row][col] == "S":
                    r, c = row, col

        MOVES = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        visited_path = set()
        visited_path.add((r, c))

        for step in path:
            dr, dc = MOVES[step]
            r, c = r + dr, c + dc
            visited_path.add((r, c))

        draw_maze(highlight_cells=visited_path)

        steps_text = " → ".join(path)
        messagebox.showinfo("Путь найден", f"Шагов: {len(path)}\n\n{steps_text}")

    draw_maze()

    btn = tk.Button(
        root,
        text="Решить",
        command=on_solve,
        font=("Arial", 13, "bold"),
        bg="#1976D2",
        fg="white",
        padx=16,
        pady=6,
        relief="flat",
        cursor="hand2",
    )
    btn.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    run_maze_gui()
