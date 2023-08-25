import streamlit as st
from chatroom import chatroom, chatData


chatrooms = chatData

chatrooms_btns = []

def generate_sidebar(root):

    create_new_chat_btn = root.sidebar.button("Create A New Chat", type="primary")

    root.sidebar.write("History chats")
    for room in chatrooms:
        button_title = room["chat_history"][0]["text"] + '\n' + str(room["date"]["year"])
        # set the first human chat as the title

        if root.sidebar.button(button_title):
            generate_room(root, room)
        # root.sidebar.button(button_title)


def get_date(date):
    # date is dict
    date_number = [ str(x) if x >= 10 else "0"+str(x) for x in date.values() ]

    return "{}-{}-{} {}:{}".format(date_number[0],date_number[1],date_number[2],date_number[3],date_number[4])

@st.cache_resource
def generate_room(root, chat):

    root.title( get_date(chat["date"]) )
    root.write("sender: " + chat["chat_history"][1]["sender"])
    root.write("text: " + chat["chat_history"][1]["text"])

