#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def count_substring(text, sub):
    if len(text) < len(sub):
        return 0

    if text[:len(sub)] == sub:
        return 1 + count_substring(text[len(sub):], sub)
    else:
        return count_substring(text[1:], sub)

def main():
    text = input("Введите основной текст: ")
    sub = input("Введите подстроку для поиска: ")

    result = count_substring(text, sub)
    print(f"\nРезультат: {result}")
    print(f"Подстрока '{sub}' встречается в тексте {result} раз(а)")
if __name__ == "__main__":
    main()