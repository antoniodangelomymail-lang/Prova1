[app]
title = Hello GUI
package.name = hello_gui
package.domain = org.example
source.dir = .
source.include_exts = py,kv,txt,png,jpg,atlas
version = 0.1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 34
ndk_api = 21
archs = arm64-v8a, armeabi-v7a
