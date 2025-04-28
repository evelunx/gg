[app]
# (str) Title of your application
title = Семка и Махира

# (str) Package name
package.name = semka_love_maho

# (str) Package domain (used for android/ios packaging)
package.domain = org.semka.love.maho

# (str) Version of your application
version = 1.0

# (str) Application source directory (if relative, it will be searched from the directory where this spec file is located)
source.dir = .

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
# Add the libraries you need (for kivy app, you'll need kivy at least)
requirements = python3,kivy

# (list) Application icon (optional)
#icon.filename = %(source.dir)s/icon.png

# (bool) Include additional files or folders into package (default is False)
# (e.g. "data/*")
include_exts = 

# (str) Application versioning
version.code = 1
version.name = 1.0

# (str) Android SDK
# This is the location of your SDK installation on your system.
# If you don't have the Android SDK yet, check the instructions here:
# https://kivy.org/doc/stable/guide/packaging-android.html#installation
# You can install the SDK using `android update sdk` or `buildozer android sdk install`
android.sdk_path = /home/runner/android-sdk

# (str) Android NDK
# NDK is needed for some parts of the Android development. It needs to be installed by running:
# `buildozer android ndk install`
# Or you can use NDK that you already have on your system.
android.ndk_path = /home/runner/android-ndk

# (list) Android libraries
# This is a list of Java libraries you need for your app
android.libs = 

# (str) Android application permissions
# Android application permissions. These permissions are necessary for the app to run
android.permissions = INTERNET

# (bool) If True, the app will automatically generate the .apk
# before starting the app on Android device or emulator
# (this can take a long time for large projects)
android.auto_rebuild = True

# (str) Android architecture
# You can specify the architecture for the APK (armv7, arm64, x86, x86_64)
android.arch = armeabi-v7a

# (str) NDK version
# You can specify a specific version of the NDK to be used.
android.ndk_version = 21.3.6528147

# (bool) Whether to use SDL2 as the engine for Android
# (if you are using Kivy, you can leave it as default)
android.use_sdl2 = True

# (str) Path to the Java executable
# java.path = /usr/bin/java
