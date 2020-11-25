
import random
lin = ["当たり", "ハズレ", "まあまあ"]
#ランダムの範囲を調べる
nume = len(lin)
print(lin)

#ランダムな数を生成
kuji = random.randrange(nume)
print(lin[kuji])

