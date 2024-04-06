class Character:

    def __init__(self):
        # 暫定でHPを100固定とする。
        self.hp = 100


if __name__ == "__main__":

    # キャラクター作成
    player1 = Character()
    player2 = Character()

    # バトル実施
    # 1 vs 1 の想定
    turn_count = 0

    # 1ターンをループで回す
    while True:
        turn_count += 1
        print("ターン" + str(turn_count))

        # 攻撃
        # 順番は player1 -> player2 の順番で攻撃する。
        # ダメージも20固定で。
        player2.hp -= 20
        print("player1 が player2 に 20 のダメージ。")

        # 攻撃後、攻撃されたキャラクターのHPが0以下だったら。バトル終了
        if player2.hp <= 0:
            break

        # 次の攻撃
        player1.hp -= 20
        print("player2 が player1 に 20 のダメージ。")

        # 攻撃後、攻撃されたキャラクターのHPが0以下だったら。バトル終了
        if player1.hp <= 0:
            break

        # 次のターンとし、次のフェーズを実施する。
        print("")
    
    if player1.hp <= 0:
        print("player2 の勝ち。")
    else:
        print("player1 の勝ち。")