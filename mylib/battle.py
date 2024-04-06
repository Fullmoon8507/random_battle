"""
バトルに関するクラス
"""
import math
import random

from mylib.charcter import Character


class Battle:
    """
    バトルクラス
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2


    # 攻撃
    def __do_attack(self, offence_character :Character, deffence_character :Character):

        """
        ダメージ＝キャラクターの offenc * 乱数（0.8 ~ 1.2）
        """
        # 乱数生成
        rand = random.uniform(0.8, 1.2)

        # ダメージを計算　※小数点は切り捨て
        damage = math.floor(offence_character.offence * rand)

        # ダメージを反映
        deffence_character.hp -= damage

        print(
            offence_character.name + " が " + deffence_character.name + " に " + \
            str(damage) + " のダメージ。")


    # 1ターン分のバトル
    def __do_battle_one_turn(self):

        # 攻撃
        # 順番は player1 -> player2 の順番で攻撃する。
        # ダメージ＝キャラクターの offenc
        self.__do_attack(self.player1, self.player2)

        # 攻撃後、攻撃されたキャラクターのHPが0以下だったら。バトル終了
        if self.player2.hp <= 0:
            return True

        # 次の攻撃
        # ダメージ＝キャラクターの offenc
        self.__do_attack(self.player2, self.player1)

        # 攻撃後、攻撃されたキャラクターのHPが0以下だったら。バトル終了
        if self.player1.hp <= 0:
            return True


    def do_battle(self):
        """
        バトル実施
        1 vs 1 で実施
        """

        # 1 vs 1 の想定
        turn_count = 0

        # 1ターンをループで回す
        while True:
            turn_count += 1
            print("ターン" + str(turn_count))

            # 1ターン分のバトルを実施
            result = self.__do_battle_one_turn()
            if result:
                break

            # 次のターンとし、次のフェーズを実施する。
            print("")

        if self.player1.hp <= 0:
            print("player2 の勝ち。")
        else:
            print("player1 の勝ち。")
