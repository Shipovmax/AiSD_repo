// Реализовать декоратор, который выводит на печать возвращаемые значения функции.

package main

import "fmt"

// Это тип функции: принимает два int, возвращает int.
type task1IntFunc func(int, int) int

// Это тип функции: принимает string, возвращает string.
type task1StringFunc func(string) string

// Это обертка для функции с числами.
func printReturnInt(fn task1IntFunc) task1IntFunc {
	return func(a int, b int) int {
		// Сначала вызываем исходную функцию.
		result := fn(a, b)
		// Потом печатаем ее результат.
		fmt.Println("Return:", result)
		// И возвращаем результат дальше.
		return result
	}
}

// Это обертка для функции со строкой.
func printReturnString(fn task1StringFunc) task1StringFunc {
	return func(name string) string {
		// Вызываем исходную функцию.
		result := fn(name)
		// Печатаем то, что она вернула.
		fmt.Println("Return:", result)
		return result
	}
}

// Обычная функция сложения.
func task1Add(a int, b int) int {
	return a + b
}

// Обычная функция приветствия.
func task1Greet(name string) string {
	return "Hello " + name
}

// Тут запускаем первое задание.
func runTask1() {
	printReturnInt(task1Add)(2, 3)
	printReturnString(task1Greet)("Max")
}

// main нужен, чтобы можно было запустить файл через go run 1.go.
func main() {
	runTask1()
}
