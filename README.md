# Hackathon website for project display

Screenshot
![](https://github.com/jay1224-jay/hackathon_website/blob/master/pictures/demo-ui.png)

Video
https://github-production-user-asset-6210df.s3.amazonaws.com/53821314/263531694-249cdd41-e38a-40ea-b933-ff64928531b9.mp4

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

1. change the page title ("LawChat.tw")

main.py

```python
st.set_page_config(
    page_title="LawChat.tw",   # where you can change the title
    layout="wide",
    initial_sidebar_state="expanded",
)
```
---
2. change ```chatroom``` title (using chatroom date as default)

main.py

```python
chat_col.title( get_date(ss.current_chatroom.date) ) # replace get_date() with the string you want
```
---
3. change avatar icon

main.py

```python
# the avatar logo
ai_logo = "<icon url>"
user_logo = "<icon url>"

```

use here

```python
if msg["sender"] == "AI":
    message(msg["text"], logo=ai_logo, key=f"{i}_ai")
else:
    message(msg["text"], is_user=True, logo=user_logo, key=f"{i}_user")
```
---
4. change the appearance of button

2 styles: "primary" and "secondary" 

example:
```python
st.button("text", type="primary") # primary style button
```
---
5. change history chat button title on the sidebar

use the first message and the year as default

main.py

```python
button_title = room.chat_history[0]["text"] + '\n' + str(room.date["year"])
```
---
6. change page, primary, and secondary color

.streamlit/config.toml
```python
[theme]
primaryColor             = "#6e75d4"  # the color
backgroundColor          = "#e8e8e8"
secondaryBackgroundColor = "#ffffff"
textColor                = "#262730"
```
---
7. change __about__ page text

pages/about.py
 
write everything you want in that file
---
7. add new page

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
 

