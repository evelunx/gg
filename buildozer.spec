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
android.permissions = INTERNET
android.private_storage = 0
android.build_tools_version = 33.0.2

[toolchain]
