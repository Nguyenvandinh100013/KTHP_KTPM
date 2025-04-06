# Sử dụng image chính thức của Python 3.11
FROM python:3.11-slim

# Cài đặt các phụ thuộc cần thiết cho Chrome và Selenium
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libxss1 \
    libgconf-2-4 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    fonts-liberation \
    libappindicator3-1 \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Cài đặt Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb || apt-get -fy install

# Cài đặt Selenium và WebDriver
RUN pip install selenium pytest

# Đặt biến môi trường để chỉ định đường dẫn tới Chrome
ENV CHROME_BIN=/usr/bin/google-chrome-stable

# Cài đặt ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver

# Copy mã nguồn vào container (nếu cần thiết)
COPY ./web/* /app/

# Thiết lập thư mục làm việc
WORKDIR /app
RUN ls -R /app
# Chạy một test mẫu khi container khởi động (tùy chọn)
CMD ["pytest", "tests"]