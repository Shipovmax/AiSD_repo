class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        field = [["." for _ in range(40)] for _ in range(40)]
        if 0 <= self.y < 40 and 0 <= self.x < 40:
            field[self.y][self.x] = "*"

        print("40x40 field:")
        for row in field:
            print("".join(row))


# 2) Create a figure object.
figure = Figure(5, 5)

# 4) Draw the figure.
figure.draw()

# 5) Change the parameters and draw again.
figure.x = 20
figure.y = 15
figure.draw()
