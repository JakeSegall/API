from tkinter import *

root =Tk()


top_label = Label( root,text="News letter", bg="light blue",fg=
"black",font=("Helvetica", 20))
top_label.place(x=60,y=20)



def perform_convert():

    print("good job")

convert_btn=Button(root,text="      Enter         ", highlightbackground="#a9a9a9", command=perform_convert)
convert_btn.place(x=300,y=147)





long_course_input=Entry(root)
long_course_input.delete(0, END)
long_course_input.insert(0, "Enter Email")
long_course_input.place(x=60,y=150)


type_of_news = IntVar()
Radiobutton(root, text="Sports",  bg=("light blue"), variable=type_of_news, value="meters").place(x=60, y=210)
Radiobutton(root, text="COVID-19",  bg=("light blue"), variable=type_of_news, value="yards").place(x=60, y=230)
Radiobutton(root, text="Breaking News", bg=("light blue"), variable=type_of_news, value="High Contrast").place(x=60, y=250)


 
def showImg(self):
    load = Image.open('UCC.png') 
    render = ImageTK.PhotoImage(load)

    img = Label(Self, image=render)
    img.imgage = render
    img.place(x=300,y=300)

root.title("News Letter")
root.geometry("500x300")
root.configure(background='light blue')
root.mainloop()