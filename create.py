"""
    # Copyright © 2022 By Nguyễn Phú Khương
    # TELEGRAM : @khuongdev0709
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""

import os
import subprocess
import sys
import shutil


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"[*] Created directory: {path}")
    else:
        print(f"[*] Directory already exists: {path}")


def git_clone(repo_url, destination):
    print(f"[*] Clone repository to {destination}")
    if not os.path.exists(destination):
        os.makedirs(destination)
    subprocess.run(["git", "clone", repo_url, destination], check=True)
    print(f"[*] Cloned Success repository to {destination}")


def create_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"[*] Created file: {file_path}")


def handle_add_option(base_path):
    app = os.path.join(base_path, "app.py")
    print(f"[*] Copy file: {app}")
    shutil.copy(
        "C:\\Users\\Khuong\\Desktop\\create-framework\\resources\\app.py", app)
    app = os.path.join(base_path, "core.py")
    print(f"[*] Copy file: {app}")
    shutil.copy(
        "C:\\Users\\Khuong\\Desktop\\create-framework\\resources\\core.py", app)
    app = os.path.join(base_path, "ui\\ui.py")
    print(f"[*] Copy file: {app}")
    shutil.copy(
        "C:\\Users\\Khuong\\Desktop\\create-framework\\resources\\ui.py", app)
    app = os.path.join(base_path, "git.ps1")
    print(f"[*] Copy file: {app}")
    shutil.copy(
        "C:\\Users\\Khuong\\Desktop\\create-framework\\resources\\git.ps1", app)
    app = os.path.join(base_path, "start.ps1")
    print(f"[*] Copy file: {app}")
    shutil.copy(
        "C:\\Users\\Khuong\\Desktop\\create-framework\\resources\\start.ps1", app)


def main(base_path, project_name):
    libs_url = "https://github.com/npk-0709/Klib.git"
    libs_path = os.path.join(base_path, "Klib")
    git_clone(libs_url, libs_path)

    create_directory(os.path.join(base_path, "config"))
    create_directory(os.path.join(base_path, "app"))
    create_directory(os.path.join(base_path, "ui"))
    create_directory(os.path.join(base_path, "resources"))
    create_directory(os.path.join(base_path, "router"))
    create_directory(os.path.join(base_path, "controller"))

    handle_add_option(base_path)

    print(f"[*] Project are created success !")
    print(f"[*] Open VsCode !")
    subprocess.run(["C:\\Users\\Khuong\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", base_path], check=True)


def run(base_path, type_create,project_name):
    if type_create == 1:
        main(base_path,project_name)
    elif not os.path.exists(base_path) and type_create == 2:
        create_directory(base_path)
        main(base_path,project_name)
    else:
        print(f"[*] Project already exists")


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1] == "start":
        project_name = os.getcwd().split('\\')[-1]
        run(os.getcwd(), 1, project_name)
    elif len(sys.argv) == 3 and sys.argv[1] == "start":
        project_name = sys.argv[2]
        base_path = os.path.join(os.getcwd(), project_name)
        run(base_path, 2, project_name)
    else:
        print("Usage: khuong start [project_name]")
        sys.exit(1)
