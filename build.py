"""
浏览器启动器打包脚本
"""
import PyInstaller.__main__
import os

# 应用名称
APP_NAME = "BrowserLauncher"
# 主脚本
MAIN_SCRIPT = "browser_launcher.py"

PyInstaller.__main__.run([
    MAIN_SCRIPT,
    "--name", APP_NAME,
    "--onefile",           # 打包成单个exe
    "--windowed",          # 不显示控制台窗口
    "--noconfirm",         # 覆盖输出目录
    "--clean",             # 清理临时文件
    # hidden imports for customtkinter
    "--hidden-import", "customtkinter",
    "--hidden-import", "requests",
    # 添加数据文件(如果有)
    # "--add-data", "assets;assets",
])

print(f"\n打包完成! 输出文件: dist/{APP_NAME}.exe")
