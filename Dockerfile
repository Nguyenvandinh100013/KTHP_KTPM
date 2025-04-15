FROM python:3.11

# Cài đặt thư viện hệ thống
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    python3 \
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
RUN python3 install HtmlTestRunner

# Đặt biến môi trường để chỉ định đường dẫn tới Chrome
ENV CHROME_BIN=/usr/bin/google-chrome-stable

# Cài đặt ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/113.0.5672.63/chromedriver_linux64.zip
RUN unzip chromedriver_linux64.zip
RUN mv chromedriver /usr/local/bin/
RUN chmod +x /usr/local/bin/chromedriver

# Copy mã nguồn vào container (nếu cần thiết)
COPY ./web /app/

# Thiết lập thư mục làm việc
WORKDIR /app
RUN ls -R /app
# Chạy một test mẫu khi container khởi động (tùy chọn)
CMD ["pytest", "/app/tests"]
=======
    gnupg \
    ca-certificates \
    fonts-liberation \
    libatk-bridge2.0-0 \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    libatk1.0-0 \
    libcups2 \
    libgdk-pixbuf2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    xdg-utils \
    libgbm1 \
    libvulkan1 \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Cài đặt Google Chrome (v134)
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Cài đặt ChromeDriver tương ứng với Chrome v134
RUN CHROMEDRIVER_VERSION=134.0.6351.2 && \
    wget -O /tmp/chromedriver.zip "https://storage.googleapis.com/chrome-for-testing-public/${CHROMEDRIVER_VERSION}/linux64/chromedriver-linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /tmp/ && \
    mv /tmp/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver*

# Biến môi trường
ENV CHROME_BIN=/usr/bin/google-chrome
ENV PATH=$PATH:/usr/local/bin

# Cài thư viện Python
RUN pip install --upgrade pip && \
    pip install selenium pytest html-testRunner

# Copy mã nguồn
COPY ./web /app
WORKDIR /app

# Chạy test
CMD ["pytest", "/app/tests"]