FROM ubuntu:latest

# Ccài đặt các công cụ cần thiết
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    openjdk-21-jdk \
    python3 \
    python3-pip \
    python3-venv \
    nodejs npm \
    && apt-get clean

# Cài đặt Android SDK và di chuyển các tệp vào thư mục latest
RUN mkdir -p /opt/android-sdk/cmdline-tools && \
    curl -o android-sdk.zip https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip && \
    unzip android-sdk.zip -d /opt/android-sdk/cmdline-tools && \
    rm android-sdk.zip && \
    mkdir -p /opt/android-sdk/cmdline-tools/latest && \
    mv /opt/android-sdk/cmdline-tools/cmdline-tools/* /opt/android-sdk/cmdline-tools/latest/ && \
    rm -rf /opt/android-sdk/cmdline-tools/cmdline-tools

# Thiết lập biến môi trường cho Android SDK
ENV ANDROID_HOME=/opt/android-sdk
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV PATH="${PATH}:${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools:${ANDROID_HOME}/tools"

# Cài đặt các công cụ SDK cần thiết (ví dụ: build-tools, platform-tools)
RUN yes | /opt/android-sdk/cmdline-tools/latest/bin/sdkmanager --sdk_root=$ANDROID_SDK_ROOT --licenses && \
    /opt/android-sdk/cmdline-tools/latest/bin/sdkmanager --sdk_root=$ANDROID_SDK_ROOT "platform-tools" "platforms;android-13" "build-tools;30.0.3"

# Tạo môi trường Python ảo và cài đặt các thư viện cần thiết cho Robot Framework
RUN python3 -m venv /opt/robot-env && \
    /opt/robot-env/bin/pip install --upgrade pip && \
    /opt/robot-env/bin/pip install robotframework robotframework-appiumlibrary onetimepass pyperclip

# Cài đặt Appium và driver UiAutomator2
RUN npm install -g appium@latest && \
    appium driver install uiautomator2

# Chuyển vào thư mục làm việc
WORKDIR /app
COPY ./bfxqa-robotframework /app

# Expose cổng cần thiết cho Appium
EXPOSE 4723
# Copy entrypoint script vào container
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Lệnh CMD để chạy script
CMD ["/entrypoint.sh"]