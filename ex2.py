#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("FileName is not given!", file=sys.stderr)
        sys.exit(1)
    file_name = sys.argv[1]

    with open(file_name, "r", encoding="utf-8") as fileptr:
        sentences = fileptr.readlines()

    for line_num, sentence in enumerate(sentences):
        sentence_words = sentence.split(" ")
        prev_word = ""

        for curr_word in sentence_words:
            if prev_word == curr_word:
                print(f"Line: {line_num + 1}, repeating word: {curr_word}")
            prev_word = curr_word
