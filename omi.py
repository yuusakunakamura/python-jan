
import random
line = ["当たり", "ハズレ", "まあまあ"]
#ランダムの範囲を調べる
nume = len(line)
print(line)

#ランダムな数を生成
kuji = random.randrange(nume)
print(line[kuji])

