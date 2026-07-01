# 📘 Algorithms and Data Structures (AiSD)

An educational repository with algorithm implementations, solved problems, and exam-prep materials for the "Algorithms and Data Structures" course at the Financial University.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Telegram](https://img.shields.io/badge/Telegram-@shipovm-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/shipovm)

---

## 📂 Project structure

The project is organized as **work type → month → day (or topic)**.

| Section | Description | Contents |
| :--- | :--- | :--- |
| [**`exam/`**](./exam/) | Exam preparation | Topic-by-topic practice problems (OOP, decorators, stacks, linked lists, arrays, higher-order functions, sorting), personal practice sets, and exam docs (question list, task list, personal notes) |
| [**`classwork/`**](./classwork/) | In-class practicals | Scripts and problem breakdowns from lessons, organized by date |
| [**`homework/`**](./homework/) | Homework assignments | Individual assignments by lecture topic, including a mock-interview problem set |

### 🌳 File map
```text
.
├── exam/
│   ├── docs/                        # Exam question list, task list, personal prep notes
│   ├── practice/                    # Topic-based practice, numbered by track
│   │   ├── 10_OOP/                  # Classes, encapsulation, magic methods (33 tasks)
│   │   ├── 20_Decorators/           # Decorators, higher-order functions (10 tasks)
│   │   ├── 30_Stack/                # Stack-based problems (13 tasks)
│   │   ├── 40_Singly linked lists/  # Singly linked list problems (7 tasks)
│   │   ├── 50_Array/                # Array problems (6 tasks)
│   │   ├── 60_Higher_order_functions/ # map/filter/reduce style problems (9 tasks)
│   │   └── 70_Sorting/              # Sorting algorithms (4 tasks)
│   └── practice_for_me/             # Personal timed practice sets (1–5, 5 tasks each)
├── classwork/
│   ├── 02/                          # February
│   │   ├── 13/                      # OOP basics, classes
│   │   ├── 20/                      # OOP, encapsulation
│   │   └── 27/                      # Pseudocode, Yandex.Contest problems (1–11)
│   ├── 03/                          # March
│   │   ├── 06/                      # Inheritance, OOP
│   │   ├── 13/                      # Magic methods, class methods
│   │   ├── 20/                      # Typed OOP (Vehicle hierarchy)
│   │   └── 27/                      # Functional programming, recursion, Money class
│   ├── 04/                          # April
│   │   ├── 02/                      # Fibonacci numbers (recursion), docstring dictionaries
│   │   ├── 10/                      # Practice tasks
│   │   ├── 17/                      # Sum of odd numbers, palindromes, mazes, staircases
│   │   └── 24/                      # Practice tasks
│   ├── 05/                          # May
│   │   ├── 15/, 20/, 22/            # Practice tasks
│   └── 06/                          # June
│       └── 05/                      # Practice tasks
└── homework/
    ├── 02/                          # 13.py, 20.py — OOP tasks, Clock class
    ├── 03/                          # 06.py — Employee/FullTime/PartTime (inheritance)
    │                                 # 13.py — Student hierarchy + generic search
    ├── 04/
    │   ├── 15/, 16/                 # Practice tasks
    │   └── 23_Interview/            # Mock technical interview: two pointers, sliding
    │                                 # window, hash maps, stacks, BFS/queue, recursion &
    │                                 # divide-and-conquer, DP, linked lists, palindromes, LCS
    └── 05/                          # 11/, 18/, 22/, 27/ — practice tasks (includes a Go solution)
```

---

## 🛠 Key topics and concepts

- **🧱 OOP:** Deep work with classes, encapsulation, and magic methods (`__init__`, `__str__`, `__repr__`, `__add__`, `__eq__`, etc.).
- **🔁 Inheritance:** Base and derived classes, method overriding, `super()`.
- **📐 Algorithms:** Recursion (factorial, Fibonacci), sorting algorithms, geometric primitives, drawing algorithms.
- **🔗 Functional programming:** Decorators, `map`/`filter`/`reduce`, `*args`/`**kwargs`, closures, higher-order functions.
- **📚 Data structures:** Stacks, singly linked lists, arrays, hash maps.
- **🎯 Interview-style problems:** Two pointers, sliding window, BFS/queue, divide-and-conquer, dynamic programming, LCS, palindromes.
- **📝 Problem solving:** Yandex.Contest problem analysis and optimization.

---

## 🚀 Quick start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shipovmax/AiSD_repo.git
   cd AiSD_repo
   ```

2. **Run a script:**
   Pick any file and run it with Python:
   ```bash
   python3 exam/practice/10_OOP/1.py
   ```

---

## 📈 Roadmap
- [ ] Add unit tests for the algorithms.
- [ ] Add sorting visualizations.
- [ ] Expand the dynamic programming section.

---

<p align="center">
  <i>Made with ❤️ for learning and self-improvement</i>
</p>
