import subprocess
from tkinter.filedialog import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

def vidDownload():
    #the -s is just for testing remove to actually download the video
    cmd = "youtube-dl -s -f bestvideo+bestaudio -o "
    directory = f_path.get()

    if directory == "Select a Download Location " or directory == '':
        messagebox.showerror("Error!", "Please choose a valid Directory!")
    else:

        Label(app, text="Downloading!").grid()

        try:
            subprocess.check_call(cmd + directory + "\%(title)s.%(ext)s " + link.get())
            Label(app, text="Complete!").grid(column="1")

        except subprocess.CalledProcessError:
            #print(err) # debugging purposes only
            messagebox.showerror("Error!","Please specify a valid Youtube URL")

def browse():
    global f_path
    directory = askdirectory()
    f_path.set(directory)

#Start of Program
app = Tk()
app.title("Youtube-dl GUI")
app.geometry("450x125")

#Download Location
f_path = StringVar()
f_path.set("Select a Download Location ")
Label(app,text="Download Location:").grid(column="1")
Entry(app, textvariable=f_path, state="readonly",width="50").grid(column="1",padx='20',pady='2')
Button(app, text="Browse", command=browse).grid(column="2", row="1")

#Url
Label(app, text="Video Url:").grid(column="1",row="2")
link = Entry(app, text="Url..",width="50")
link.grid(column="1",row="3")

#Download Button
Button(app, text="Download", command=vidDownload).grid(column="2",row="3")

app.mainloop()


'''
https://www.youtube.com/watch?v=v1GhTjuCyrg
'''
