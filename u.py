
item_images = {
	"ゴリ":"gorira.jpeg",
	"男":"男.jpg",
	"女":"onnna.jpg"
}

item_order = ["ゴリ","男","女"]
#アイテムを取り出す
for item_name in item_order:
#アイテム画像表示
   print("<img src='" + item_images[item_name] + "'>")
   print(item_name + "<br>")