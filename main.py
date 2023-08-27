import streamlit as st
from chatroom import chatroom, chatData
from streamlit_chat import message
from streamlit.components.v1 import html # for embedding js

import time
chatrooms = chatData

chatrooms_btns = []

def scrollbarDown():
    print("in scrollbar down")
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

current_chatroom = chatrooms[0]


# @st.cache_resource(experimental_allow_widgets=True)
def generate_room(root, room):
    chat_col, doc_col = root.columns([0.6, 0.4])

    # ===== chat room =====

    chat_col.title( get_date(current_chatroom["date"]) )
    
    chat_history = current_chatroom["chat_history"]
    
    chat_box = chat_col.expander("chat", True) # 2nd parameter should be True if you want the expander to be in "expanded" initially
    

    ai_logo = "https://t3.ftcdn.net/jpg/03/22/38/32/360_F_322383277_xcXz1I9vOFtdk7plhsRQyjODj08iNSwB.jpg"
    user_logo = "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-1/347419759_987667648912432_848655211680491487_n.jpg?stp=dst-jpg_p320x320&_nc_cat=110&ccb=1-7&_nc_sid=7206a8&_nc_ohc=dW-t7kVd4T4AX-Yh_Jp&_nc_ht=scontent-tpe1-1.xx&oh=00_AfDPpcAGXX7ropNFZzUPs1iOjEbrWi2u1VIwS-utY6xf1w&oe=64ECF617"
    with chat_box:
        for msg in chat_history:
            if msg["sender"] == "AI":
                message(msg["text"], logo=ai_logo, key=msg["text"])
            else:
                message(msg["text"], is_user=True, logo=user_logo, key=msg["text"]) # align to right

    # generate_input(chat_col)
    chat_col.text_area("type here",key="chat_input")

    # left, center, right = chat_col.columns([1, 2, 1])
    # # display chat message
    # turn = -1 # 0: AI, 1: Human
    # buffer_space = 1 # how many lines to print
    # for message in chat_history:
    #     
    #     if message["sender"] == "AI" :
    #         if turn == 1:
    #             for i in range(buffer_space):
    #                 left.write("")
    #                 left.write("")
    #             buffer_space = 1
    #         elif turn == -1:
    #             pass
    #         else:
    #             buffer_space += 1
    #         turn = 0
    #         left.write(message["text"])
    #     else:
    #         if turn == 0:
    #             for i in range(buffer_space):
    #                 right.write("")
    #                 right.write("")
    #             buffer_space = 1
    #         elif turn == -1:
    #             pass
    #         else:
    #             buffer_space += 1
    #         turn = 1
    #         right.write(message["text"])

    # ===== chat room =====

    # ===== doc room =====

    doc_col.title("Document: ")

    with doc_col.expander("Doc"):
        for doc in room["docs"]:
            st.write(doc)
        

    # ===== doc room =====

    scrollbarDown()

st.set_page_config(
    page_title="LawChat.tw",
    # page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Report a bug': "https://www.extremelycoolapp.com/bug",
    }
)

# write CSS to website
st.markdown(
"""

<style>
    .streamlit-expanderContent {
        overflow: scroll;
        height: 550px;
    }
</style>

"""
, unsafe_allow_html=True)



create_new_chat_btn = st.sidebar.button("Create A New Chat", type="primary")

st.sidebar.write("History chats")
for room in chatrooms:
    button_title = room["chat_history"][0]["text"] + '\n' + str(room["date"]["year"])
    # set the first human chat as the title

    if st.sidebar.button(button_title):
        current_chatroom = room

generate_room(st, current_chatroom)

print("chat input: " + st.session_state["chat_input"])


