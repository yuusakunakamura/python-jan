# coding: utf-8
# おみくじプログラム

import random
lin = input().rstrip()

# 今回は自力で全部書いてみよう！

# カンマで分割して、リストに代入
omikuj = lin.split(",")
# リストの要素数を変数に代入
num = len(omikuj)
# リストの中身を出力
print(omikuj)
# ランダムに選んだリストの要素を出力
print(omikuj[random.randrange(num)])