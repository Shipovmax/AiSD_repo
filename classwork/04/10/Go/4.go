// Реализовать декоратор с именем not_sum, который генерирует
// исключительную ситуацию, если декорируемая функция вернула
// отрицательное значение суммы трех чисел.

package main

import "fmt"

// Тип функции, которая принимает три числа и возвращает сумму.
type task4Func func(int, int, int) int

// Обертка проверяет, что сумма не отрицательная.
func notSum(fn task4Func) task4Func {
	return func(a int, b int, c int) int {
		// Сначала считаем сумму через исходную функцию.
		result := fn(a, b, c)

		// Если сумма меньше нуля, кидаем ошибку через panic.
		if result < 0 {
			panic("ValueError")
		}

		// Если все нормально, возвращаем сумму.
		return result
	}
}

// Обычная функция суммы трех чисел.
func sumThree(a int, b int, c int) int {
	return a + b + c
}

// Тут запускаем четвертое задание.
func runTask4() {
	// recover ловит panic и дает красиво напечатать ValueError.
	defer func() {
		if recover() != nil {
			fmt.Println("ValueError")
		}
	}()

	fmt.Println(notSum(sumThree)(1, 2, -10))
}

// main нужен, чтобы можно было запустить файл через go run 4.go.
func main() {
	runTask4()
}
