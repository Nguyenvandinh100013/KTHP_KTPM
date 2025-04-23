from concurrent.futures import ThreadPoolExecutor, TimeoutError
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException

def my_keyword(driver):
    driver.get("https://example.com")
    element = driver.find_element("id", "some-id") 
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

driver = webdriver.Chrome()
status = run_with_timeout(driver, timeout=5)
print(status)
driver.quit()


# ///////////////////////////////////////////////////////////////////////
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import os
from openpyxl import Workbook

# Đường dẫn đến ChromeDriver
driver_path = "C:/webdrivers/chromedriver.exe"
service = Service(driver_path)


# Hàm kiểm thử từng test case
def run_test_case(driver, username, password, screenshot_folder, test_case_name):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    # Điền username
    driver.find_element(By.ID, "username").send_keys(username)

    # Điền password
    driver.find_element(By.ID, "password").send_keys(password)

    # Click Submit
    driver.find_element(By.ID, "submit").click()
    time.sleep(3)

    # Chụp ảnh màn hình sau khi submit
    screenshot_path = os.path.join(screenshot_folder, f"{test_case_name}.png")
    driver.save_screenshot(screenshot_path)

    # Kiểm tra kết quả
    try:
        # Trường hợp đăng nhập thành công
        if "logged-in-successfully" in driver.current_url:
            return "Logged in successfully"
        # Trường hợp lỗi
        else:
            error_message = driver.find_element(By.ID, "error").text
            return error_message
    except:
        return "Unknown error"


# Đọc dữ liệu từ file Excel
data = pd.read_excel("D:/test_data.xlsx")

# Khởi tạo WebDriver
driver = webdriver.Chrome(service=service)

# Tạo thư mục lưu ảnh chụp màn hình
screenshot_folder = "D:/screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

# Tạo danh sách lưu kết quả
results = []

# Chạy từng test case
for index, row in data.iterrows():
    test_case_name = row["Test Case"].replace(" ", "_")
    username = row["Username"]
    password = row["Password"]
    expected_result = row["Expected Result"]

    print(f"Running test case: {row['Test Case']}")

    # Thực thi kiểm thử
    actual_result = run_test_case(driver, username, password, screenshot_folder, test_case_name)

    # So sánh kết quả thực tế và mong đợi
    status = "Passed" if actual_result == expected_result else "Failed"

    # Lưu kết quả
    results.append({
        "Test Case": row["Test Case"],
        "Username": username,
        "Password": password,
        "Expected Result": expected_result,
        "Actual Result": actual_result,
        "Status": status
    })

# Đóng trình duyệt
driver.quit()

# Xuất kết quả ra file Excel
output_file = "D:/test_report_with_screenshots.xlsx"
report_df = pd.DataFrame(results)
report_df.to_excel(output_file, index=False)
print(f"Test report has been saved to {output_file}")

# Thông báo đường dẫn lưu ảnh chụp
print(f"Screenshots have been saved to the folder: {screenshot_folder}")
