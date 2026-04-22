# Подготовка к собесу Яндекс — Backend Python

## Как пользоваться этим файлом
1. Читаешь разбор задачи — понимаешь паттерн
2. Смотришь живой пример с кодом
3. В конце файла — 50 задач в разнобой без решений, решаешь сам

---

# ЧАСТЬ 1 — РАЗБОР ПАТТЕРНОВ

---

## Паттерн 1: Two Pointers (Два указателя)

### Когда применять
Массив/строка, нужно найти пару/подстроку/проверить условие. Вместо O(n²) вложенного цикла — O(n) двумя указателями с двух сторон или в одну сторону.

### Почему так
Если массив отсортирован и ищем пару с суммой X — левый указатель двигаем вправо если сумма мала, правый влево если велика. Каждый элемент посещаем один раз.

### Задача 1: Two Sum в отсортированном массиве
**Условие:** Дан отсортированный массив и число target. Найди два индекса (1-based) элементов, сумма которых равна target.

**Разбор:** Классика two pointers. Левый = 0, правый = len-1. Если сумма < target — left++. Если > target — right--. Если == target — нашли.

```python
def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    left, right = 0, len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]  # 1-based
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# Тест
print(two_sum_sorted([2, 7, 11, 15], 9))  # [1, 2]
print(two_sum_sorted([2, 3, 4], 6))       # [1, 3]
```

**Сложность:** O(n) время, O(1) память

---

### Задача 2: Разворот строки на месте
**Условие:** Разверни строку (массив символов) на месте.

**Разбор:** Two pointers от краёв к центру, меняем местами.

```python
def reverse_string(s: list[str]) -> None:
    left, right = 0, len(s) - 1
    
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Тест
s = ['h', 'e', 'l', 'l', 'o']
reverse_string(s)
print(s)  # ['o', 'l', 'l', 'e', 'h']
```

---

### Задача 3: Контейнер с водой (Container With Most Water)
**Условие:** Дан массив высот. Найди два столбца, между которыми помещается максимум воды. Вода = min(h[l], h[r]) * (r - l).

**Разбор:** Two pointers. Сужаем сторону с меньшей высотой — только так можем увеличить площадь.

```python
def max_area(height: list[int]) -> int:
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        water = min(height[left], height[right]) * (right - left)
        max_water = max(max_water, water)
        
        # Сдвигаем меньший — больший не имеет смысла
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# Тест
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
```

---

## Паттерн 2: Sliding Window (Скользящее окно)

### Когда применять
Нужно найти подстроку/подмассив с каким-то условием (максимальная сумма, без повторов, все символы входят). Окно расширяется вправо, сужается слева при нарушении условия.

### Почему так
Вместо перебора всех подстрок O(n²) или O(n³) — движемся одним проходом O(n). Ключевая идея: поддерживаем состояние окна инкрементально.

### Задача 4: Самая длинная подстрока без повторяющихся символов
**Условие:** Найди длину самой длинной подстроки без повторяющихся символов.

**Разбор:** Скользящее окно + hashset. Правый указатель расширяет окно. Если символ уже есть — двигаем левый пока не уберём дубликат.

```python
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        # Убираем символы пока есть дубликат
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len

# Тест
print(length_of_longest_substring("abcabcbb"))  # 3 ("abc")
print(length_of_longest_substring("bbbbb"))     # 1 ("b")
print(length_of_longest_substring("pwwkew"))    # 3 ("wke")
```

---

### Задача 5: Максимальная сумма подмассива длины k
**Условие:** Дан массив и число k. Найди максимальную сумму подмассива длины ровно k.

**Разбор:** Фиксированное окно. Вычисляем сумму первых k элементов, потом скользим: добавляем правый, убираем левый.

```python
def max_sum_subarray(arr: list[int], k: int) -> int:
    if len(arr) < k:
        return -1
    
    # Сумма первого окна
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Скользим
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Тест
print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))  # 9 (5+1+3)
print(max_sum_subarray([2, 3, 4, 1, 5], 2))      # 7 (3+4)
```

---

### Задача 6: Минимальная длина подмассива с суммой >= target
**Условие:** Дан массив положительных чисел и target. Найди минимальную длину подмассива с суммой >= target.

**Разбор:** Динамическое окно. Расширяем пока сумма < target, потом сужаем слева пока условие выполняется, запоминаем минимум.

```python
def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(len(nums)):
        current_sum += nums[right]
        
        # Сужаем окно пока условие выполняется
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

# Тест
print(min_subarray_len(7, [2, 3, 1, 2, 4, 3]))  # 2 (4+3)
print(min_subarray_len(4, [1, 4, 4]))             # 1 (4)
```

---

## Паттерн 3: HashMap / HashSet

### Когда применять
Подсчёт частот, поиск за O(1), группировка элементов, проверка наличия.

### Почему так
dict/set в Python — O(1) на вставку/поиск в среднем. Часто превращает O(n²) решение в O(n).

### Задача 7: Two Sum (несортированный)
**Условие:** Дан массив и target. Верни индексы двух элементов, сумма которых равна target.

**Разбор:** Для каждого элемента ищем complement = target - nums[i] в хешмапе. Если есть — нашли. Если нет — добавляем текущий.

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}  # значение -> индекс
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

# Тест
print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
print(two_sum([3, 2, 4], 6))         # [1, 2]
```

---

### Задача 8: Анаграммы
**Условие:** Даны две строки. Определи, являются ли они анаграммами.

**Разбор:** Анаграмма = те же символы, те же частоты. Считаем частоты через Counter и сравниваем. Или сортируем — но O(n log n).

```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

# Вариант без Counter — O(n) памяти, O(n) время
def is_anagram_v2(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        count[c] = count.get(c, 0) - 1
    
    return all(v == 0 for v in count.values())

# Тест
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))           # False
```

---

### Задача 9: Группировка анаграмм
**Условие:** Дан список слов. Сгруппируй анаграммы вместе.

**Разбор:** Ключ = отсортированное слово (одинаковый для всех анаграмм). Группируем в dict.

```python
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    
    for word in strs:
        key = tuple(sorted(word))  # "eat" -> ('a','e','t')
        groups[key].append(word)
    
    return list(groups.values())

# Тест
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# [["eat","tea","ate"],["tan","nat"],["bat"]]
```

---

### Задача 10: Первый уникальный символ
**Условие:** Найди индекс первого неповторяющегося символа в строке. Если нет — верни -1.

```python
from collections import Counter

def first_uniq_char(s: str) -> int:
    count = Counter(s)
    
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    
    return -1

# Тест
print(first_uniq_char("leetcode"))   # 0
print(first_uniq_char("loveleet"))   # 2
print(first_uniq_char("aabb"))       # -1
```

---

## Паттерн 4: Стек (Stack)

### Когда применять
Задачи с вложенностью, скобками, "последний пришёл — первый вышел", отмена операций, монотонный стек.

### Задача 11: Валидные скобки
**Условие:** Дана строка из скобок ()[]{}. Определи, является ли она валидной.

**Разбор:** Открывающую — пушим в стек. Закрывающую — проверяем что на вершине стека соответствующая открывающая.

```python
def is_valid(s: str) -> bool:
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)
    
    return len(stack) == 0

# Тест
print(is_valid("()[]{}"))  # True
print(is_valid("([)]"))    # False
print(is_valid("{[]}"))    # True
```

---

### Задача 12: Минимальный стек
**Условие:** Реализуй стек с операциями push, pop, top и getMin за O(1).

**Разбор:** Храним два стека — основной и стек минимумов. При push в стек минимумов пушим min(новый, текущий минимум).

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.min_stack[-1]

# Тест
ms = MinStack()
ms.push(-2)
ms.push(0)
ms.push(-3)
print(ms.getMin())  # -3
ms.pop()
print(ms.top())     # 0
print(ms.getMin())  # -2
```

---

### Задача 13: Вычисление обратной польской нотации
**Условие:** Вычисли значение выражения в обратной польской нотации. Пример: ["2","1","+","3","*"] = (2+1)*3 = 9.

```python
def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {'+', '-', '*', '/'}
    
    for token in tokens:
        if token in ops:
            b, a = stack.pop(), stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(int(a / b))  # truncate toward zero
        else:
            stack.append(int(token))
    
    return stack[0]

# Тест
print(eval_rpn(["2","1","+","3","*"]))          # 9
print(eval_rpn(["4","13","5","/","+"]))          # 6
```

---

## Паттерн 5: Очередь и BFS

### Когда применять
Обход графа/дерева в ширину, кратчайший путь в невзвешенном графе, задачи "уровнями".

### Задача 14: Обход бинарного дерева по уровням
**Условие:** Дано бинарное дерево. Верни список уровней (каждый уровень — отдельный список).

```python
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

---

### Задача 15: Кратчайший путь в лабиринте
**Условие:** Дана матрица 0/1 (0 — путь, 1 — стена). Найди длину кратчайшего пути из (0,0) в (n-1,m-1).

**Разбор:** BFS по клеткам. Каждый шаг = уровень BFS = +1 к длине пути.

```python
from collections import deque

def shortest_path(grid: list[list[int]]) -> int:
    n, m = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[n-1][m-1] == 1:
        return -1
    
    queue = deque([(0, 0, 1)])  # row, col, distance
    visited = {(0, 0)}
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    
    while queue:
        r, c, dist = queue.popleft()
        
        if r == n-1 and c == m-1:
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited and grid[nr][nc] == 0:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return -1

# Тест
grid = [[0,0,0],[1,1,0],[1,1,0]]
print(shortest_path(grid))  # 4
```

---

## Паттерн 6: Рекурсия и разделяй-властвуй

### Задача 16: Бинарный поиск
**Условие:** Найди индекс элемента в отсортированном массиве. Если нет — верни -1.

**Разбор:** Классика. Каждый шаг делим пространство поиска пополам. O(log n).

```python
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # избегаем overflow
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Тест
print(binary_search([-1,0,3,5,9,12], 9))   # 4
print(binary_search([-1,0,3,5,9,12], 2))   # -1
```

---

### Задача 17: Поиск в ротированном отсортированном массиве
**Условие:** Массив был отсортирован, потом повёрнут. Найди элемент за O(log n).

**Разбор:** Модифицированный бинарный поиск. Определяем какая половина отсортирована, сужаем поиск.

```python
def search_rotated(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        # Левая половина отсортирована
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Правая половина отсортирована
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

# Тест
print(search_rotated([4,5,6,7,0,1,2], 0))  # 4
print(search_rotated([4,5,6,7,0,1,2], 3))  # -1
```

---

### Задача 18: Merge Sort
**Условие:** Реализуй сортировку слиянием.

**Разбор:** Рекурсивно делим массив пополам, сортируем каждую часть, сливаем. O(n log n) время, O(n) память.

```python
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Тест
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))  # [3, 9, 10, 27, 38, 43, 82]
```

---

## Паттерн 7: Динамическое программирование (базовое)

### Когда применять
Задача имеет оптимальную подструктуру (решение = решения подзадач) и перекрывающиеся подзадачи.

### Задача 19: Числа Фибоначчи с мемоизацией
**Разбор:** Без мемоизации — O(2^n). С мемоизацией — O(n). Классический пример зачем нужно DP.

```python
from functools import lru_cache

# Рекурсия с мемоизацией
@lru_cache(maxsize=None)
def fib_memo(n: int) -> int:
    if n <= 1:
        return n
    return fib_memo(n - 1) + fib_memo(n - 2)

# Итеративно — O(n) время, O(1) память
def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(fib_dp(10))  # 55
```

---

### Задача 20: Подъём по лестнице (Climbing Stairs)
**Условие:** Лестница из n ступенек. За один шаг можно подняться на 1 или 2 ступеньки. Сколько способов добраться до вершины?

**Разбор:** dp[i] = dp[i-1] + dp[i-2]. Это Фибоначчи! dp[1]=1, dp[2]=2.

```python
def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    
    return curr

# Тест
print(climb_stairs(2))  # 2
print(climb_stairs(3))  # 3
print(climb_stairs(5))  # 8
```

---

### Задача 21: Максимальная сумма подмассива (Kadane's Algorithm)
**Условие:** Найди подмассив с максимальной суммой.

**Разбор:** dp[i] = максимальная сумма подмассива, заканчивающегося в i. dp[i] = max(nums[i], dp[i-1] + nums[i]). Если предыдущая сумма отрицательная — начинаем заново.

```python
def max_subarray(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Тест
print(max_subarray([-2,1,-3,4,-1,2,1,-5,4]))  # 6 (4,-1,2,1)
print(max_subarray([1]))                        # 1
print(max_subarray([5,4,-1,7,8]))              # 23
```

---

### Задача 22: Монеты (Coin Change)
**Условие:** Дан набор монет и сумма amount. Найди минимальное количество монет для набора суммы. Если невозможно — верни -1.

**Разбор:** dp[i] = минимум монет для суммы i. Для каждой суммы от 1 до amount перебираем все монеты.

```python
def coin_change(coins: list[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# Тест
print(coin_change([1, 5, 11], 15))  # 3 (5+5+5)
print(coin_change([2], 3))           # -1
print(coin_change([1, 2, 5], 11))   # 3 (5+5+1)
```

---

## Паттерн 8: Связный список

### Задача 23: Разворот связного списка
**Условие:** Разверни односвязный список.

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev
```

---

### Задача 24: Обнаружение цикла в связном списке
**Условие:** Определи, есть ли цикл в связном списке.

**Разбор:** Алгоритм Флойда — два указателя, медленный и быстрый. Если есть цикл — встретятся.

```python
def has_cycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False
```

---

### Задача 25: Середина связного списка
**Условие:** Найди середину связного списка. Если чётное количество — верни второй средний.

**Разбор:** Два указателя — медленный и быстрый. Когда быстрый дошёл до конца — медленный на середине.

```python
def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow
```

---

## Паттерн 9: Строки

### Задача 26: Палиндром
**Условие:** Определи, является ли строка палиндромом (игнорируй не-алфавитные символы, регистр).

```python
def is_palindrome(s: str) -> bool:
    cleaned = [c.lower() for c in s if c.isalnum()]
    return cleaned == cleaned[::-1]

# Two pointers версия — O(1) доп. память
def is_palindrome_v2(s: str) -> bool:
    left, right = 0, len(s) - 1
    
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome_v2("A man, a plan, a canal: Panama"))  # True
print(is_palindrome_v2("race a car"))                       # False
```

---

### Задача 27: Самая длинная общая подстрока (LCS)
**Условие:** Найди длину самой длинной общей подпоследовательности двух строк.

**Разбор:** DP. dp[i][j] = LCS для s1[:i] и s2[:j]. Если символы совпадают — dp[i][j] = dp[i-1][j-1] + 1, иначе max(dp[i-1][j], dp[i][j-1]).

```python
def longest_common_subsequence(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]

print(longest_common_subsequence("abcde", "ace"))   # 3
print(longest_common_subsequence("abc", "abc"))      # 3
print(longest_common_subsequence("abc", "def"))      # 0
```

---

## Паттерн 10: Сортировка и поиск

### Задача 28: K-й наибольший элемент
**Условие:** Найди k-й наибольший элемент в массиве.

**Разбор:** Можно sorted() за O(n log n). Оптимально — QuickSelect O(n) в среднем. Для собеса часто принимают heapq решение O(n log k).

```python
import heapq

def find_kth_largest(nums: list[int], k: int) -> int:
    # Min-heap размером k
    heap = nums[:k]
    heapq.heapify(heap)
    
    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    
    return heap[0]

# Тест
print(find_kth_largest([3,2,1,5,6,4], 2))   # 5
print(find_kth_largest([3,2,3,1,2,4,5,5,6], 4))  # 4
```

---

### Задача 29: Сортировка цветов (Dutch National Flag)
**Условие:** Дан массив из 0, 1, 2. Отсортируй на месте за O(n) и один проход.

**Разбор:** Три указателя — low, mid, high. 0 идут до low, 2 — после high, 1 — между.

```python
def sort_colors(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

# Тест
nums = [2, 0, 2, 1, 1, 0]
sort_colors(nums)
print(nums)  # [0, 0, 1, 1, 2, 2]
```

---

### Задача 30: Пересечение двух массивов
**Условие:** Найди пересечение двух массивов (уникальные общие элементы).

```python
def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))

# Тест
print(intersection([1,2,2,1], [2,2]))      # [2]
print(intersection([4,9,5], [9,4,9,8,4]))  # [9, 4]
```

---

# ЧАСТЬ 2 — ДОПОЛНИТЕЛЬНЫЕ РАЗБОРЫ

---

### Задача 31: Число островов (Number of Islands)
**Условие:** Дана матрица из '1' (земля) и '0' (вода). Найди количество островов.

**Разбор:** DFS/BFS от каждой непосещённой '1'. Помечаем посещённые клетки.

```python
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    
    count = 0
    
    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if grid[r][c] != '1':
            return
        grid[r][c] = '#'  # помечаем как посещённый
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                dfs(r, c)
                count += 1
    
    return count

grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
print(num_islands(grid))  # 3
```

---

### Задача 32: Топологическая сортировка (Kahn's Algorithm)
**Условие:** Дан список зависимостей курсов. Можно ли пройти все курсы? (Course Schedule)

**Разбор:** Строим граф зависимостей. Если есть цикл — нельзя. BFS от узлов без входящих рёбер (in-degree = 0).

```python
from collections import deque, defaultdict

def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    in_degree = [0] * num_courses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
    completed = 0
    
    while queue:
        course = queue.popleft()
        completed += 1
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    return completed == num_courses

print(can_finish(2, [[1,0]]))        # True
print(can_finish(2, [[1,0],[0,1]]))  # False (цикл)
```

---

### Задача 33: Максимальная глубина дерева
```python
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))
```

---

### Задача 34: Валидное BST
**Условие:** Определи, является ли бинарное дерево валидным BST.

**Разбор:** Рекурсивно передаём границы [min, max]. Каждый узел должен быть в своих границах.

```python
def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def validate(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (validate(node.left, min_val, node.val) and
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))
```

---

### Задача 35: Произведение кроме себя (Product of Array Except Self)
**Условие:** Для каждого элемента найди произведение всех остальных элементов. Без деления, O(n).

**Разбор:** Два прохода — префиксные произведения слева и справа.

```python
def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n
    
    # Префикс слева
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Суффикс справа
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

print(product_except_self([1,2,3,4]))   # [24,12,8,6]
print(product_except_self([-1,1,0,-3,3]))  # [0,0,9,0,0]
```

---

### Задача 36: Поворот матрицы на 90 градусов
**Условие:** Поверни матрицу N×N на 90 градусов по часовой стрелке, на месте.

**Разбор:** Транспонируем, потом разворачиваем каждую строку.

```python
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    
    # Транспонируем
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Разворачиваем строки
    for row in matrix:
        row.reverse()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print(matrix)  # [[7,4,1],[8,5,2],[9,6,3]]
```

---

### Задача 37: Спиральная матрица
**Условие:** Верни элементы матрицы в спиральном порядке.

```python
def spiral_order(matrix: list[list[int]]) -> list[int]:
    result = []
    top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
    
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1
        
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
    
    return result

print(spiral_order([[1,2,3],[4,5,6],[7,8,9]]))  # [1,2,3,6,9,8,7,4,5]
```

---

### Задача 38: Нули в матрице (Set Matrix Zeroes)
**Условие:** Если элемент = 0, обнули всю его строку и столбец. На месте, O(1) доп. память.

```python
def set_zeroes(matrix: list[list[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))
    
    # Используем первую строку/столбец как маркеры
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
```

---

### Задача 39: Счастливые числа (Happy Number)
**Условие:** Число счастливое если, заменяя его суммой квадратов цифр, в итоге приходим к 1. Определи является ли n счастливым.

**Разбор:** Цикл Floyd для обнаружения цикла (не приходит к 1).

```python
def is_happy(n: int) -> bool:
    def sum_squares(num):
        total = 0
        while num:
            num, digit = divmod(num, 10)
            total += digit ** 2
        return total
    
    slow, fast = n, sum_squares(n)
    
    while fast != 1 and slow != fast:
        slow = sum_squares(slow)
        fast = sum_squares(sum_squares(fast))
    
    return fast == 1

print(is_happy(19))  # True
print(is_happy(2))   # False
```

---

### Задача 40: Самый длинный палиндромный подстрок
**Условие:** Найди самую длинную палиндромную подстроку.

**Разбор:** Expand around center. Для каждой позиции расширяем в обе стороны. O(n²) время, O(1) память.

```python
def longest_palindrome(s: str) -> str:
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]
    
    result = ""
    for i in range(len(s)):
        # Нечётная длина
        odd = expand(i, i)
        # Чётная длина
        even = expand(i, i+1)
        
        if len(odd) > len(result):
            result = odd
        if len(even) > len(result):
            result = even
    
    return result

print(longest_palindrome("babad"))   # "bab" или "aba"
print(longest_palindrome("cbbd"))    # "bb"
```

---

### Задача 41: Три суммы (3Sum)
**Условие:** Найди все уникальные тройки в массиве, сумма которых равна 0.

**Разбор:** Сортируем. Фиксируем первый элемент, two pointers для остальных двух. Пропускаем дубликаты.

```python
def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # пропускаем дубликаты
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return result

print(three_sum([-1,0,1,2,-1,-4]))  # [[-1,-1,2],[-1,0,1]]
```

---

### Задача 42: Пересечение интервалов (Merge Intervals)
**Условие:** Дан список интервалов. Объедини все перекрывающиеся.

```python
def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    return merged

print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
```

---

### Задача 43: Поиск пика
**Условие:** Найди индекс любого пикового элемента (больше соседей). O(log n).

**Разбор:** Бинарный поиск. Если mid < mid+1 — пик справа. Иначе — слева или сам mid.

```python
def find_peak_element(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

print(find_peak_element([1,2,3,1]))    # 2
print(find_peak_element([1,2,1,3,5,6,4]))  # 5
```

---

### Задача 44: Уникальные пути (Unique Paths)
**Условие:** Робот в верхнем левом углу матрицы m×n. Может двигаться только вправо или вниз. Сколько уникальных путей до правого нижнего угла?

```python
def unique_paths(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]

print(unique_paths(3, 7))  # 28
print(unique_paths(3, 2))  # 3
```

---

### Задача 45: Сумма пути в дереве
**Условие:** Есть ли в дереве путь от корня до листа с суммой, равной target?

```python
def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target_sum
    
    remaining = target_sum - root.val
    return has_path_sum(root.left, remaining) or has_path_sum(root.right, remaining)
```

---

### Задача 46: Симметричное дерево
**Условие:** Является ли бинарное дерево зеркально симметричным?

```python
def is_symmetric(root: Optional[TreeNode]) -> bool:
    def is_mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))
    
    return is_mirror(root.left, root.right)
```

---

### Задача 47: Степень двойки
**Условие:** Определи, является ли n степенью двойки. O(1).

**Разбор:** Степень двойки в двоичном виде — ровно один бит. n & (n-1) обнуляет младший установленный бит. Если результат 0 — был ровно один бит.

```python
def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0

print(is_power_of_two(1))   # True (2^0)
print(is_power_of_two(16))  # True (2^4)
print(is_power_of_two(3))   # False
```

---

### Задача 48: Подсчёт битов (Counting Bits)
**Условие:** Для каждого числа от 0 до n верни количество единичных битов.

**Разбор:** dp[i] = dp[i >> 1] + (i & 1). Сдвиг вправо = делим на 2, последний бит = остаток.

```python
def count_bits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp

print(count_bits(5))  # [0,1,1,2,1,2]
```

---

### Задача 49: Слияние k отсортированных списков
**Условие:** Слей k отсортированных связных списков в один.

**Разбор:** Min-heap из первых элементов каждого списка. Извлекаем минимум, добавляем следующий элемент из того же списка.

```python
import heapq

def merge_k_lists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    dummy = ListNode(0)
    curr = dummy
    
    while heap:
        val, i, node = heapq.heappop(heap)
        curr.next = node
        curr = curr.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next
```

---

### Задача 50: LRU Cache
**Условие:** Реализуй LRU Cache с операциями get и put за O(1).

**Разбор:** OrderedDict (двусвязный список + хешмап). При get/put перемещаем элемент в конец (последний использованный). При переполнении удаляем первый (наименее используемый).

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # удаляем LRU

# Тест
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))    # 1
lru.put(3, 3)        # вытесняет ключ 2
print(lru.get(2))    # -1
```

---

---

# ЧАСТЬ 3 — 50 ЗАДАЧ БЕЗ РЕШЕНИЙ

Реши сам. Это твоя тренировка перед собесом.

---

### Two Pointers

1. Дан отсортированный массив. Удали дубликаты на месте. Верни новую длину.

2. Дан массив с нулями. Перемести все нули в конец, сохранив порядок остальных элементов. На месте.

3. Дана строка. Разверни только слова (не всю строку). `"the sky is blue"` → `"blue is sky the"`.

4. Даны два отсортированных массива. Слей их в один отсортированный на месте (первый массив имеет достаточно места в конце).

5. Дан массив из n+1 элементов, все элементы от 1 до n. Найди дубликат без изменения массива и без доп. памяти O(n).

---

### Sliding Window

6. Дана строка s и строка p. Найди все начальные индексы анаграмм p в s.

7. Дана строка s и строка t. Найди минимальное окно в s, содержащее все символы t.

8. Дан массив целых чисел и k. Найди максимальное среднее значение подмассива длины k.

9. Дана бинарная строка. Можно заменить не более k нулей на единицы. Найди длину самой длинной последовательности единиц.

10. Дан массив фруктов (каждый тип — число). Можно собирать фрукты только двух типов подряд. Найди максимальное количество фруктов.

---

### HashMap / HashSet

11. Дан массив. Найди все пары элементов с разностью равной k.

12. Дан массив строк. Сгруппируй все строки, которые принадлежат одной и той же последовательности сдвигов. `"az"` и `"ba"` — одна группа.

13. Дан массив. Найди длину самой длинной последовательности подряд идущих чисел (числа в массиве не отсортированы). O(n).

14. Даны два массива. Найди их пересечение с учётом дубликатов (если элемент встречается 2 раза в обоих — включить 2 раза).

15. Дана строка. Найди количество подстрок, являющихся палиндромами, за O(n).

---

### Стек

16. Дана строка со скобками и числами, типа `"3[a]2[bc]"`. Декодируй её → `"aaabcbc"`.

17. Дан массив температур. Для каждого дня найди через сколько дней будет более тёплый день. Если такого дня нет — 0.

18. Реализуй очередь используя только два стека.

19. Дан массив. Найди максимальную площадь прямоугольника в гистограмме.

20. Дана строка с операциями над счётом: число (прибавить), `"+"` (сумма двух предыдущих), `"D"` (удвоить последнее), `"C"` (удалить последнее). Верни итоговую сумму.

---

### BFS / DFS

21. Дана матрица. Найди количество компонент связности (групп единиц, соединённых по горизонтали/вертикали).

22. Дан граф (список смежности). Определи, является ли он двудольным (bipartite).

23. Дано дерево. Найди диаметр — длину наидлиннейшего пути между двумя узлами.

24. Дана матрица с гнилыми апельсинами (2), свежими (1) и пустыми клетками (0). Гниль распространяется по 4 направлениям за 1 минуту. Найди минимальное время пока все апельсины не сгниют. Если невозможно — -1.

25. Дан список пар слов (начало → конец трансформации, меняем одну букву за раз). Найди кратчайшую цепочку трансформаций от beginWord до endWord.

---

### Бинарный поиск

26. Найди первую и последнюю позицию элемента в отсортированном массиве. O(log n).

27. Дана функция `isBadVersion(n)`. Найди первую плохую версию среди 1..n. O(log n).

28. Дана матрица n×m, строки и столбцы отсортированы. Найди элемент за O(n+m).

29. Найди квадратный корень числа x (целая часть). Без `math.sqrt`. O(log n).

30. Дан массив отсортированный и повёрнутый, с возможными дубликатами. Найди минимальный элемент.

---

### Динамическое программирование

31. Дана строка. Найди длину самой длинной возрастающей подпоследовательности (LIS).

32. Даны две строки. Найди минимальное количество операций (вставка, удаление, замена) для преобразования одной строки в другую (Edit Distance).

33. Дан рюкзак ёмкостью W и предметы с весами и ценностями. Максимизируй ценность (0/1 knapsack).

34. Дана сетка с ценами клеток. Найди минимальную стоимость пути из верхнего левого в нижний правый угол (движение только вправо/вниз).

35. Дан массив. Найди количество подмассивов с суммой равной k.

---

### Деревья

36. Найди наименьшего общего предка (LCA) двух узлов в бинарном дереве.

37. Сериализуй и десериализуй бинарное дерево (преобразуй в строку и обратно).

38. Дано BST и два узла. Найди их LCA.

39. Переведи BST в отсортированный двусвязный список на месте.

40. Дано дерево. Найди все пути от корня до листьев с суммой равной target.

---

### Связные списки

41. Разверни связный список от позиции left до right на месте.

42. Найди узел, с которого начинается цикл в связном списке.

43. Дан связный список. Определи, является ли он палиндромом. O(n) время, O(1) память.

44. Разбей связный список так, чтобы все узлы меньше x шли перед узлами >= x, сохранив относительный порядок.

45. Даны два связных списка. Найди узел их пересечения (если есть).

---

### Разное

46. Дан массив интервалов встреч. Найди минимальное количество переговорных комнат.

47. Реализуй `myAtoi(string)` — аналог `int()` с обработкой пробелов, знака, переполнения.

48. Дана строка. Найди длину последнего слова.

49. Дан массив из n целых чисел. Найди все уникальные четвёрки, сумма которых равна target.

50. Реализуй итератор для плоского вложенного списка. `NestedIterator([[1,1],2,[1,1]])` → `[1,1,2,1,1]`.

---
