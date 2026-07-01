package main_test

func convert(s string, numRows int) string {
	if numRows == 1 || numRows >= len(s) {
		return s
	}

	// Заранее выделяем память под весь результат.
	// Емкость равна длине строки — ровно 1 аллокация за всю функцию.
	res := make([]byte, 0, len(s))
	cycle := 2*numRows - 2

	for i := 0; i < numRows; i++ {
		for j := i; j < len(s); j += cycle {
			// Добавляем символ из основного вертикального столбца
			res = append(res, s[j])

			// Высчитываем индекс для промежуточного символа в диагонали
			mid := j + cycle - 2*i

			// Если это не первая и не последняя строка, и индекс валиден — добавляем
			if i > 0 && i < numRows-1 && mid < len(s) {
				res = append(res, s[mid])
			}
		}
	}

	// Конвертируем итоговый байтовый срез в строку (еще 1 аллокация)
	return string(res)
}
