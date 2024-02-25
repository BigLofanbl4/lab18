#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Скрипт на Python, который автоматизирует управление
# файлами на компьютере с помощью функций модуля os.
#
# Скрипт выполняет следующие функции:
# 
# 1. Переместиться в рабочую директорию (путь рабочей директории
# указывается как аргумент командой строки), где будет проводиться
# управление файлами.
#
# 2. Создать поддиректории 'Images', 'Docs', 'Audio' и 'Others'
# для сортировки файлов.
#
# 3. Перенос файлы из рабочей директории в соответствующие поддиректории
# на основе их расширений. Например, изображения (.jpg, .png) должны быть
# перемещены в 'Images', документы (.pdf, .txt) - в 'Docs',
# аудиофайлы (.mp3, .wav) - в 'Audio'. Все остальные файлы
# должны быть перемещены в 'Others'.
#
# 4. Удаление пустой директории 'Temp', если она существует
# в рабочей директории.
#
# 5. В конце скрипта вывод полного пути к рабочей директории.


import os
import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Word directory path is not given!", file=sys.stderr)
        sys.exit(1)

    work_directory = sys.argv[1]
    os.chdir(work_directory)

    file_map = {
        ".jpg": "Images",
        ".png": "Images",
        ".mp3": "Audio",
        ".wav": "Audio",
        ".txt": "Doc",
        ".pdf": "Doc",
    }

    for folder in ["Images", "Audio", "Doc", "Others"]:
        if not os.path.exists(folder):
            os.mkdir(folder)

    for file_name in os.listdir("."):
        if not os.path.isfile(file_name):
            continue
        file_ext = os.path.splitext(file_name)[1]
        os.rename(file_name, f'{file_map.get(file_ext, "Others")}/{file_name}')

    if os.path.exists("Temp"):
        os.rmdir("Temp")

    print(f"Word directory is {os.getcwd()}")
