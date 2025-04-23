#!/bin/bash

# Chạy Appium
appium &

# Kết nối với Android container qua adb
echo "Connecting to Android container..."
adb connect android-container:5555
adb devices
sleep 80
# Chạy test với pytest
pytest /app/tests/ --html=/report/test_report.html --self-contained-html
