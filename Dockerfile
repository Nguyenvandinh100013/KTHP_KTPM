FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    openjdk-21-jdk \
    python3 \
    python3-pip \
    python3-venv \
    nodejs \
    npm \
    git \
    adb \
    && apt-get clean

RUN mkdir -p /opt/android-sdk/cmdline-tools && \
    curl -o android-sdk.zip https://dl.google.com/android/repository/commandlinetools-linux-8512546_latest.zip && \
    unzip android-sdk.zip -d /opt/android-sdk/cmdline-tools && \
    rm android-sdk.zip && \
    mkdir -p /opt/android-sdk/cmdline-tools/latest && \
    mv /opt/android-sdk/cmdline-tools/cmdline-tools/* /opt/android-sdk/cmdline-tools/latest/ && \
    rm -rf /opt/android-sdk/cmdline-tools/cmdline-tools

ENV ANDROID_HOME=/opt/android-sdk
ENV ANDROID_SDK_ROOT=/opt/android-sdk
ENV PATH="${PATH}:${ANDROID_HOME}/cmdline-tools/latest/bin:${ANDROID_HOME}/platform-tools"

RUN yes | sdkmanager --sdk_root=$ANDROID_SDK_ROOT --licenses && \
    sdkmanager --sdk_root=$ANDROID_SDK_ROOT "platform-tools" "platforms;android-34" "build-tools;34.0.0"

RUN npm install -g appium@latest && \
    appium driver install uiautomator2

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install Appium-Python-Client selenium pytest pytest-html

ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app
COPY ./mobile /app

EXPOSE 4723

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]
