class Character:

    def __init__(self, name: str):
        # 名前は必ず設定
        self.name = name

        # 各変数に初期値を設定。
        self.hp = 100
        self.offence = 20
