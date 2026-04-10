// Реализовать декоратор с именем not_sum, который генерирует
// исключительную ситуацию, если декорируемая функция вернула
// отрицательное значение суммы трех чисел.

package main

import "fmt"

type task4Func func(int, int, int) int

func notSum(fn task4Func) task4Func {
	return func(a int, b int, c int) int {
		result := fn(a, b, c)

		if result < 0 {
			panic("ValueError")
		}

		return result
	}
}

func sumThree(a int, b int, c int) int {
	return a + b + c
}

func runTask4() {
	defer func() {
		if recover() != nil {
			fmt.Println("ValueError")
		}
	}()

	fmt.Println(notSum(sumThree)(1, 2, -10))
}
