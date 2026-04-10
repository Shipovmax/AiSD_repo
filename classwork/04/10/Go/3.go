// Реализовать декоратор с именем print_type, выводящий
// на печать тип значения, возвращаемого декорируемой функцией.

package main

import "fmt"

// Типы функций для примеров: одна возвращает int, другая string.
type task3IntFunc func(int, int) int
type task3StringFunc func(string) string

// Обертка для функции, которая возвращает int.
func printTypeInt(fn task3IntFunc) task3IntFunc {
	return func(a int, b int) int {
		// Получаем результат функции.
		result := fn(a, b)
		// Печатаем тип результата.
		fmt.Printf("Type: %T\n", result)
		return result
	}
}

// Обертка для функции, которая возвращает string.
func printTypeString(fn task3StringFunc) task3StringFunc {
	return func(name string) string {
		// Получаем результат функции.
		result := fn(name)
		// Печатаем тип результата.
		fmt.Printf("Type: %T\n", result)
		return result
	}
}

// Обычная функция сложения.
func task3Add(a int, b int) int {
	return a + b
}

// Обычная функция приветствия.
func task3Greet(name string) string {
	return "Hello " + name
}

// Тут запускаем третье задание.
func runTask3() {
	printTypeInt(task3Add)(2, 3)
	printTypeString(task3Greet)("Max")
}

// main нужен, чтобы можно было запустить файл через go run 3.go.
func main() {
	runTask3()
}
