"""
メインプログラム
"""
import streamlit as st

from mylib.charcter import Character
from mylib.battle import Battle


if __name__ == "__main__":

    # キャラクター作成
    player1 = Character("player1")
    player2 = Character("player2")

    # バトル実施
    battle = Battle(player1, player2)
    battle.do_battle()

    # タイトル表示
    st.title("ランダムバトル")

    # キャラクター情報の表示
    col1, col2 = st.columns(2)
    with col1:
        player_info = f"<div style='border:2px solid black; padding:10px;'> \
                        <h4>{player1.name}</h4> \
                        <p>HP: {player1.hp}<br>Offence: {player1.offence}</p> \
                        </div>"
        st.markdown(player_info, unsafe_allow_html=True)
    with col2:
        player_info = f"<div style='border:2px solid black; padding:10px;'> \
                        <h4>{player2.name}</h4> \
                        <p>HP: {player2.hp}<br>Offence: {player2.offence}</p> \
                        </div>"
        st.markdown(player_info, unsafe_allow_html=True)

    st.button("攻撃")

    log_text = "\n".join(battle.battle_log_list)

    # バトルのログを表示。テキストエリアの高さは200px。
    st.text_area(
        "ログ",
        value=log_text,
        height=200,
    )
