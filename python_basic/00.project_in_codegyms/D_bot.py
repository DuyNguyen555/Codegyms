import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as web
import os
from random import choice
from tkinter import *

accept_requests = choice(["Okay", "All right", "Ok, wait a minute"])

def send():
    """Hàm này để gửi tin nhắn"""
    createbot()
    entry = entry_chat.get("1.0",'end-1c').strip()
    
    query = entry.lower()
    entry_chat.delete("0.0",END)
    
    your_chat = query.capitalize()
    if "google" in query:
        chat.insert(END, "You: " + your_chat + '\n\n')
        open_google()

    elif "youtube" in query:
        chat.insert(END, "You: " + your_chat + '\n\n')
        open_youtube()
    
    elif query != '':
        chat.config(state=NORMAL)
        chat.insert(END, "You: " + query.capitalize() + '\n\n')
        chat.config(state=DISABLED)
        chat.yview(END)
        run(query)
        
def micro():
    """Hàm này để nói"""
    createbot()
    request = command().lower()
    chat.config(state=NORMAL)
    your_chat = request.capitalize()
    chat.insert(END, "You: " + your_chat + '\n\n')
    chat.config(state=DISABLED)
    chat.yview(END)
    run(request)

def createbot():
    """Hàm này để tạo ra công cụ giúp chuyển đổi văn bản thành giọng nói"""
    global dbot
    
    dbot = pyttsx3.init()
    voice = dbot.getProperty('voices')

    # Chọn giới tính của bot
    dbot.setProperty('voice', voice[1].id)

def speak_chatting(audio):
    """Hàm để con bot nói"""
    chat.config(state=NORMAL)
    chat.insert(END, "Bot: " + audio + '\n\n')
    chat.config(state=DISABLED)
    chat.yview(END)
    
    dbot.say(audio)
    dbot.runAndWait()
    
def command():
    """Hàm này để con bot nhận yêu cầu của bạn"""
    # Khởi tạo biến nhận yêu cầu
    receive_requests = sr.Recognizer()
    
    # Lấy giọng nói của mình
    with sr.Microphone() as source:
        # Dừng 1 giây trước khi có lệnh mới
        receive_requests.pause_threshold = 1
        audio = receive_requests.listen(source)

    try:
        # Tìm giọng nói tiếng anh
        query = receive_requests.recognize_google(audio, language="en")

    except:
        query = ""
        
    return query

def run(request):
    """Hàm này để chay bot"""

    if   "hi" in request: greeting()

    elif "hello" in request: greeting()
    
    elif "your name" in request: namebot()
    
    elif "who are you" in request: namebot()
    
    elif "you live" in request: you_live()

    elif "how do you do" in request: feel()

    elif "diana" in request: speak_chatting("Need anything?")

    elif "thank" in request: thank()
        
    elif "google" in request: search_google()

    elif "youtube" in request: search_youtube()
    
    elif "message" in request: open_zalo()
        
    elif "time" in request: time()
    
    elif "today" in request: today()
    
    elif "bye" in request: goodbye()
    
    elif "" in request: speak_chatting("Sorry, I don't know")


def greeting():
    """Hàm này để con bot chào bạn"""
    greet = choice(["Hi", "Hi there", "Hello", "Hey"])
    response = "How can I help you?"
    speak_chatting(greet)
    speak_chatting(response)
    
def goodbye():
    """Hàm này để con bot chào tạm biệt và tắt"""
    bye = choice(["Take care, have a good time", "See you later", 
                  "Catch you later", "See you soon", "See you next time"])
    speak_chatting(bye)
    quit()
    
def thank():
    """Khi bạn cám ơn bot, nó sẽ trả lời"""
    responding = choice(["You are welcome", "No problem"])
    speak_chatting(responding)
    
def namebot():
    """Hàm này để giới thiệu tên"""
    speak_chatting("My name is Diana")
    
def time():
    """Thời gian hiện tại"""
    speak_chatting(accept_requests)
    time_today = datetime.datetime.now().strftime("%I:%M %p")
    speak_chatting(time_today)

def today():
    """Ngày hiện tại"""
    speak_chatting(accept_requests)
    time_today = datetime.datetime.now().strftime("%B, %d, %Y")
    speak_chatting(time_today)
    
def you_live():
    speak_chatting("In a little space, I'm not sure")

def feel():
    speak_chatting("I'm doing well, thank you")
    
def search_google():
    """Hàm này để tìm kiếm trong google"""
    speak_chatting("What should I search for you ?")
    search = command().lower()
    speak_chatting(accept_requests)
    url = f"https://www.google.com/search?q={search}"
    web.get().open(url)
    
def open_google():
    """Hàm này để mở trong google"""
    speak_chatting(accept_requests)
    url = f"https://www.google.com"
    web.get().open(url)
    speak_chatting("Open Google Chrome")
    
def search_youtube():
    """Hàm này để tìm kiếm trên youtube"""
    speak_chatting("What should I search for you ?")
    search = command().lower()
    speak_chatting(accept_requests)
    url = f"https://www.youtube.com/search?q={search}"
    web.get().open(url)

def open_youtube():
    """Hàm này để mở trong google"""
    speak_chatting(accept_requests)
    url = f"https://www.youtube.com"
    web.get().open(url)
    

def open_zalo():
    """Hàm này để mở Zalo chat"""
    speak_chatting(accept_requests)
    zalo = r"C:\Users\Admin\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Zalo"
    os.startfile(zalo)


if __name__ == '__main__':

    display = Tk()
    display.geometry("600x700")
    display.title("Chat Bot")
    display.resizable(width=FALSE, height=FALSE)
    display.configure(bg="black")

    # Tạo thanh trượt
    scroll_bar = Scrollbar(display, cursor="circle", orient=VERTICAL)
    
    # Tạo khung trò chuyện
    chat = Text(display, font="Arial 20 bold", width=37, height=18, insertwidth=3, 
                bd=10, cursor="circle", yscrollcommand=scroll_bar.set, bg="skyblue")
    
    # Tạo nút để gữi tin nhắn
    send_button = Button(display, text="SEND", font="Arial 10 bold",width=5, height=2, bd=10, bg="aqua", command=send, cursor="circle")

    # Tạo khung để nhập
    entry_chat = Text(display, font="Arial 15 bold",width=38, height=2, bd=10, insertwidth=3,cursor="heart", bg="#6666FF")
    
    # Tạo nút micro
    micro_button = Button(display, text="MICRO", font="Arial 10 bold",width=5, height=2, bd=10, bg="#CCFFFF", command=micro, cursor="circle")
    
    chat.place(x=4, y=4)
    scroll_bar.config(command=chat.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)
    send_button.place(x=4, y=620)
    entry_chat.place(x=72, y=615)
    micro_button.place(x=515, y=620)

    display.mainloop()
    