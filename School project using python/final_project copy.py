
from tkinter import *

import tweepy
import webbrowser
import time

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

consumer_key = "Yr2w21j6wiZULiuAQAc6BsDJk"
consumer_secret = "eR3J2aYWn8vzvA3huuwZH17L97OKEHQYmWcxLWctPyHJAZUMV5"

auth = None
popup = None
api = None
MyStreamListener = None
user_list = ["CNN", "FoxNews", "globalnewsto", "jake14886732" ]

callback_uri = 'oob' 


root =Tk()

top_label = Label( root,text="News letter", bg="light blue",fg=
"black",font=("Helvetica", 20))
top_label.place(x=60,y=20)

def log_in_to_twitter():
    #makes the function use the global variable auth instead of creating a local one
    global auth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
    redirect_url = auth.get_authorization_url()

    webbrowser.open(redirect_url)

    popupmsg("Enter Twitter pin")

# convert_btn=Button(root,text= "Authenticate", highlightbackground="#a9a9a9", width = 10)
# convert_btn.place(x=300,y=147)

def popupmsg(msg):
    global popup
    popup = Tk()
    popup.wm_title("!")
    label = Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    text = Text(popup, width=10, height = 1)

    text.pack()
    B1 = Button(popup, text="Okay", command = lambda: twitter_authentication((text.get('1.0', END))))
    B1.pack()
    popup.mainloop()

def twitter_authentication(twitter_code):
    print("twitter_code", twitter_code)
    global MyStreamListener
    global type_of_news
    global popup
    popup.destroy()
    global auth
    global api
    global user_list
    target_user = ""
    auth.get_access_token(twitter_code)
    api = tweepy.API(auth)


    # try-catch exception to catch errors. 
    try:    
        print(type_of_news.get())
        tweets = api.user_timeline(screen_name=type_of_news.get(), count=1)
        target_user = str(tweets[0].user.id)
        
        MyStreamListener = MyStreamListener()
        MyStreamListener.this_user_id = target_user
        myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener)   
        myStream.filter(follow=[target_user], is_async=True)
    except:
        print("failed to get user timeline, exception thrown")


  
        



    #stream listener

class MyStreamListener(tweepy.StreamListener):
    this_user_id = ""
    def on_status(self, status):
        global email_text_content
        if status.user.id_str != self.this_user_id:
            return
        print(status.text)
        mail_content = status.text
        #The mail addresses and password
        sender_address = 'pythonnewsapp@gmail.com'
        sender_pass = 'Swimming123'
        receiver_address = email_text_content.get()
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'A new tweet has been posted by and account you follow'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'plain'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
        
    # myStream.filter(follow=[str()])

email_text_content = StringVar()
email_box=Entry(root, textvariable=email_text_content)
email_box.delete(0, END)
email_box.insert(0, "Enter Email")
email_box.place(x=60,y=150)


type_of_news = StringVar(value = "jake14886732")
Radiobutton(root, text="CNN",  bg=("light blue"), variable=type_of_news, value="CNN").place(x=60, y=210)
Radiobutton(root, text="FoxNews",  bg=("light blue"), variable=type_of_news, value="FoxNews").place(x=60, y=230)
Radiobutton(root, text="GlobalNewsToronto", bg=("light blue"), variable=type_of_news, value="globalnewsto").place(x=60, y=250)
Radiobutton(root, text="Me", bg=("light blue"), variable=type_of_news, value="jake14886732").place(x=60, y=270)


root.title("News Letter")
root.geometry("500x300")
root.configure(background='light blue')

def showImg(self):
    load = Image.open('UCC.png') 
    render = ImageTK.PhotoImage(load)

    img = Label(Self, image=render)
    img.imgage = render
    img.place(x=300,y=300)
    
#trying to close the listener
def destroy():  
    global popup
    global root
    global MyStreamListener
    if not MyStreamListener == None:del MyStreamListener
    print("destroy")
    if not popup == None: popup.destroy()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", destroy)
    
root.after(1000, log_in_to_twitter)

root.mainloop()


