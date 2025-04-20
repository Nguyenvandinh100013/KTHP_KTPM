#!/bin/bash

# Chạy Appium
appium --address 0.0.0.0 --port 4723 --log-level info &

sleep 80
echo "Connecting to Android container..."
adb connect android-container:5555
adb devices
/opt/robot-env/bin/robot -v SERVER:vv -v ENV:staging -v OS:ANDROID -v DEVICE:NEXUS_5_ANDROID_13 --loglevel DEBUG --suitestatlevel 3 /app/e2e-tests/testcases/bitfinex/guest_user
