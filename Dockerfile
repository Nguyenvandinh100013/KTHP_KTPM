FROM python:3.11-slim

# Cài các thư viện hệ thống cần thiết
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
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
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Cài đặt Google Chrome phiên bản 134.0.6998.179 (tương thích với ChromeDriver 134.0.0.0)
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y ./google-chrome-stable_current_amd64.deb && \
    rm google-chrome-stable_current_amd64.deb

# Cài ChromeDriver tương ứng với Chrome v134
RUN DRIVER_VERSION=134.0.0.0 && \
    wget -O /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${DRIVER_VERSION}/chromedriver_linux64.zip" && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm /tmp/chromedriver.zip

# Cài thư viện Python
RUN pip install --upgrade pip && \
    pip install selenium pytest html-testRunner

# Biến môi trường cho Chrome
ENV CHROME_BIN=/usr/bin/google-chrome
ENV PATH=$PATH:/usr/local/bin

# Copy source code vào container
COPY ./web /app
WORKDIR /app
RUN ls -R /app

# Mặc định chạy pytest
CMD ["pytest", "/app/tests"]
