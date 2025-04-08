FROM node:20

# Cài đặt các gói cần thiết
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    fonts-liberation \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

# Tạo thư mục và tải Chrome for Testing
WORKDIR /opt

RUN wget https://storage.googleapis.com/chrome-for-testing-public/135.0.7049.42/linux64/chrome-linux64.zip && \
    unzip chrome-linux64.zip && \
    mv chrome-linux64 chrome && \
    ln -s /opt/chrome/chrome /usr/bin/google-chrome && \
    rm chrome-linux64.zip

# Thiết lập biến môi trường để sử dụng Puppeteer với Chrome đã tải
ENV PUPPETEER_EXECUTABLE_PATH=/opt/chrome/chrome

# Copy source code
WORKDIR /app
COPY . .

# Cài đặt npm và khởi động app
RUN npm install

CMD ["npm", "start"]
