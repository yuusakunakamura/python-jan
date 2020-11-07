
import random
line = ["当たり", "ハズレ", "まあまあ"]
#ランダムの範囲を調べる
num = len(line)
print(line)

#ランダムな数を生成
kuji = random.randrange(num)
print(line[kuji])

