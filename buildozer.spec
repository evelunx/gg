[app]
title = SemkaLoveMaho
package.name = semkalovemaho
package.domain = org.evelunx
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 0

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 24.0.0
android.private_storage = 0
android.permissions = INTERNET
android.sdk_path = $HOME/android-sdk
android.ndk_path = $HOME/.buildozer/android/platform/android-ndk-r25b
android.build_tools_version = 33.0.2
android.accept_sdk_license = True

[toolchain]
