[app]
# --- Thông tin ứng dụng ---
title = Order Printer
package.name = orderprinter
package.domain = org.example

# --- File nguồn ---
source.dir = .
source.include_exts = py,png,jpg,jpeg,ttf,xml,json
icon.filename = %(source.dir)s/icon.png

# --- Phiên bản ---
version = 1.0.0

# --- Hiển thị ---
orientation = portrait
fullscreen = 0

# --- Thư viện yêu cầu ---
# ⭐ COMBO: PYZBAR + OPENCV 4.5.5.64 + NUMPY (KHÔNG VERSION)
requirements = python3,kivy,pyjnius,pillow,plyer,certifi,pyzbar,opencv-python-headless==4.5.5.64,numpy

# --- Quyền Android ---
android.permissions = INTERNET,ACCESS_NETWORK_STATE,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA,VIBRATE

# === MANIFEST ===
android.manifest = android-manifest.xml
android.manifest.extra = 
    <uses-feature android:name="android.hardware.camera" android:required="false" />
    <uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />

# === LIBZBAR (BẮT BUỘC CHO PYZBAR) ===
android.add_src = libzbar

# --- Tài nguyên đính kèm ---
presplash.filename = %(source.dir)s/icon.png
android.presplash_color = #FFFFFF

# --- Android SDK / NDK ---
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.archs = arm64-v8a,armeabi-v7a

# ⭐ Dùng develop để hỗ trợ tốt nhất
p4a.branch = develop

android.allow_backup = True
android.enable_androidx = True

# --- Giảm kích thước APK ---
exclude_patterns = tests,docs,*.pyc,*.pyo,*.md,__pycache__,.git

# --- Môi trường ---
environment = 
    PYTHONOPTIMIZE=2
    KIVY_METRICS_DENSITY=2

[buildozer]
log_level = 2
warn_on_root = 1
android.accept_sdk_license = True
android.enable_androidx = True
