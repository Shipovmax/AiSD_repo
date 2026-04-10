// Реализовать декоратор с именем not_none, который генерирует
// исключительную ситуацию если декорируемая функция вернула значения None.

package main

import "fmt"

// В Go нет None, поэтому используем nil-указатель.
type task2Func func(int, int) *int

// Это обертка: она проверяет, что функция не вернула nil.
func notNone(fn task2Func) task2Func {
	return func(a int, b int) *int {
		// Вызываем исходную функцию.
		result := fn(a, b)

		// Если вернулся nil, это как None в Python.
		if result == nil {
			panic("AttributeError")
		}

		// Если nil нет, возвращаем результат.
		return result
	}
}

// Функция специально возвращает nil, чтобы проверить ошибку.
func task2Add(a int, b int) *int {
	c := a + b
	// Так Go не ругается, что c посчитали и не использовали.
	_ = c
	return nil
}

// Тут запускаем второе задание.
func runTask2() {
	// recover ловит panic, чтобы программа не падала с длинной ошибкой.
	defer func() {
		if recover() != nil {
			fmt.Println("AttributeError")
		}
	}()

	notNone(task2Add)(1, 2)
}

// main нужен, чтобы можно было запустить файл через go run 2.go.
func main() {
	runTask2()
}
