// Реализовать декоратор с именем print_type, выводящий
// на печать тип значения, возвращаемого декорируемой функцией.

package main

import "fmt"

type task3IntFunc func(int, int) int
type task3StringFunc func(string) string

func printTypeInt(fn task3IntFunc) task3IntFunc {
	return func(a int, b int) int {
		result := fn(a, b)
		fmt.Printf("Type: %T\n", result)
		return result
	}
}

func printTypeString(fn task3StringFunc) task3StringFunc {
	return func(name string) string {
		result := fn(name)
		fmt.Printf("Type: %T\n", result)
		return result
	}
}

func task3Add(a int, b int) int {
	return a + b
}

func task3Greet(name string) string {
	return "Hello " + name
}

func runTask3() {
	printTypeInt(task3Add)(2, 3)
	printTypeString(task3Greet)("Max")
}
