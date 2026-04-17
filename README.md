# 📘 Algorithms and Data Structures (AiSD)

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Telegram](https://img.shields.io/badge/Telegram-@shipovm-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/shipovm)

> Educational repository with algorithm implementations, problem solutions, and course study materials.

---

## 📂 Project Structure

The project is organized using the following hierarchy: **Work Type → Month → Day**.

| Section | Description | Contents |
| :--- | :--- | :--- |
| [**`classwork/`**](./classwork/) | In-class practice | Python scripts, Yandex problem walkthroughs, pseudocode |
| [**`homework/`**](./homework/) | Homework assignments | Individual tasks based on lecture topics |

### 🌳 File Map
```text
.
├── classwork/             # In-class practical work
│   ├── 02/                # February
│   │   ├── 13/            # Feb 13 — OOP basics, classes
│   │   ├── 20/            # Feb 20 — OOP, encapsulation
│   │   └── 27/            # Feb 27 — Pseudocode, Yandex problems (tasks 1–11)
│   ├── 03/                # March
│   │   ├── 06/            # Mar 06 — Inheritance, OOP
│   │   ├── 13/            # Mar 13 — Magic methods, class methods
│   │   ├── 20/            # Mar 20 — OOP with type hints (Vehicle hierarchy)
│   │   └── 27/            # Mar 27 — Functional programming, recursion, money class
│   │       ├── factorial.py
│   │       ├── 1.py       # Plane class (variant 2)
│   │       ├── 2.py       # Computer class with inheritance
│   │       ├── 3.py       # Money class with magic methods
│   │       ├── Лекция_12.ipynb
│   │       └── ФП_полное_руководство.md
│   └── 04/                # April
│       └── 02/            # Apr 02 — Fibonacci (recursion), docstring-based dict
└── homework/              # Independent work
    ├── 02/                # February
    │   ├── 13.py          # OOP tasks
    │   └── 20.py          # Clock class (minutes → hours/seconds)
    └── 03/                # March
        ├── 06.py          # Employee/FullTime/PartTime (inheritance, vacation)
        └── 13.py          # Student hierarchy + universal search
```

---

## 🛠 Key Topics and Concepts

- **🧱 OOP:** In-depth work with classes, encapsulation, and magic methods (`__init__`, `__str__`, `__repr__`, `__add__`, `__eq__`, etc.).
- **🔁 Inheritance:** Base and derived classes, method overriding, `super()`.
- **📐 Algorithms:** Recursive algorithms (factorial, Fibonacci), drawing algorithms (pseudo-graphics), and geometric primitives.
- **🔗 Functional Programming:** Decorators, `map`/`filter`/`reduce`, `*args`/`**kwargs`, monads, currying, pattern matching.
- **🔐 Cryptography:** Basic encryption algorithms such as the Caesar cipher.
- **📝 Problem Solving:** Analysis and optimization of tasks from Yandex Contest.

---

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shipovmax/AiSD_repo.git
   cd AiSD_repo
   ```

2. **Run a script:**
   Choose the required file and run it with Python:
   ```bash
   python3 classwork/03/06/main.py
   ```

---

## 📈 Development Plans
- [ ] Add unit tests for algorithms.
- [ ] Add sorting visualizations.
- [ ] Expand the dynamic programming section.

---

<p align="center">
  <i>Made with ❤️ for study and self-development</i>
</p>
