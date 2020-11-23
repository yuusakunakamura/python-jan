# coding: utf-8
# おみくじプログラム

import random
lin = input().rstrip()

# 今回は自力で全部書いてみよう！

# カンマで分割して、リストに代入
omikuji = lin.split(",")
# リストの要素数を変数に代入
num = len(omikuji)
# リストの中身を出力
print(omikuji)
# ランダムに選んだリストの要素を出力
print(omikuji[random.randrange(num)])