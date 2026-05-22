package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
	"regexp"
	"strings"
	"time"
)

// Структура для итогового JSON
type Result struct {
	ID    string `json:"id"`
	Price string `json:"price"`
}

// Структура ответа Wildberries
type WBData struct {
	Data struct {
		Products []struct {
			ID         int    `json:"id"`
			SalePriceU int    `json:"salePriceU"` // Цена в копейках
			Name       string `json:"name"`
		} `json:"products"`
	} `json:"data"`
}

func fetchPrice(productID string) string {
	// dest — это код региона (Москва). Можно менять для разных цен.
	url := fmt.Sprintf("https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&nm=%s", productID)

	client := &http.Client{
		Timeout: 5 * time.Second,
	}

	req, _ := http.NewRequest("GET", url, nil)
	
	// Заголовки, чтобы WB не блокировал запрос
	req.Header.Set("User-Agent", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")
	req.Header.Set("Accept", "*/*")
	req.Header.Set("Origin", "https://www.wildberries.ru")

	resp, err := client.Do(req)
	if err != nil {
		return "Ошибка запроса"
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)

	var data WBData
	if err := json.Unmarshal(body, &data); err != nil {
		return "Ошибка данных"
	}

	if len(data.Data.Products) > 0 {
		// Делим на 100, так как цена приходит без разделителя (например, 150000 вместо 1500.00)
		finalPrice := data.Data.Products[0].SalePriceU / 100
		return fmt.Sprintf("%d", finalPrice)
	}

	return "Не найдено"
}

func main() {
	// Читаем входной файл
	inputPath := "test.txt" // Или запроси через fmt.Scanln
	data, err := os.ReadFile(inputPath)
	if err != nil {
		fmt.Println("Ошибка: не удалось найти файл test.txt")
		return
	}

	// Ищем ID в ссылках
	re := regexp.MustCompile(`catalog/(\d+)/`)
	lines := strings.Split(string(data), "\n")
	
	var results []Result

	fmt.Println("Запуск парсинга...")

	for _, line := range lines {
		line = strings.TrimSpace(line)
		if line == "" {
			continue
		}

		match := re.FindStringSubmatch(line)
		if len(match) > 1 {
			id := match[1]
			price := fetchPrice(id)
			
			results = append(results, Result{
				ID:    id,
				Price: price,
			})
			
			fmt.Printf("Обработано: %s | Цена: %s\n", id, price)
			// Небольшая задержка, чтобы не поймать капчу (хотя API лояльно)
			time.Sleep(150 * time.Millisecond)
		}
	}

	// Сохраняем в result.json
	file, _ := json.MarshalIndent(results, "", "  ")
	_ = os.WriteFile("result.json", file, 0644)

	fmt.Println("\nГотово! Результаты в result.json")
}