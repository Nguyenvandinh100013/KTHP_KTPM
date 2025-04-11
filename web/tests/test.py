from concurrent.futures import ThreadPoolExecutor, TimeoutError
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def my_keyword(driver):
    # Đây là keyword bạn muốn chạy
    driver.get("https://example.com")
    element = driver.find_element("id", "some-id")  # Ví dụ
    return "success"

def run_with_timeout(driver, timeout=10):
    with ThreadPoolExecutor(max_workers=1) as executor:
        future = executor.submit(my_keyword, driver)
        try:
            result = future.result(timeout=timeout)
            return {"status": "success", "detail": result}
        except TimeoutError:
            return {"status": "timeout"}
        except Exception as e:
            return {"status": "error", "detail": str(e)}

# Khởi tạo driver và test
driver = webdriver.Chrome()
status = run_with_timeout(driver, timeout=5)
print(status)
driver.quit()
