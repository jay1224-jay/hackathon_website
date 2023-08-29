# Hackathon website for project display

Screenshot
![](https://github.com/jay1224-jay/hackathon_website/blob/master/pictures/demo-ui.png)

Video

https://github.com/jay1224-jay/hackathon_website/assets/53821314/d03c7cfe-29b2-4041-a575-233cc703f941

## Demo App

[Demo](https://law-thon-project-test.streamlit.app/)

## run this app

```shell
git clone https://github.com/jay1224-jay/hackathon_website.git
cd hackathon_website
pip install streamlit streamlit-chat hugchat
streamlit run main.py
```

## dev log:

https://github.com/jay1224-jay/hackathon_website/commits/master

## Configuration 


### 1. add your AI model

return response based on user's prompt

```main.py```

```python
def ai_model(prompt):
    # where the LawChat.tw model should be

    # example:
    # 
    # response = my_model(prompt)
    # return response
    
    response = prompt[::-1]

    return response
```

### 2. add chat data

You can modify the value, but just remember to keep the same name (```chatData```), which will be imported in ```main.py```

```chat_data.py```

```python
c1 = chatroom(chat1["date"], chat1["chat_history"], chat1["docs"])
c2 = chatroom(chat2["date"], chat2["chat_history"], chat2["docs"])

chatData = [c2, c1]  # the complete chat data
```

### 3. change avatar icon

```main.py```

```python
# the avatar logo
ai_logo = "<icon url>"
user_logo = "<icon url>"

```

used here

```python
if msg["sender"] == "AI":
    message(msg["text"], logo=ai_logo, key=f"{i}_ai")
else:
    message(msg["text"], is_user=True, logo=user_logo, key=f"{i}_user")
```

### 4. change the appearance of button

2 styles: "primary" and "secondary" 

example:
```python
st.button("text", type="primary") # primary style button
```

### 5. change history chat button title on the sidebar

use the first message and the year as default

```main.py```

```python
button_title = room.chat_history[0]["text"] + '\n' + str(room.date["year"])
```

### 6. change page, primary, and secondary color

```.streamlit/config.toml```

```python
[theme]
primaryColor             = "#6e75d4"  # the color
backgroundColor          = "#e8e8e8"
secondaryBackgroundColor = "#ffffff"
textColor                = "#262730"
```

### 7. change __about__ page text

pages/about.py
 
write everything you want in that file

### 8. add new page

create new .py file in ```pages/```

for example:

you want to create a new page called __contact__

```
├── main.py
├── pages
    └── about.py
    └── contact.py  # create new .py file
```

you will see the result on sidebar after creating the file
 
### 9. change the page title ("LawChat.tw")

```main.py```

```python
st.set_page_config(
    page_title="LawChat.tw",   # where you can change the title
    layout="wide",
    initial_sidebar_state="expanded",
)
```

### 10. change ```chatroom``` title (using chatroom date as default)

```main.py```

```python
chat_col.title( get_date(ss.current_chatroom.date) ) # replace get_date() with the string you want
```
