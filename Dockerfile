FROM ubuntu:latest

# Cài đặt các công cụ cơ bản
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    openjdk-21-jdk \
    python3 \
    python3-pip \
    nodejs \
    npm \
    git \
    && apt-get clean

# Cài Android SDK command line tools
RUN mkdir -p /opt/android-sdk/cmdline-tools && \
    curl -o android-sdk.zip https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip && \
    unzip android-sdk.zip -d /opt/android-sdk/cmdline-tools && \
    rm android-sdk.zip && \
    mkdir -p /opt/android-sdk/cmdline-tools/latest && \
    mv /opt/android-sdk/cmdline-tools/cmdline-tools/* /opt/android-sdk/cmdline-tools/latest/ && \
    rm -rf /opt/android-sdk/cmdline-tools/cmdline-tools

# Thiết lập biến môi trường Android
ENV ANDROID_HOME=/opt/android-sdk
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV PATH="${PATH}:${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools"

# Cài platform-tools và build-tools cần thiết
RUN yes | sdkmanager --sdk_root=$ANDROID_SDK_ROOT --licenses && \
    sdkmanager --sdk_root=$ANDROID_SDK_ROOT "platform-tools" "platforms;android-34" "build-tools;34.0.0"

# Cài đặt Appium và driver
RUN npm install -g appium@latest && \
    appium driver install uiautomator2

# Cài đặt Appium Python client và các thư viện cần thiết
RUN pip3 install --upgrade pip && \
    pip3 install Appium-Python-Client selenium pytest pytest-html

# Thiết lập thư mục làm việc
WORKDIR /app
COPY ./mobile /app

# Mở cổng Appium server
EXPOSE 4723

# Copy script chạy hoặc test
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Lệnh chạy mặc định
CMD ["/entrypoint.sh"]
