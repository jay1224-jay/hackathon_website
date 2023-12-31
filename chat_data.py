
# standard chatroom class
#
# essential attributes:
#   1. date
#   2. chat_history
#   3. docs
#
# essential methods
#   1. send_msg(sender, text)
#
# only one way to get attributes' value     '
#   1. chatroom.<attributes> # how main.py get the value
# 
# if you want to get value using dict{} ( maybe your original data uses dict{} )
#   chatroom["chat_history"]
# 
# please do not use chatroom and remember to replace ".<attribute>" with "['<attritube>']"
#   chatroom.date -> chatroom["date"]
 


class chatroom:

    def __init__(self, date, chat_history, docs):

        self.date = date # date the chatroom created
        self.chat_history = chat_history
        self.docs = docs

    def send_msg(self, sender, text):
        
        chat_dict = {"sender": sender, "text": text}
        self.chat_history.append(chat_dict)

        return self

    def add_doc(self, doc):

        self.docs.append(doc)

        return self


chat1 = {
    "date": {
        "year": 2023,
        "month": 8,
        "day": 25,
        "hour": 6,
        "minute": 0
    },
    "chat_history": [
        {
            "sender": "Bob",
            "text": "嗨",
        },
        {
            "sender": "AI",
            "text": "你好，這是Bing。",
        },
        {
            "sender": "Bob",
            "text": "今天天氣如何？",
        },
        {
            "sender": "AI",
            "text": "我我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。不確定，但我可以幫你查詢。",
        },
        {
            "sender": "AI",
            "text": "我我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。不確定，但我可以幫你查詢。",
        },
        {
            "sender": "AI",
            "text": "我我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。我不確定，但我可以幫你查詢。不確定，但我可以幫你查詢。",
        },
        {
            "sender": "Bob",
            "text": "謝謝",
        }
    ],
    "docs": [
            """
            # 民法第301條
            第三人與債務人訂立契約承擔其債務者，非經債權人承認，對於債權人不生效力。
            """,
            """
            # 民法第1024條
            pow(2, 10) = 1024.
            """,
            """
            # 臺灣苗栗地方法院 112 年度司促字第 5565 號民事裁定
            一、債務人應向債權人連帶清償新臺幣115,324元，及如附表所示之利息、違約金，並連帶賠償督促程序費用新臺幣500元，否則應於本命令送達後20日之不變期間內，向本院提出異議。
二、債權人請求之原因事實：
    （一）債務人陳彥成於民國105年至106年間邀同債務人陳文智、謝玉卿為連帶保證人向債權人訂借「高中以上學生就學貸款」3筆，共計新臺幣139,371元整，借款期限及償還辦法還款方式為於階段學業完成或休退學、退伍後滿一年之日起開始分72期，每滿一個月為一期平均攤還本金或本息。倘借款人不依期償還本金或本息時，除應自遲延日起按約定利率計付遲延利息外，另按遲延還本付息部分，本金自到期日起，遲延利息自付息日起，照應還款額，逾期六個月以內者，按借款利率百分之十，逾期超過六個月以上者，按借款利率百分之二十加計違約金。（二）依借據約定，借款人有任何一宗債務不依約清償本金、利息時，即喪失分期償還權利，債權人得終止契約，追償全部借款本息暨違約金，詎債務人陳彥成於就讀學校畢業後自民國112年5月1日起未依約履行計尚欠本金新臺幣115,324元及如附表所示之利息違約金等未清償，迭經催討，未蒙繳納，債務人陳文智、謝玉卿既為連帶保證人，自應依如附表所示之借款本金、利息及違約金負連帶清償責任。（三）本件就學貸款係政策性貸款，懇請  鈞院向債務人住所送達，無法送達時，酌情依據民事訴訟法第一百三十八條第一項之規定，准予寄存送達，又本件係請求一定數量之金錢債務，依民事訴訟法第五○八條之規定，狀請  鈞院鑒核，依督促程序對債務人等核發支付命令，實感德便。釋明文件：1.就學貸款放出查詢單 2.放款借據影本 3.撥款通知書影本 4.利率表 5.戶籍謄本
            """
    ]
} 

chat2 = {
    "date": {
        "year": 2025,
        "month": 8,
        "day": 23,
        "hour": 13,
        "minute": 59
    },
    "chat_history": [
        {
            "sender": "Jay",
            "text": "hola",
        },
        {
            "sender": "AI",
            "text": "hola amigo",
        },
        {
            "sender": "AI",
            "text": "Do u have any problems??",
        },
        {
            "sender": "Jay",
            "text": "how's ur day, bro??",
        },
        {
            "sender": "AI",
            "text": "shit",
        },
        {
            "sender": "Jay",
            "text": "so do I",
        },
        {
            "sender": "Jay",
            "text": "Then what is the smallest prime number?",
        },
        {
            "sender": "Jay",
            "text": "Is it one?",
        },
        {
            "sender": "Jay",
            "text": "Please explain",
        },
        {
            "sender": "AI",
            "text": "It is 2 for no reason.",
        }
    ],
    "docs": [
            """
            # 民法第1024條
            2^10 = 1024 
            """,
            """
            # 臺灣苗栗地方法院 112 年度司促字第 5565 號民事裁定
            一、債務人應向債權人連帶清償新臺幣115,324元，及如附表所示之利息、違約金，並連帶賠償督促程序費用新臺幣500元，否則應於本命令送達後20日之不變期間內，向本院提出異議。
二、債權人請求之原因事實：
            """
    ]
} 

c1 = chatroom(chat1["date"], chat1["chat_history"], chat1["docs"])
c2 = chatroom(chat2["date"], chat2["chat_history"], chat2["docs"])

chatData = [c2, c1]
for _ in range(10):
    chatData.append(c1)
