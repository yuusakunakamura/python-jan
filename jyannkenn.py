import random

#ゲームクラス   
class Game:
    
    hands = { 0: "グー", 1:"チョキ", 2:"パー" }
    decision = { 0:"引き分け", 1:"負け", 2:"勝ち"}

#ゲーム開始クラス
class GameStart:
    
    print("じゃんけん・・・")

    #判定処理
    def Judge(self, player):
        #入力された値が0～2以外の場合は、戻り値(0)を返す
        if 0 <= player <= 2:
            self.player = player
        
            #相手の手をランダムで決定
            com = random.randint(0,2)

            #自分と相手の出した手を出力
            print("あなたは" + Game.hands[player] + "をだしました")
            print("あいては" + Game.hands[com] + "をだしました")

            #勝負の判定
            decision = (self.player - com + 3) % 3

            #結果の出力
            print("勝敗結果は" + Game.decision[decision] + "です")

            #判定結果を返す
            #引き分けの場合は0を返す
            return decision

        else:
            print("0～2の範囲で数字を入力してください")
            return 0


#メイン処理
draw = 0

#GameStartクラスの戻り値が引き分け(0)の場合、処理を繰り返す
while draw == 0:
    game = GameStart()
    try:
        player_hand = int(input("0=グー, 1=チョキ, 2=パー: "))
        draw = game.Judge(player_hand)
    except ValueError:
        print("数値で入力してください")
        draw == 1