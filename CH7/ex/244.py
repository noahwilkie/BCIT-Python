from tkinter import *
import pygame.mixer

def play_correct_sound():
    number_correct.set(number_correct.get() + 1)
    correct_s.play()
def play_wrong_sound():
    number_wrong.set(number_wrong.get() + 1)
    wrong_s.play()

app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')

sounds = pygame.mixer
sounds.init()

correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

number_correct = IntVar()
number_correct.set(0)

number_wrong = IntVar()
number_wrong.set(0)


b1 = Button(app, text = "Correct!", width = 10, command = play_correct_sound)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text = "Wrong!", width = 10, command = play_wrong_sound)
b2.pack(side = 'right', padx = 10, pady = 10)

lab = Label(app, text='When you are ready, click on the buttons!', height=3)
lab.pack()

lab1 = Label(app, textvariable = number_correct)
lab1.pack(side='left')

lab2 = Label(app, textvariabl = number_wrong)
lab2.pack(side='right')

app.mainloop()
