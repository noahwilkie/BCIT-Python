import subprocess
from tkinter.filedialog import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from os import path
import os

#   Function that downloads the video with audio
def video_dl():
    save_history()
    cmd = "youtube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 -o "
    directory = f_path.get()

    if directory == "Select a Download Location " or directory == '':
        messagebox.showerror("Error!", "Please choose a valid Directory!")
    else:

        ''' figure out why this isnt working
        vidLabel=Label(app, text="Downloading!")
        vidLabel.grid(column=1,row=4)
        '''
        try:
            subprocess.check_call(cmd + directory + "\%(title)s.%(ext)s " + link.get(),cwd="src/")
            messagebox.showinfo("Complete","Download Complete!")

        except subprocess.CalledProcessError:
        #except Exception:
            messagebox.showerror("Error!","Please specify a valid Youtube URL")
            #vidLabel.destroy()

#   Function that only downloads the audio of the video
#   (e.i. used to download music that you own the rights to *winky face*)
def audio_dl():
    cmd = "youtube-dl -f bestaudio[ext=m4a]/m4a -o "
    directory = f_path.get()

    if directory == "Select a Download Location " or directory == '':
        messagebox.showerror("Error!", "Please choose a valid Directory!")
    else:
        '''
        #figure out why this pops up after
        audioL = Label(app, text="Downloading!")
        audioL.grid(column=1,row=4)
        '''
        try:
            subprocess.check_call(cmd + directory + "\%(title)s.%(ext)s " + link.get())
            messagebox.showinfo("Complete", "Download Complete!")

        except subprocess.CalledProcessError:
            messagebox.showerror("Error!", "Please specify a valid Youtube URL")
            #audioL.destroy()

#   Function to save the download location
def save_location():
    if cb.get() == "1":
        if f_path.get() == "Select a Download Location ":
            messagebox.showerror("Error!", "Please select a location before saving")
            cb.set("0")
        else:
            file = open("src/location.txt","w")
            file.write(f_path.get())
            cb.set("1")
            file.close()
    else:
        os.remove("src/location.txt")
        cb.set("0")

#   Function used to save the download history
def save_history():
    history_len()
    history_f=open("src/history.txt","a+")
    history_f.write("%s\n"%link.get())
    history_f.close()

#   Func used to get the history from history.txt
def read_history(file):
    history_len()
    if path.exists(file):
        history=[]
        history_f=open(file)
        for line in history_f:
            history.append(line.strip())
        history_f.close()
        return history
    else:
        history = open("src/history.txt", "w+")
        history.close()

#   Function to check the length of the history and if its to big it deletes the file
def history_len():
    count = 0
    count_f=open("src/history.txt")
    for line in count_f.readlines():
        count += 1
    count_f.close
    if count >= 30:
        print(count)
        os.remove("src/history.txt")

#   function to browse for download directory
def browse():
    global f_path
    directory = askdirectory()
    f_path.set(directory)

#   Start of Program
app = Tk()
app.title("Youtube Downloader")
app.geometry("600x125")

#Download Location
Label(app,text="Download Location:").grid(column="1")
f_path = StringVar()
f_path.set("Select a Download Location ")
Entry(app, textvariable=f_path, state="readonly",width="53").grid(column="1",padx='20',pady='2')

#   Browse button
Button(app, text="Browse", command=browse,width=15).grid(column="2", row="1")

#   Url stuff
Label(app, text="Video Url:").grid(column="1",row="2")

#   Checks to see if the history file exists and creates it if it isnt present
if path.exists("src/history.txt"):
    history = read_history("src/history.txt")
else:
    history = []
    history_f = open("src/history.txt", "w")
    history_f.close()

#   Combobox for url entry
link = Combobox(app, text="Url..",width="50",values=history)
link.grid(column="1",row="3")

#    Video download button
Button(app, text="Download Video", command=video_dl,width=15).grid(column="2",row="3")

#   Audio download button
Button(app, text="Download Audio", command=audio_dl,width=15).grid(column="3",row="3")

#   Save download location
cb = StringVar()
cb.set("0")
Checkbutton(app,text="Save Location",variable=cb,comman=save_location).grid(column=3,row=1)

#   Checks to see if location.txt exists
if path.exists("src/location.txt"):
    cb.set("1")
    cb_f = open("src/location.txt")
    for line in cb_f:
        f_path.set(line)
    cb_f.close()
else:
    cb.set("0")

#   Notice message to the user
Label(app, text="Program will freeze during download, don't panic & be patient").grid(column=1,row=5)

app.mainloop()
