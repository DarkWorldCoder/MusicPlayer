from tkinter import *
import os
from tkinter import messagebox,filedialog
from pygame import mixer
from PIL import Image,ImageTk
tk = Tk()
tk.geometry(("900x500"))
tk.title("Music Player")
from mutagen.mp3 import MP3
tk.iconphoto(False,ImageTk.PhotoImage(file = os.path.join("Assests","Iocn.png")))
mixer.init()
class Main:
    def __init__(self):
        
        self.FileLength = 0
        self.value = 0
        self.flag = False
        self.slider_value = DoubleVar()
        self.Draw()
       
        


    def musicSearch(self,path):
        os.chdir(path)
        for root, dirs, files in os.walk('.'):
            for filename in files:
                if os.path.splitext(filename)[1] == ".mp3":
                    self.mylist.insert(END,os.path.join(root, filename))
    
    def load(self,hi):
        
        # mixer.music.stop()
        self.value = 0
        mixer.music.load(self.mylist.get(ACTIVE)) 
        self.play()
    def play(self):
        
        


        
        img1 = Image.open(os.path.join("Assests","Pause.png"))
        img1 = img1.resize((50,50), Image.ANTIALIAS)
        photoImg5 =  ImageTk.PhotoImage(img1)
        
        
        
        
        
        if self.value == 0 :  # music not started
            
            self.Play.config(image=photoImg5)
            self.Play.photo = photoImg5
            mixer.music.play()
            self.value =  1
            return
            
            
            
            
            
            
        
        if self.value == 1: 
            
            self.Play.config(image=self.photoImg)
            self.Play.photo = self.photoImg
             # music playing
            mixer.music.pause()
            self.value = 2
            print(mixer.music.get_pos())
            
            
            
        else:  # music paused
            self.Play.config(image=photoImg5)
            self.Play.photo = photoImg5
            
            mixer.music.unpause()
            self.value = 1
            
            

            
    def Draw(self):
        #Play
        
        img = Image.open(os.path.join("Assests","Play.png"))
        img = img.resize((50,50), Image.ANTIALIAS)
        self.photoImg =  ImageTk.PhotoImage(img)
        #Next
        img1 = Image.open(os.path.join("Assests","Next.png"))
        img1 = img1.resize((50,50), Image.ANTIALIAS)
        photoImg1 =  ImageTk.PhotoImage(img1)
        #Prev
        
        
        img2 = Image.open(os.path.join("Assests","Next.png"))
        rotateImage2 = img2.rotate(180)
        rotateImage2 = rotateImage2.resize((50,50), Image.ANTIALIAS)
        photoImg2 =  ImageTk.PhotoImage(rotateImage2)
        
        
        #MusicLister and scroll bar
        MusicList = Frame(tk,height=300,width=500,bg="black")
        MusicList.pack()
        MusicList.pack_propagate(False)
        scrollbar = Scrollbar(MusicList)
        scrollbar.pack( side = RIGHT, fill = Y )
        

        self.mylist = Listbox(MusicList, yscrollcommand = scrollbar.set,height=300,width=500,font=("Courier",15,"bold"),activestyle='none',bg="black",fg="white" )
        
        self.musicSearch(os.path.join("C:"))
        
        self.mylist.pack( side = RIGHT,fill = BOTH )
        self.mylist.bind("<Button-1>",self.load)
        # print(self.mylist)
        scrollbar.config( command = self.mylist.yview )
    
        self.scale = Scale(tk,orient=HORIZONTAL,length=300,sliderlength=10,relief=GROOVE)
        
        self.scale.pack()
        #Button Embadding
        ButtonWork = Frame(tk)
        
        self.Play = Button(ButtonWork,image=self.photoImg,command=self.play)
        self.Play.grid(row = 0,column = 1,padx=10)
        Next = Button(ButtonWork,image=photoImg1)
        Next.grid(row = 0,column = 2,padx=10)
        prev = Button(ButtonWork,image=photoImg2)
        prev.grid(row = 0,column = 0,padx=10,)
        Open = Button(ButtonWork,text="Open Folder",bg="#08a0cf",command=self.openFolder)
        Open.grid(row=0,column=3,ipady=15)
        ButtonWork.pack(pady=10)
        tk.mainloop()
    def openFolder(self):
        a = (filedialog.askdirectory())
        
        self.mylist.delete(0,END)
        
        self.musicSearch(a)

        
        
        
        



Main()



