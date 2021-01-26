from tkinter import *
from tkinter import ttk
import os
from tkinter import messagebox,filedialog
from pygame import mixer
from PIL import Image,ImageTk
tk = Tk()
tk.geometry(("600x500"))
tk.title("Music Player")
from mutagen.mp3 import MP3
tk.iconphoto(False,ImageTk.PhotoImage(file = os.path.join("Assests","Iocn.png")))
mixer.init()
class Main:
    def __init__(self):
        
        self.FileLength = 0
        self.value = 0
        self.flag = False
        self.volumeVlaue = 100
        self.songLength = 0
        self.scalePos = 0
        self.musicPos = 0
        self.newFlag = True
        self.innerFlag = True
        self.Draw()
    def reset(self):
        self.scalePos = 0
        self.musicPos = 0
        self.newFlag = True
        self.innerFlag = True
        self.value = 0
    def musicSearch(self,path):
        os.chdir(path)
        for root, dirs, files in os.walk('.'):
            for filename in files:
                if os.path.splitext(filename)[1] == ".mp3" or os.path.splitext(filename)[1] == ".wav" or os.path.splitext(filename)[1] == ".mp4a":
                    self.mylist.insert(END,os.path.join(root, filename))
    def new(self):
        try:
            self.reset()
            a = self.mylist.curselection()
            b = a[0]+1


            song = self.mylist.get(b)
            mixer.music.load(song)
            self.songLength=MP3(song).info.length
            self.scale.config(to=self.songLength)
            
            
            self.labelPlaying.config(text=f'{self.mylist.get(ACTIVE)}') 
            self.play()
            self.mylist.selection_clear(0,END)
            self.mylist.activate(b)
            self.mylist.selection_set(b)
        except Exception:
            pass
    def prev(self):
        self.reset()
        a = self.mylist.curselection()
        if a[0] >0 :
            b = a[0]-1

            song = self.mylist.get(b)
            mixer.music.load(song)
            self.songLength=MP3(song).info.length
            self.scale.config(to=self.songLength)
        
            self.labelPlaying.config(text=f'{self.mylist.get(ACTIVE)}') 
            self.play()
            self.mylist.selection_clear(0,END)
            self.mylist.activate(b)
            self.mylist.selection_set(b)
    def load(self,hi):
        
        # mixer.music.stop()
        self.reset()
        a=self.mylist.get(ACTIVE)
        mixer.music.load(a)
        mixer.music.set_volume(self.volumeVlaue/100)
        self.labelPlaying.config(text=f'{a}') 
        self.songLength=MP3(a).info.length
        self.scale.config(to=self.songLength)
        
        self.play()
        
    def play(self):
        self.reset()
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
            
            
            
            
        else:  # music paused
            self.Play.config(image=photoImg5)
            self.Play.photo = photoImg5
            
            mixer.music.unpause()
            self.value = 1
            
            
    def update(self):#For updating thevalue everysecond
        if mixer.music.get_busy():
             
            # self.a = mixer.music.get_pos()//1000
            # print(self.a,b)
            
            if self.newFlag:
                if self.innerFlag:
                       
                 
                    self.scale.set(mixer.music.get_pos()//1000)
                else:
                    self.musicPos += 0.5
                    
                    self.scale.set(int(self.musicPos))
               
            
            else:
                
                self.scale.set(self.scalePos)
                
                self.newFlag = True

        self.scale.after(500,self.update)
    
    def setVolume(self,a):
        self.volumeVlaue = self.volume.get()
        mixer.music.set_volume(self.volumeVlaue/100)      
    def release(self,a):
        self.scalePos = self.scale.get()
        
        self.musicPos = self.scalePos
        mixer.music.set_pos(int(self.scalePos))
       
        
        self.newFlag = False
        self.innerFlag = False
        

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
        Playing = Frame(tk,height=40,width=500)
        self.labelPlaying = Label(Playing,text="Double Click that music",font=("Courier",20,"bold"))
        self.labelPlaying.pack()
       
        Playing.pack()

        self.mylist = Listbox(MusicList, yscrollcommand = scrollbar.set,height=300,width=500,font=("Courier",15,"bold"),activestyle='none',bg="black",fg="white" )
        
        self.musicSearch(os.path.join("C:"))
        
        self.mylist.pack( side = RIGHT,fill = BOTH )
        self.mylist.bind("<Button-1>",self.load)
        # print(self.mylist)
        scrollbar.config( command = self.mylist.yview )
        playBar = Frame(tk)
        self.start = Label(playBar,text="00:00")
        self.finish = Label(playBar,text="00:00")
        self.start.grid(row=0,column=0)
        self.finish.grid(row=0,column=2)
        self.scale = ttk.Scale(playBar,orient=HORIZONTAL,length=300,from_=0,to=100,)
        self.scale.bind("<ButtonRelease-1>",self.release)
        self.scale.grid(row=0,column=1)
        playBar.pack()
        #Button Embadding
        ButtonWork = Frame(tk)
        
        self.Play = Button(ButtonWork,image=self.photoImg,command=self.play)
        self.Play.grid(row = 0,column = 1)
        Next = Button(ButtonWork,image=photoImg1,command = self.new)
        Next.grid(row = 0,column = 2)
        prev = Button(ButtonWork,image=photoImg2,command = self.prev)
        prev.grid(row = 0,column = 0)
        self.volume = Scale(ButtonWork,length=54,sliderlength = 10,bg="#15e8e1",command=self.setVolume)
        self.volume.set(self.volumeVlaue)
        self.volume.grid(row=0 ,column=3)
        Open = Button(ButtonWork,text="Open Folder",bg="#08a0cf",command=self.openFolder)
        Open.grid(row=0,column=4,ipady=15)
        ButtonWork.pack(pady=10)
        self.scale.after(1000,self.update)
        tk.after(100)
        tk.mainloop()
    
    def scaleSet(self):
        pass
    def openFolder(self):
        a = (filedialog.askdirectory())
        
        self.mylist.delete(0,END)
        
        self.musicSearch(a)

        
        
        
if __name__ == "__main__":

    Main()



