class Character:

    def __init__(self):
        # 各変数に初期値を設定。
        self.hp = 100
        self.offence = 20


class Battle:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
    

    def __doBattleOneTurn(self):

        # 攻撃
        # 順番は player1 -> player2 の順番で攻撃する。
        # ダメージ＝キャラクターの offenc
        damage = player1.offence
        player2.hp -= damage
        print("player1 が player2 に " + str(damage) + " のダメージ。")

        # 攻撃後、攻撃されたキャラクターのHPが0以下だったら。バトル終了
        if player2.hp <= 0:
            return True

        # 次の攻撃
        # ダメージ＝キャラクターの offenc
        damage = player2.offence
        player1.hp -= player2.offence
        print("player2 が player1 に " + str(damage) + " のダメージ。")

        # 攻撃後、攻撃されたキャラクターのHPが0以下だったら。バトル終了
        if player1.hp <= 0:
            return True


    # バトル実施
    # 1 vs 1 で実施
    def doBattle(self):

        # 1 vs 1 の想定
        turn_count = 0

        # 1ターンをループで回す
        while True:
            turn_count += 1
            print("ターン" + str(turn_count))

            # 1ターン分のバトルを実施
            result = self.__doBattleOneTurn()
            if result:
                break
    
            # 次のターンとし、次のフェーズを実施する。
            print("")

        if player1.hp <= 0:
            print("player2 の勝ち。")
        else:
            print("player1 の勝ち。")


if __name__ == "__main__":

    # キャラクター作成
    player1 = Character()
    player2 = Character()

    # バトル実施
    battle = Battle(player1, player2)
    battle.doBattle()