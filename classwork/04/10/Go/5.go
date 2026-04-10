// С помощью декоратора реализовать отладочный вывод работы
// factorial(n) как для вызовов функций, так и для возвращаемых значений.

package main

import "fmt"

type task5Func func(int) int

func debugFactorial(fn task5Func) task5Func {
	return func(n int) int {
		fmt.Println("Call: factorial", n)
		result := fn(n)
		fmt.Println("Return:", result)
		return result
	}
}

func runTask5() {
	var factorial task5Func

	factorial = debugFactorial(func(n int) int {
		if n == 0 || n == 1 {
			return 1
		}

		return n * factorial(n-1)
	})

	fmt.Println(factorial(5))
}
