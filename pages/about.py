import streamlit as st

# About page

st.title("About")

st.markdown("### LawBERT.tw")
st.markdown(
        """
        - 用途: 實現更佳的相似度搜索
        - 訓練數據: 清洗過的法律文件
        - Pretrained Model:
        \t- ckiplab/bert-base-chinese
        """)

st.markdown("---")

st.markdown("### Fantasy2Reality.tw")
st.markdown(
        """
        - 用途: 將判決書主文變成現實中委託人和律師的對話
        - 訓練數據: 判決書主文和法律人標記後的對話
        - Pretrained Model:
        \t- ckip-joint/bloom-3b-zh
        \t- THUDM/chatglm2-6b
        """)

st.markdown("---")

st.markdown("### LawChat.tw")
st.markdown(
        """
        - 用途: 讓使用者問問題的類ChatGPT助理
        - 訓練數據: 問題-答案對
        - Pretrained Model:
        \t- ckip-joint/bloom-3b-zh
        \t- THUDM/chatglm2-6b

        """)


