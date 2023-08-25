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

    left, center, right = chat_col.columns([1, 2, 1])

    turn = 0 # 0: AI, 1: Human
    buffer_space = 0 # how many lines to print
    for message in chat_history:
        
        if message["sender"] == "AI" :
            if turn == 1:
                for i in range(buffer_space):
                    left.write("")
                    left.write("")
            else:
                buffer_space += 1
            turn = 0
            left.write(message["text"])
        else:
            if turn == 0:
                for i in range(buffer_space):
                    right.write("")
                    right.write("")
            else:
                buffer_space += 1
            turn = 1
            right.write(message["text"])

        #  
        #  with chat_col.container():
        #      st.write("Sender: " + message["sender"])
        #      st.write("Text:   " + message["text"])

    # ===== chat room =====

    # ===== doc room =====

    doc_col.title("Document: ")

    with doc_col.expander("Doc"):
        for doc in room["docs"]:
            st.write(doc)
        

    # ===== doc room =====

