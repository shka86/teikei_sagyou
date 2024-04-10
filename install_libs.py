import subprocess
import sys


def install_packages():
    # 必要なパッケージのリスト
    packages = [
        'pyautogui',
        'keyboard',
        'pynput',
        'pyperclip',
    ]

    # 各パッケージをインストール
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])


if __name__ == "__main__":
    install_packages()
    print("インストールが完了しました。")
