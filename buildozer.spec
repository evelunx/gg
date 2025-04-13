[app]
title = SemkaLoveMaho
package.name = semkalove
package.domain = org.evelunx
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 24.0.3
android.archs = armeabi-v7a, arm64-v8a
