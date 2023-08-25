import streamlit as st
import ui
from chatroom import chatroom, chatData



st.set_page_config(
    page_title="LawChat.tw",
    # page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "https://www.extremelycoolapp.com/bug",
    }
)

ui.generate_sidebar(st)


# st.write("start chatting")



# ui.generate_room(st, chatData[0])
