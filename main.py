"""
メインプログラム
"""
from mylib.charcter import Character
from mylib.battle import Battle


if __name__ == "__main__":

    # キャラクター作成
    player1 = Character("player1")
    player2 = Character("player2")

    # バトル実施
    battle = Battle(player1, player2)
    battle.do_battle()
