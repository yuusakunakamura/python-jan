# 画像用ハッシュ
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# 出力するアイテム数を変数に代入
item_cnt = int(input())

# 標準入力にあるアイテムを出力する
while item_cnt > 0:
  item = input()
  print("<img src = '" + items_imges[item] + "'>")
  item_cnt = item_cnt - 1