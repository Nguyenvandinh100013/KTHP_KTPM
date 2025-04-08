FROM python:3.11-slim

# Cài thư viện hệ thống
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    unzip \
    gnupg \
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

# Cài Chrome phiên bản ổn định (114.0.5735.90)
RUN wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_114.0.5735.90-1_amd64.deb && \
    dpkg -i google-chrome-stable_114.0.5735.90-1_amd64.deb || apt-get -fy install && \
    rm google-chrome-stable_114.0.5735.90-1_amd64.deb

# Cài ChromeDriver tương ứng
RUN wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/ && \
    chmod +x /usr/local/bin/chromedriver && \
    rm chromedriver_linux64.zip

# Cài pip packages
RUN pip install --upgrade pip && \
    pip install selenium pytest html-testRunner

# Đặt biến môi trường
ENV CHROME_BIN=/usr/bin/google-chrome
ENV PATH=$PATH:/usr/local/bin

# Copy mã nguồn
COPY ./web /app
WORKDIR /app
RUN ls -R /app

CMD ["pytest", "/app/tests"]
