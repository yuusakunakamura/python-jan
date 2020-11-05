# 九九の表を作成してみよう

def multiply(x, y):
    return x * y

for step in range(1, 10):
    for num in range(1, 10):
        print(multiply(step, num), end="")
        if num < 9:
            print(", ", end="")
    print("")


    # coding: utf-8
# メソッドをオーバーライドしよう

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    # ここにオーバライドするメソッドを記述する
    def say_hello(self, target):
        print(self.msg + " " + target)


player = Hello()
player.say_hello("python")