#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 目的: 条件分岐について学ぶためのサンプルコード


# 説明を表示
print("入力された数字が5より大きいか小さいかを調べてみよう！")
number = int(raw_input("数字を入力: "))

# 区切りを表示
print("----------------------------------")

# 「変数"number"が5より大きい」のとき, 「入力された数字は5より大きい」と表示
if number > 5:
    print("入力された数字は5より大きい")

# 「変数"number"が5より大きい」に当てはまらないとき, 「入力された数字は5以下です」と表示
else:
    print("入力された数字は5以下です")
