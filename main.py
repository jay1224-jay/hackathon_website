import streamlit as st
from streamlit import session_state as ss
from chatroom import chatroom, chatData
from streamlit_chat import message
from streamlit.components.v1 import html # for embedding js
from streamlit_javascript import st_javascript as st_js

import time
from datetime import datetime

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
    scrollbarDown();
    </script>
        """, width=0, height=0)

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


    
def ai_model(prompt):
    # where the LawBERT.tw model should be

    # return answer
    if prompt == "":
        return "Bro, u serious??"
    elif prompt == "存證信函是什麼？":
        return "1.存證信函是指藉由郵局證明信件內容及發信日期、收信日期的信件 文書.\n2.存證信函僅能證明發信人在信中表達了一定的意思表示，而且收信者確 實收到了信件.\n3.存證信函並不能夠代表發信者確實擁有信中敘述的權利，也不能夠代表 收信者即負有信中所敘述或要求的義務。"
    return prompt[::-1]

def get_ai_response(prompt):

    return ai_model(prompt)



# @st.cache_resource(experimental_allow_widgets=True)


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
submit_btn = st.button("Submit", type="primary", key="submit_btn", on_click=add_new_message, args=("Bob", ss['chat_input']))


# ===== chat room =====

# ===== doc room =====

doc_col.title("Document: ")

if ss.current_chatroom.docs == []:
    doc_col.markdown("### Empty")
else:
    with doc_col.expander("Doc", False):
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

    st_js("""function scrollbarDown() {
            const e = window.parent.document.getElementsByClassName("streamlit-expanderContent");
            e[0].scrollTop = e[0].scrollHeight; //  - e[0].clientHeight;
            console.log("scrollbar");
           }
           scrollbarDown();
           """) 
    st_js("console.log(\"in\");")
    print("st js work successfully")

def create_new_chat():

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

    chatrooms.insert(0, room)
    
    change_room(room)


create_new_chat_btn = st.sidebar.button("Create A New Chat", type="primary", on_click=create_new_chat)

st.sidebar.write("History chats")

room_count = 0
for room in chatrooms:
    if room.chat_history == []: # avoid empty chat history
        room.chat_history.append({})
        room.chat_history[0]["sender"] = "AI"
        room.chat_history[0]["text"] = "Welcome to LawChat.tw."

    # the title on the sidebar
    # set the first human chat as the title
    button_title = room.chat_history[0]["text"] + '\n' + str(room.date["year"])

    st.sidebar.button(button_title, on_click=change_room, args=(room,), key=f"{room_count}_{button_title}")
    room_count += 1


js = f"""
<script>
    function scroll(dummy_var_to_force_repeat_execution){{
        var textAreas = window.parent.document.querySelectorAll('');
        for (let index = 0; index < textAreas.length; index++) {{
            textAreas[index].style.color = 'red'
            textAreas[index].scrollTop = textAreas[index].scrollHeight;
        }}
    }}
    scroll( {len(st.session_state.chat)} )
</script>
"""

html(js)
