import streamlit as st
from chatroom import chatroom, chatData
import time

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

# @st.cache_data
def generate_room(root, room):

    chat_col, doc_col = root.columns([0.6, 0.4], gap="large")
    # ===== chat room =====

    chat_col.title( get_date(room["date"]) )
    
    chat_history = room["chat_history"]

    for message in chat_history:
        with chat_col.container():
            root.write("Sender: " + message["sender"])
            root.write("Text:   " + message["text"])

    # ===== chat room =====

    # ===== doc room =====

    doc_col.title("Document: ")
    
    with doc_col.expander("Docs"):
        for doc in room["docs"]:
            st.write(doc)

    # ===== doc room =====

