#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 目的: 条件分岐について学ぶためのサンプルコード


# 説明文を表示
print("0時から24時までの任意の時間を入力してみよう")

# 変数 "time" に説明文のあとに入力された文字を数値として入れる（代入）
time = int(raw_input("時間(0〜24の範囲の数字)を入力: "))

# 区切りを表示
print("------------------------------------------")
# 「変数 "time" が12より小さい」かつ「変数 "time" が0以上」のとき,「AMです!」と表示
if time < 12 and time >= 0:
    print("AMです！")

# 「変数 "time" が12以下」かつ「変数 "time" が24以下」のとき，「PMです!」と表示
elif time >= 12 and time <= 24:
    print("PMです!")

# 上２つの条件に当てはまらない場合の説明を表示
else:
    print("{}時なんて存在しないよ！".format(time))