// Реализовать декоратор с именем not_none, который генерирует
// исключительную ситуацию если декорируемая функция вернула значения None.

package main

import "fmt"

type task2Func func(int, int) *int

func notNone(fn task2Func) task2Func {
	return func(a int, b int) *int {
		result := fn(a, b)

		if result == nil {
			panic("AttributeError")
		}

		return result
	}
}

func task2Add(a int, b int) *int {
	c := a + b
	_ = c
	return nil
}

func runTask2() {
	defer func() {
		if recover() != nil {
			fmt.Println("AttributeError")
		}
	}()

	notNone(task2Add)(1, 2)
}
