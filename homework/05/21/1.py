import json
import re
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def extract_product_id(url):
    match = re.search(r"catalog/(\d+)/", url)
    return match.group(1) if match else None


def parse_wb_price(url):
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1440, 900)

    driver.execute_cdp_cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        {
            "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        },
    )

    price_text = None
    try:
        driver.get(url)

        selectors = [
            "h3.mo-typography.mo-typography_variant_title3.mo-typography_variable-weight_title3.mo-typography_variable.mo-typography_color_danger",
            'h3[class*="mo-typography"][class*="color_danger"]',
            "ins.price-block__final-price",
            ".price-block__final-price",
            'span[class*="priceBlockPrice"]',
        ]

        element = None
        for selector in selectors:
            try:
                element = WebDriverWait(driver, 4).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                )
                if element:
                    break
            except Exception:
                continue

        if not element:
            time.sleep(2)
            for selector in selectors:
                elements = driver.find_elements(By.CSS_SELECTOR, selector)
                if elements:
                    element = elements[0]
                    break

        if element:
            raw_text = element.get_attribute("textContent")
            if raw_text:
                if "₽" in raw_text:
                    raw_text = raw_text.split("₽")[0]

                digits = re.findall(r"\d+", raw_text)
                if digits:
                    price_text = "".join(digits)
    except Exception:
        pass
    finally:
        driver.quit()

    return price_text


def main():
    input_path = input("Введите путь к файлу .txt со ссылками: ").strip()
    output_path = "result.json"

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            urls = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Файл не найден. Проверьте путь.")
        return

    results = []

    for url in urls:
        product_id = extract_product_id(url)
        if product_id:
            price = parse_wb_price(url)
            results.append({"id": product_id, "price": price or "Не найдено"})
            time.sleep(1)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(
        f"Готово! Обработано ссылок: {len(results)}. Результат сохранен в {output_path}"
    )


if __name__ == "__main__":
    main()

