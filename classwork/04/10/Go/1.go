// Реализовать декоратор, который выводит на печать возвращаемые значения функции.

package main

import "fmt"

type task1IntFunc func(int, int) int
type task1StringFunc func(string) string

func printReturnInt(fn task1IntFunc) task1IntFunc {
	return func(a int, b int) int {
		result := fn(a, b)
		fmt.Println("Return:", result)
		return result
	}
}

func printReturnString(fn task1StringFunc) task1StringFunc {
	return func(name string) string {
		result := fn(name)
		fmt.Println("Return:", result)
		return result
	}
}

func task1Add(a int, b int) int {
	return a + b
}

func task1Greet(name string) string {
	return "Hello " + name
}

func runTask1() {
	printReturnInt(task1Add)(2, 3)
	printReturnString(task1Greet)("Max")
}

func main() {
	runTask1()
	runTask2()
	runTask3()
	runTask4()
	runTask5()
}
