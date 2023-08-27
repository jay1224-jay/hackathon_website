import streamlit as st
from streamlit import session_state as ss
from chatroom import chatroom, chatData
from streamlit_chat import message
from streamlit.components.v1 import html # for embedding js

import time

st.set_page_config(
    page_title="LawChat.tw",
    # page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "https://www.extremelycoolapp.com/bug",
    }
)

chatrooms = chatData

chatrooms_btns = []
if "current_chatroom" not in ss:
    ss["current_chatroom"] = chatrooms[0]

ss["current_messages"] = ss.current_chatroom.chat_history

def scrollbarDown():
    time.sleep(1) # time sleep to wait for the chat box appearing
    html(
        """
    <script language="javascript">
    const e = window.parent.document.getElementsByClassName("streamlit-expanderContent");
    e[0].scrollTop = e[0].scrollHeight; //  - e[0].clientHeight;
    console.log("scrollbar");
    </script>
        """, width=0, height=0)

def get_date(date):
    # date is dict
    date_number = [ str(x) if x >= 10 else "0"+str(x) for x in date.values() ]

    return "{}-{}-{} {}:{}".format(date_number[0],date_number[1],date_number[2],date_number[3],date_number[4])

def add_new_message(sender, message):
    
    mm = {"sender": sender, "text" : message}
    ss.current_chatroom = ss.current_chatroom.send_msg(sender, message)
    ss.current_messages = ss.current_chatroom.chat_history
    ss.chat_input = ""

    # generate_room(st, st.session_state.current_chatroom)
    


# @st.cache_resource(experimental_allow_widgets=True)

# ss.current_chatroom = room

chat_col, doc_col = st.columns([0.6, 0.4])

# ===== chat room =====

chat_col.title( get_date(ss.current_chatroom.date) )

# chat_history = room.chat_history

chat_box = chat_col.expander("chat", True) # 2nd parameter should be True if you want the expander to be in "expanded" initially


ai_logo = "https://t3.ftcdn.net/jpg/03/22/38/32/360_F_322383277_xcXz1I9vOFtdk7plhsRQyjODj08iNSwB.jpg"
user_logo = "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-1/347419759_987667648912432_848655211680491487_n.jpg?stp=dst-jpg_p320x320&_nc_cat=110&ccb=1-7&_nc_sid=7206a8&_nc_ohc=dW-t7kVd4T4AX-Yh_Jp&_nc_ht=scontent-tpe1-1.xx&oh=00_AfDPpcAGXX7ropNFZzUPs1iOjEbrWi2u1VIwS-utY6xf1w&oe=64ECF617"

msg_count = 0
with chat_box:
    for i in range(len(ss.current_messages)):
        msg = ss.current_messages[i]
        if msg["sender"] == "AI":
            message(msg["text"], logo=ai_logo, key=f"{i}_ai") # , key=str(msg_count) + msg["text"])
        else:
            message(msg["text"], is_user=True, logo=user_logo, key=f"{i}_user") # , key=str(msg_count) + msg["text"]) # align to right
        msg_count += 1



chat_col.text_area("type here", key="chat_input")
submit_btn = st.button("Submit", key="submit_btn", on_click=add_new_message, args=("Bob", ss['chat_input']))
# if submit_btn:
#     # print("text: ", st.session_state["chat_input"])
#     # add_new_message(ss.current_chatroom, "user", ss["chat_input"])
#     ss.current_messages.append({"sender": "user", "text": ss['chat_input']})
#     ss.current_messages = ss.current_messages



# ===== chat room =====

# ===== doc room =====

doc_col.title("Document: ")

with doc_col.expander("Doc"):
    for doc in ss.current_chatroom.docs:
        st.write(doc)
    

# ===== doc room =====



# write CSS to website
st.markdown(
"""

<style>
    .streamlit-expanderContent {
        overflow: scroll;
        height: 520px;
    }
</style>

"""
, unsafe_allow_html=True)

def change_room(room):
    ss.current_chatroom = room
    ss.current_messages = room.chat_history


create_new_chat_btn = st.sidebar.button("Create A New Chat", type="primary")

st.sidebar.write("History chats")
for room in chatrooms:
    button_title = room.chat_history[0]["text"] + '\n' + str(room.date["year"])
    # set the first human chat as the title

    st.sidebar.button(button_title, on_click=change_room, args=(room,))


# generate_room(st, ss.current_chatroom, ss.current_messages)

# st.write(ss)
st.write(ss["current_chatroom"])
# st.write(ss["current_chatroom"])
for msg in ss.current_messages:
    st.write(msg["sender"])
    st.write(msg["text"])
