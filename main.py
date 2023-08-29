import streamlit as st
from streamlit import session_state as ss
from streamlit_chat import message
from streamlit.components.v1 import html # for embedding js

from chat_data import chatroom, chatData # import the chat data, see chatroom.py for further information

from datetime import datetime
import re

st.set_page_config(
    page_title="LawChat.tw",
    # page_icon="",
    layout="wide",
    initial_sidebar_state="expanded",
    # menu_items={
    #     'Report a bug': "com/bug",
    # }
)

chatrooms = chatData  # where all chat data stores

if "current_chatroom" not in ss:
    ss["current_chatroom"] = chatrooms[0]
ss["current_messages"] = ss.current_chatroom.chat_history
ss["scrollbarDownVar"] = 0  # tell the scrollbar when to scroll to the bottom


def get_date(date):
    # date is dict
    date_number = [ str(x) if x >= 10 else "0"+str(x) for x in date.values() ]

    return "{}-{}-{} {}:{}".format(date_number[0],date_number[1],date_number[2],date_number[3],date_number[4])

def add_new_message(sender, message):
    
    ai_name = ["ai", "AI"]

    mm = {"sender": sender, "text" : message}
    ss.current_chatroom = ss.current_chatroom.send_msg(sender, message)
    ss.current_messages = ss.current_chatroom.chat_history
    ss.chat_input = ""

    if sender not in ai_name:
        add_new_message("AI", get_ai_response(message))

    ss["scrollbarDownVar"] += 1
    
def ai_model(prompt):
    # where the LawChat.tw model should be

    # example:
    # 
    # answer = my_model(prompt)
    # return answer

    return prompt[::-1] # fake model ??

def get_ai_response(prompt):
    # call model to get response

    return ai_model(prompt)

def change_room(room):
    ss.current_chatroom = room
    ss.current_messages = room.chat_history

    ss["scrollbarDownVar"] += 1

def create_new_chat():

    # backup function 
    # use this if there's no chatroom.create_new_chat()

    tmp = datetime.now()

    date_dict = dict()
    date_dict["year"] = tmp.year
    date_dict["month"] = tmp.month
    date_dict["day"] = tmp.day
    date_dict["hour"] = tmp.hour
    date_dict["minute"] = tmp.minute
    date_dict["second"] = tmp.second
    
    # add greeting words
    chat_history_list = []
    chat_history_list.append({})
    chat_history_list[0]["sender"] = "AI"
    chat_history_list[0]["text"] = "Welcome to LawChat.tw."

    docs_list = []

    room = chatroom(date_dict, chat_history_list, docs_list)

    chatrooms.insert(0, room) # add new chatroom to the front
    
    change_room(room) # redirect to the new chatroom

def get_doc_title(doc):

    doc_title = ""
    for title in doc.split('\n'):
        if title != "":
            doc_title = title
            break
    return doc_title.replace("#", "").replace(" ", "")

def divide_doc(doc):
    # return 1 if doc is 判決書, else return 0 if doc is 法條


    judge_book_keyword = ["裁定", "判決", "法院"]

    doc_title = get_doc_title(doc)

    flag = 0
    for k in judge_book_keyword:
        if k in doc_title:
            flag = 1
            break
    return flag


doc_law = []
doc_judge_page = []

def refresh_doc_list(dummy_var_force):
    doc_law = []
    doc_judge_page = []

refresh_doc_list(ss["current_messages"])

# create 2 columns: chat column and document column
chat_col, doc_col = st.columns([0.6, 0.4])

# ===== chat room =====
# set chatroom date as title 
chat_col.title( get_date(ss.current_chatroom.date) )


chat_box = chat_col.expander("chat", True) # 2nd parameter should be True if you want the expander to be in "expanded" initially

# the avatar logo
ai_logo = "https://t3.ftcdn.net/jpg/03/22/38/32/360_F_322383277_xcXz1I9vOFtdk7plhsRQyjODj08iNSwB.jpg"
user_logo = "https://scontent-tpe1-1.xx.fbcdn.net/v/t39.30808-1/347419759_987667648912432_848655211680491487_n.jpg?stp=dst-jpg_p320x320&_nc_cat=110&ccb=1-7&_nc_sid=7206a8&_nc_ohc=dW-t7kVd4T4AX-Yh_Jp&_nc_ht=scontent-tpe1-1.xx&oh=00_AfDPpcAGXX7ropNFZzUPs1iOjEbrWi2u1VIwS-utY6xf1w&oe=64ECF617" # our boss

msg_count = 0
with chat_box:
    for i in range(len(ss.current_messages)):
        msg = ss.current_messages[i]
        if msg["sender"] == "AI":
            message(msg["text"], logo=ai_logo, key=f"{i}_ai")
        else:
            message(msg["text"], is_user=True, logo=user_logo, key=f"{i}_user")
        msg_count += 1 # create unique id for message() widget

chat_col.text_area("type here", key="chat_input") # where user can type
submit_btn = chat_col.button("Submit", type="primary", key="submit_btn", on_click=add_new_message, args=("Bob", ss['chat_input'])) # submit button
# ===== chat room =====

# ===== doc room =====
# The document viewer


doc_col.title("Document: ")

if ss.current_chatroom.docs == []:
    doc_col.markdown("### Empty")
else:
    # with doc_col.expander("Doc", True):
    for doc in ss.current_chatroom.docs:
        if divide_doc(doc) == 1:
            doc_judge_page.append(doc)
        else:
            doc_law.append(doc)

    doc_col.markdown("### 法律條文")
    for doc in doc_law:
        with doc_col.expander(get_doc_title(doc)):
            st.write(doc)

    doc_col.markdown("### 判決書")
    for doc in doc_judge_page:
        with doc_col.expander(get_doc_title(doc)):
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
    div[data-testid=\"stMarkdownContainer\"] {
        font-size: 20px;
    }
</style>

"""
, unsafe_allow_html=True)

# create widget on sidebar(left)
create_new_chat_btn = st.sidebar.button("Create A New Chat", type="primary", on_click=create_new_chat)

st.sidebar.write("History chats")

room_count = 0
for room in chatrooms:
    if room.chat_history == []: # avoid empty chat history
        room.chat_history.append({})
        room.chat_history[0]["sender"] = "AI"
        room.chat_history[0]["text"] = "Welcome to LawChat.tw."

    # the title on the sidebar
    # set the first chat as the title
    button_title = room.chat_history[0]["text"] + '\n' + str(room.date["year"])

    st.sidebar.button(button_title, on_click=change_room, args=(room,), key=f"{room_count}_{button_title}")
    room_count += 1


js = f"""
<script>

    function sleep(ms) {{
        console.log(\"sleep\");
        return new Promise(resolve => setTimeout(resolve, ms));
    }}
    async function scroll(dummy_var_to_force_repeat_execution){{
        // console.log("scroll");
        await sleep(0.5 * 1000); // sleep 0.5 sec
        var expander = window.parent.document.getElementsByClassName("streamlit-expanderContent");
        expander[0].scrollTop = expander[0].scrollHeight;
    }}


    scroll( {len(ss.current_messages)} );
</script>
"""
# make scrollbar scroll to the bottom when there's any change in the chats
html(js)

st.write(ss.scrollbarDownVar)


# # useful references:
# 
# scrollbar automatically scrolls to the bottom:
# https://discuss.streamlit.io/t/how-do-i-move-the-default-scroll-of-st-text-area-to-the-bottom/39320
# 
# no refresh after click the button?
# https://discuss.streamlit.io/t/what-causes-a-streamlit-form-to-refresh-after-clicking-the-submit-button-and-how-can-i-fix-it/44393
# 
# modern chatbot UI in streamlit
# https://github.com/AI-Yash/st-chat
# 
# streamlit documentation
# https://docs.streamlit.io/
# 
# streamlit session state official doc
# https://docs.streamlit.io/library/api-reference/session-state
# 
# add scrollbar using CSS in streamlit
# https://discuss.streamlit.io/t/how-to-add-scroll-bar-in-st-expander/41579/3
# 
# embed Javascript in streamlit
# https://discuss.streamlit.io/t/how-to-embed-javascript-into-streamlit/20152/3
# 
# custom avatar icon in streamlit_chat
# https://github.com/AI-Yash/st-chat/pull/34

