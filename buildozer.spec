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

# =========================================================
# QUAN TRỌNG: THƯ VIỆN YÊU CẦU (ĐÃ THÊM OPENCV + NUMPY)
# =========================================================
requirements = python3,kivy,pyjnius,pillow,plyer,certifi,pyzbar,opencv-python-headless==4.5.5.64,numpy==1.19.5

# =========================================================
# QUYỀN ANDROID (GIỮ NGUYÊN)
# =========================================================
android.permissions = INTERNET,ACCESS_NETWORK_STATE,BLUETOOTH,BLUETOOTH_ADMIN,BLUETOOTH_CONNECT,BLUETOOTH_SCAN,ACCESS_FINE_LOCATION,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,CAMERA

# =========================================================
# MANIFEST (GIỮ NGUYÊN)
# =========================================================
android.manifest = android-manifest.xml

android.manifest.extra = <uses-feature android:name="android.hardware.camera" android:required="false" />

android.manifest.extra = 
    <uses-feature android:name="android.hardware.camera" android:required="false" />
    <uses-feature android:name="android.hardware.camera.autofocus" android:required="false" />

# =========================================================
# LIBZBAR CHO PYZBAR (GIỮ NGUYÊN - NHƯNG CẦN ĐÚNG CÁCH)
# =========================================================
# ⚠️ LƯU Ý: "android.add_src = libzbar" KHÔNG ĐÚNG CÚ PHÁP
# Cách đúng: Đặt file libzbar.so vào thư mục libs/ và dùng:
# android.add_libs_armeabi_v7a = libs/armeabi-v7a/libzbar.so
# android.add_libs_arm64_v8a = libs/arm64-v8a/libzbar.so
# HOẶC xóa dòng này và để Buildozer tự xử lý qua recipe pyzbar

# === TẠM THỜI COMMENT DÒNG NÀY ĐỂ TRÁNH LỖI BUILD ===
# android.add_src = libzbar

# --- Tài nguyên đính kèm ---
# android.add_assets = arial.ttf,wifi_printers.json

# --- Màn hình khởi động ---
presplash.filename = %(source.dir)s/icon.png
android.presplash_color = #FFFFFF

# =========================================================
# ANDROID SDK / NDK - TỐI ƯU CHO OPENCV + NUMPY
# =========================================================
android.api = 33
android.minapi = 24                  # ⚠️ NÂNG LÊN 24 CHO NUMPY
android.ndk = 23c                    # ⚠️ HẠ XUỐNG 23c CHO OPENCV ỔN ĐỊNH
android.ndk_api = 21
android.archs = arm64-v8a,armeabi-v7a

# =========================================================
# P4A BRANCH (GIỮ NGUYÊN)
# =========================================================
p4a.branch = develop

android.allow_backup = True

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