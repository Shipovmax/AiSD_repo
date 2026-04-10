// С помощью декоратора реализовать отладочный вывод работы
// factorial(n) как для вызовов функций, так и для возвращаемых значений.

package main

import "fmt"

// Тип функции factorial: принимает n и возвращает число.
type task5Func func(int) int

// Обертка печатает вызов factorial и его результат.
func debugFactorial(fn task5Func) task5Func {
	return func(n int) int {
		// Печатаем вход в функцию.
		fmt.Println("Call: factorial", n)
		// Вызываем исходную функцию.
		result := fn(n)
		// Печатаем выход из функции.
		fmt.Println("Return:", result)
		return result
	}
}

// Тут запускаем пятое задание.
func runTask5() {
	// Сначала объявляем переменную, чтобы factorial мог вызывать сам себя.
	var factorial task5Func

	// Тут создаем factorial и сразу оборачиваем его в debugFactorial.
	factorial = debugFactorial(func(n int) int {
		// База рекурсии: 0! и 1! равны 1.
		if n == 0 || n == 1 {
			return 1
		}

		// Рекурсивный шаг: n! = n * (n - 1)!.
		return n * factorial(n-1)
	})

	fmt.Println(factorial(5))
}

// main нужен, чтобы можно было запустить файл через go run 5.go.
func main() {
	runTask5()
}
