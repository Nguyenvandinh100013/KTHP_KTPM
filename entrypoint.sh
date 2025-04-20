#!/bin/bash

# Chạy Appium
appium --address 0.0.0.0 --port 4723 --log-level info &

sleep 80
echo "Connecting to Android container..."
adb connect android-container:5555
adb devices
pytest /app/tests/ --html=/report/test_report.html --self-contained-html
