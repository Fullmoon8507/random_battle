"""
メインプログラム
"""
import streamlit as st

from mylib.charcter import Character
from mylib.battle import Battle


if __name__ == "__main__":

    # # キャラクター作成
    player1 = Character("player1")
    player2 = Character("player2")

    # # バトル実施
    battle = Battle(player1, player2)
    battle.do_battle()

    st.title("ランダムバトル")
    log_text = "\n".join(battle.battle_log_list)

    # バトルのログを表示。テキストエリアの高さは200px。
    st.text_area(
        "ログ",
        value=log_text,
        height=200,
    )
