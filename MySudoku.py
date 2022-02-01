from tkinter import*
from tkinter.messagebox import showinfo
import random
import time
from PIL import ImageTk
import pygame
import threading
pygame.mixer.init()


def background_music():
    pygame.mixer.music.load("background_music.mp3")
    pygame.mixer.music.play()


def clear():
    global sudoku
    global valid
    global curtime
    global sudoku_canvas,st
    global timer_thread,name_text,name
    global stop_thread,button_Restart,button_NewGame,button_highest
    stop_thread = True
    time.sleep(.20)
    name.place(x=0,y=0,height=0,width=0)
    sudoku_canvas.delete(name_text)
    for i in range(9):
        for j in range(9):
            sudoku[i][j].config(bg="teal")
    for i in range(9):
        for j in range(9):
            E = sudoku[i][j]
            E.delete(0, END)
    sudoku_canvas.delete(curtime)
    st=""
    button_Restart.place(x=0, y=0, height=0, width=1)
    button_NewGame.place(x=550, y=100, height=50, width=200)
    button_highest.place(x=550, y=220, height=50, width=200)
    button_help.place(x=550, y=280, height=50, width=200)
    button_about.place(x=550, y=340, height=50, width=200)
    button_exit.place(x=550, y=400, height=50, width=200)
    sudoku_canvas.pack()

def Start():
    global sudoku
    global valid
    global curtime
    global sudoku_canvas
    global timer_thread,name,name_text
    global stop_thread,button_Restart,button_NewGame,highest
    stop_thread = False
    timer_thread=threading.Thread(target=timer)
    for i in range(9):
        for j in range(9):
            sudoku[i][j].config(bg="teal")
    for i in range(9):
        for j in range(9):
            E=sudoku[i][j]
            E.delete(0,END)

    make_puzzle()
    insert_value()
    button_NewGame.place(x=0, y=0, height=0, width=0)
    button_Restart.place(x=550, y=220, height=50, width=200)
    
    name.place(x=550,y=120,height=30,width=200)
    sudoku_canvas.delete(name_text)
    sudoku_canvas.pack()
    name_text=sudoku_canvas.create_text(600, 100, text="Name:" + st, font="Times 18 bold",
                                        fill="#ffffcc")
    sudoku_canvas.pack()
    button_help.place(x=0, y=3, height=0, width=0)
    button_highest.place(x=0, y=3, height=0, width=0)
    button_about.place(x=0, y=4, height=0, width=0)
    button_exit.place(x=0, y=5, height=0, width=0)
    sudoku_canvas.pack()
    timer_thread.start()

def timer():
    global curtime
    global timer_on,st
    sudoku_canvas.delete(curtime)
    curtime = sudoku_canvas.create_text(250, 500, text="Time: 00:00:00" , font="Times 18 bold",
                                        fill="#ffffcc")
    sudoku_canvas.pack()
    h=int(0);m=int(0);s=int(1)
    while 1:
        global stop_thread
        if stop_thread == True:
            sudoku_canvas.delete(curtime)
            time.sleep(1)
            break
        st=""
        if h<=9:
            st=st+"0"+str(h)
        else:
            st=st+str(h)
        if m<=9:
            st=st+":0"+str(m)
        else:
            st=st+":"+str(m)
        if s<=9:
            st=st+":0"+str(s)
        else:
            st=st+":"+str(s)
        time.sleep(1)
        sudoku_canvas.delete(curtime)
        curtime = sudoku_canvas.create_text(250, 500, text="Time:" + st, font="Times 18 bold",
                                        fill="#ffffcc")
        sudoku_canvas.pack()
        s+=1
        m=m+(s//60)
        h=h+(m//60)
        m=m%60
        s=s%60
    
        

def About():
    showinfo("About","This game has been developed by Md Imran Khan.")

def make_puzzle():
    global puzzle
    for i in range(9):
        for j in range(9):
            puzzle[i][j]=(i+j+1)%9
            if puzzle[i][j]==0:
                puzzle[i][j]=9

    for k in range(500):
        x=random.randrange(1,4)
        if x==1:
            swap_puzzle()
        elif x==2:
            swap_column()
        elif x==3:
            swap_row()
        else:
            rotate()
    empty_puzzle()


def empty_puzzle():
    global puzzle
    x=random.randrange(10,20)
    for k in range(x):
        i=random.randrange(0,9)
        j=random.randrange(0,9)
        while puzzle[i][j]!=0:
            puzzle[i][j]=0

def swap_row():
    global puzzle
    a=random.randrange(0,9)
    b=random.randrange(0,9)
    for j in range(9):
        c=puzzle[a][j]
        puzzle[a][j]=puzzle[b][j]
        
        puzzle[b][j]=c

def swap_column():
    global puzzle
    a=random.randrange(0,9)
    b=random.randrange(0,9)
    for j in range(9):
        c=puzzle[j][a]
        puzzle[j][a]=puzzle[j][b]
        puzzle[j][b]=c


def swap_puzzle():
    global puzzle
    a=random.randrange(1,10)
    b=random.randrange(1,10)
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==a:
                puzzle[i][j]=b
            elif puzzle[i][j]==b:
                puzzle[i][j]=-1
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==-1:
                puzzle[i][j]=a

def rotate():
    global puzzle
    cur=[]
    cur=puzzle
    for i in range(9):
        for j in range(9):
            puzzle[i][j]=cur[j][i]


def insert_value():
    global puzzle
    global sudoku
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==0:
                sudoku[i][j].config(bg="#93a3b8")
            else:
                sudoku[i][j].insert(0,str(puzzle[i][j]))
                sudoku[i][j].config(bg="teal")


def Submit():
    win=int(1)
    global sudoku
    global valid
    global puzzle
    flag=int(0)
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]!=0:
                sudoku[i][j].config(bg="teal")
                if str(puzzle[i][j])!=sudoku[i][j].get():
                    flag=1
                    sudoku[i][j].delete(0,END)
                    sudoku[i][j].insert(0,str(puzzle[i][j]))
    if flag==1:
        showinfo("Warning","Don't try to change the default values!\n")
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]==0:
                sudoku[i][j].config(bg="#93a3b8")
    for i in range(9):
        for j in range(9):
            s1=[]
            s2=[]
            if (sudoku[i][j].get()) not in valid:
                if puzzle[i][j] == 0:
                    sudoku[i][j].config(bg="pink")
            for k in range(9):
                if str(sudoku[i][k].get())  in s1:
                    if puzzle[i][k] == 0:
                        sudoku[i][k].config(bg="pink")
                    for f in range(9):
                        if sudoku[i][f].get()==sudoku[i][k].get():
                            if puzzle[i][f] == 0:
                                sudoku[i][f].config(bg="pink")
                if str(sudoku[k][j].get())  in s2:
                    if puzzle[k][j] == 0:
                        sudoku[k][j].config(bg="pink")
                    for f in range(9):
                        if sudoku[f][j].get() == sudoku[k][j].get():
                            if puzzle[f][j] == 0:
                                sudoku[f][j].config(bg="pink")
                s1.append(str(sudoku[i][k].get()))
                s2.append(str(sudoku[k][j].get()))

            s1=sorted(s1)
            s2=sorted(s2)
            if ''.join(s1)!="123456789" or ''.join(s2)!="123456789":
                win=int(0)
    if win==1:
        global stop_thread
        global curtime
        stop_thread = True
        f = open("scores.txt", "r+")
        scores =f.read().split(',')
        result = str(st)+" "+ name.get()+","
        scores.append(result)
        scores=sorted(scores)
        f.write(result)

        showinfo("Game Status","Congratulations!\nYou Won The Game\nTime: "+str(st))
        clear()
    else:
        showinfo("Game Status", "Sorry!\nIt is not solved yet!\n")

def highest():
    f = open("scores.txt", "r+")
    scores =f.read().split(',')
    scores=sorted(scores)
    res=""
    for i in range(min(len(scores),5)):
        res=res+scores[i]+"\n"
    showinfo("Highest Scores","Highest Scores:"+res)

def Help():
    showinfo("Help","You have to fill the empty boxes with correct numbers.\nThe numbers should be in the range of 1 - 9.\nAnd there should be no repeat of numbers in same column and same row.")

def Exit():
    exit()





root = Tk()
root.title("My Sudoku")
root.wm_iconbitmap("icon.ico")
background_music()
sudoku=[]
puzzle=[[0 for x in range(9)]for y in range(9)]
valid=["1","2","3","4","5","6","7","8","9"]
st=""
# create canvas
sudoku_canvas=Canvas(root,height=550,width=880,bg="#18332b")
root.resizable(height=False,width=False)
photo=ImageTk.PhotoImage(file='background_photo.png')
sudoku_canvas.create_image(0,0,image=photo,anchor=NW)
#creating initial grid
p=80
q=90
for i in range(9):
    l=[]
    for j in range(9):
        E = Entry(root,font="BOLD 28",bg="teal")
        E.grid(row=i,column=j)
        E.place(x=p,y=q,height=40,width=40)
        l.append(E)
        p+=41
    sudoku.append(l)
    q+=41
    p=80

name = Entry(root,font="BOLD 18",bg="teal")
name_text=sudoku_canvas.create_text(0,0,text="",font="Times 24 bold",fill="#ffffcc")
#creating buttons
button_NewGame = Button(root, text="New Game",font="Times 20 bold",bg="#1d1e26",foreground="#ffffcc",command=Start)
button_Solve = Button(root, text="Submit",font="Times 20 bold",bg="#1d1e26",foreground="#ffffcc",command=Submit)
button_Restart = Button(root, text="Restart",font="Times 20 bold",bg="#1d1e26",foreground="#ffffcc",command=clear)
button_highest = Button(root, text="Highest Scores",font="Times 20 bold ",bg="#1d1e26",foreground="#ffffcc",command=highest)
button_help = Button(root, text="Help",font="Times 20 bold ",bg="#1d1e26",foreground="#ffffcc",command=Help)
button_about = Button(root, text="About",font="Times 20 bold ",bg="#1d1e26",foreground="#ffffcc",command=About)
button_exit = Button(root, text="Exit",font="Times 20 bold ",bg="#1d1e26",foreground="#ffffcc",command=Exit)

button_NewGame.place(x=550, y=100, height=50, width=200)
button_Solve.place(x=550, y=160, height=50, width=200)
button_highest.place(x=550, y=220, height=50, width=200)
button_help.place(x=550, y=280, height=50, width=200)
button_about.place(x=550, y=340, height=50, width=200)
button_exit.place(x=550, y=400, height=50, width=200)

sudoku_canvas.create_text(400,40,text="My Sudoku",font="Times 24 bold ",fill="#ffffcc")
sudoku_canvas.pack()
#threading
stop_thread = False
timer_thread = 1
curtime=sudoku_canvas.create_text(270,500,text="",font="Times 24 bold",fill="#ffffcc")
sudoku_canvas.pack()

root.mainloop()
