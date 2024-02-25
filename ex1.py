#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":
    digits_words = {
        "0": "ноль",
        "1": "один",
        "2": "два",
        "3": "три",
        "4": "четыре",
        "5": "пять",
        "6": "шесть",
        "7": "семь",
        "8": "восемь",
        "9": "девять",
    }

    with open("file.txt", "r", encoding="utf-8") as fileptr:
        sentences = fileptr.readlines()

    for sentence in sentences:
        sentence = sentence.strip()

        for digit, word in digits_words.items():
            sentence = sentence.replace(digit, word)
        print(sentence)
