from mylib.Charcter import Character


class Battle:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


    # 攻撃
    def __doAttack(self, offenceCharacter :Character, deffenceCharacter :Character):
        
        # ダメージ＝キャラクターの offenc
        damage = offenceCharacter.offence
        deffenceCharacter.hp -= damage
        print(offenceCharacter.name + " が " + deffenceCharacter.name + " に " + str(damage) + " のダメージ。")
    

    # 1ターン分のバトル
    def __doBattleOneTurn(self):

        # 攻撃
        # 順番は player1 -> player2 の順番で攻撃する。
        # ダメージ＝キャラクターの offenc
        self.__doAttack(self.player1, self.player2)

        # 攻撃後、攻撃されたキャラクターのHPが0以下だったら。バトル終了
        if self.player2.hp <= 0:
            return True

        # 次の攻撃
        # ダメージ＝キャラクターの offenc
        self.__doAttack(self.player2, self.player1)

        # 攻撃後、攻撃されたキャラクターのHPが0以下だったら。バトル終了
        if self.player1.hp <= 0:
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

        if self.player1.hp <= 0:
            print("player2 の勝ち。")
        else:
            print("player1 の勝ち。")