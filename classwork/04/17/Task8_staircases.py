import tkinter as tk
from tkinter import messagebox


def count_staircases(n: int) -> tuple[int, list[list[int]]]:
    results = []

    def helper(remaining: int, min_step: int, current: list):
        step = min_step
        while step <= remaining:
            if remaining - step == 0 and len(current) >= 1:
                results.append(current + [step])
            elif remaining - step >= step + 1:
                helper(remaining - step, step + 1, current + [step])
            step += 1

    helper(n, 1, [])
    return len(results), results


def run_staircase_gui():
    root = tk.Tk()
    root.title("Лесенки — задача 8")
    root.resizable(False, False)

    frame_top = tk.Frame(root, pady=10)
    frame_top.pack()

    tk.Label(frame_top, text="Количество кубиков n:", font=("Arial", 12)).pack(side="left", padx=6)

    entry = tk.Entry(frame_top, font=("Arial", 12), width=6, justify="center")
    entry.insert(0, "6")
    entry.pack(side="left", padx=6)

    result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="#1976D2")
    result_label.pack()

    canvas = tk.Canvas(root, bg="white", width=700, height=400)
    canvas.pack(padx=10, pady=10)

    def draw_staircases(staircases: list[list[int]]):
        canvas.delete("all")

        if not staircases:
            canvas.create_text(350, 200, text="Нет лесенок", font=("Arial", 14), fill="#888")
            return

        block = 20
        gap = 14
        x_offset = 10
        y_offset = 10
        max_height = max(sum(s) for s in staircases) * block
        canvas_height = max_height + y_offset * 2 + 30

        total_width = sum(max(s) * block + gap for s in staircases) + x_offset
        canvas.config(width=max(700, total_width), height=max(400, canvas_height))

        colors = ["#90CAF9", "#A5D6A7", "#FFCC80", "#F48FB1", "#CE93D8", "#80DEEA"]

        for idx, staircase in enumerate(staircases):
            color = colors[idx % len(colors)]
            col_x = x_offset
            for col_idx, height in enumerate(staircase):
                for block_idx in range(height):
                    bx1 = col_x + col_idx * block
                    by1 = y_offset + max_height - (block_idx + 1) * block
                    bx2 = bx1 + block - 1
                    by2 = by1 + block - 1
                    canvas.create_rectangle(bx1, by1, bx2, by2,
                                            fill=color, outline="#546E7A", width=1)

            label_x = x_offset + len(staircase) * block // 2
            canvas.create_text(
                label_x, y_offset + max_height + 14,
                text="+".join(map(str, staircase)),
                font=("Arial", 8), fill="#333"
            )

            x_offset += len(staircase) * block + gap

    def on_calculate():
        try:
            n = int(entry.get())
            if n <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Ошибка", "Введите натуральное число")
            return

        count, staircases = count_staircases(n)
        result_label.config(text=f"Количество лесенок из {n} кубиков: {count}")
        draw_staircases(staircases)

    btn = tk.Button(root, text="Посчитать", command=on_calculate,
                    font=("Arial", 12, "bold"), bg="#1976D2", fg="white",
                    padx=14, pady=5, relief="flat", cursor="hand2")
    btn.pack(pady=6)

    on_calculate()
    root.mainloop()


if __name__ == "__main__":
    run_staircase_gui()