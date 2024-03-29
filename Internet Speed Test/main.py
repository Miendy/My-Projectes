import tkinter as tk
from tkinter import*
import speedtest

root = Tk()
root.title("Internet Speed Test")
root.geometry("360x600")
root.resizable(False, False)
root.configure(bg="#1a212d")

def start():
    test = speedtest.Speedtest()
    
    uploading = round(test.upload() / (1024 * 1024), 2)
    upload.configure(text=uploading)

    downloading = round(test.download() / (1024 * 1024), 2)
    download.configure(text=downloading)
    Download.configure(text=downloading)

    servernames = []
    test.get_servers(servernames)
    ping.configure(text=test.results.ping)


#icon
image_icon = PhotoImage(file="Internet Speed Test\logo.png")
root.iconphoto(False, image_icon)

#images
Top = PhotoImage(file="Internet Speed Test\jtop.png")
Label(root, image = Top, bg="#1a212d").pack()

Main = PhotoImage(file="Internet Speed Test\main.png")
Label(root, image = Main, bg="#1a212d").pack(pady=(40, 0))

button = PhotoImage(file="Internet Speed Test\jbutton.png")
Button = Button(root, image = button, bg="#1a212d", bd=0, activebackground="#1a212d", cursor="hand2", command = start)
Button.pack(pady=10)

#Label
Label(root, text="PING", font="arial 9 bold", bg="#1A212D", fg = "white").place(x=54, y=123)
Label(root, text="DOWNLOAD", font="arial 9 bold", bg="#1A212D", fg = "white").place(x=143, y=123)
Label(root, text="UPLOAD", font="arial 9 bold", bg="#1A212D", fg = "white").place(x=265, y=123)

Label(root, text="MS", font="arial 7 bold", bg="#384056", fg="white").place(x=62, y=80)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=165, y=80)
Label(root, text="MBPS", font="arial 7 bold", bg="#384056", fg="white").place(x=275, y=80)

Label(root, text="DOWNLOAD", font="arial 15 bold", bg="#384056", fg = "white").place(x=125, y=280)
Label(root, text="MBPS", font="arial 15 bold", bg="#384056", fg = "white").place(x=155, y=380) 


ping = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
ping.place(x=70, y=60, anchor="center")

download = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
download.place(x=180, y=60, anchor="center")

upload = Label(root, text="00", font="arial 13 bold", bg="#384056", fg="white")
upload.place(x=290, y=60, anchor="center")


Download = Label(root, text="00", font="arial 40 bold", bg="#384056", fg="white")
Download.place(x=185, y=350, anchor="center")

root.mainloop()
