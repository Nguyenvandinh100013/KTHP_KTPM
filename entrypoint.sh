#!/bin/bash

# Chạy Appium
appium --address 0.0.0.0 --port 4723 --log-level info &

# Đợi Appium khởi động
until curl -s http://localhost:4723 | grep -q '"status": 0'; do
    echo "Waiting for Appium server to start..."
    sleep 5
done

# Kết nối với Android container qua adb
echo "Connecting to Android container..."
adb connect android-container:5555
adb devices

# Chạy test với pytest
pytest /app/tests/ --html=/report/test_report.html --self-contained-html
