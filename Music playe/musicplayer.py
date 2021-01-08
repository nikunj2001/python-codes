def volumeup():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol+.05)
    ProgressbarVolumeLabel.configure(text="{}".format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100


def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol-.05)

    ProgressbarVolumeLabel.configure(text="{}".format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100
def stopMusic():
    mixer.music.stop()
    ProgressbarMusicLabel.grid_remove()


    AudioStatusLabel.configure(text="Music Stopped")

def musicurl():
    try:
        dd=filedialog.askopenfilename(initialdir="C:/Users/vnind/OneDrive/Desktop/songs",
        title="Select Audio File",
        filetype=(("MP3","*.mp3"),("WAV","*.wav")))
    except:
        dd=filedialog.askopenfilename(title="Select Audio File",
        filetype=(("MP3","*.mp3"),("WAV","*.wav")))
    audiotrack.set(dd)
    

def muteMusic():
    global currentVol
    currentVol=mixer.music.get_volume()
    mixer.music.set_volume(0)
    root.muteButton.grid_remove()
    root.unmuteButton.grid()
    AudioStatusLabel.configure(text="Music Muted")

def unmuteMusic():
    global currentVol
    mixer.music.set_volume(currentVol)

    root.unmuteButton.grid_remove()
    root.muteButton.grid()
def pause():
    mixer.music.pause()
    root.PauseButton.grid_remove()
    root.ResumeButton.grid()
    AudioStatusLabel.configure(text="Music Paused")

def resumeMusic():
    root.ResumeButton.grid_remove()

    root.PauseButton.grid()
    mixer.music.unpause()

def playMusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    mixer.music.play()
    mixer.music.set_volume(.4)
    ProgressbarVolume["value"]=40
    ProgressbarVolumeLabel["text"]="40%"
    ProgressbarMusicLabel.grid()


    AudioStatusLabel.configure(text="Playing...")
    ProgressbarLabel.grid()
    root.muteButton.grid()
    song=MP3(ad)
    totalSongLength=int(song.info.length)
    ProgressbarMusic['maximum']=totalSongLength
    ProgressbarMusicEndTimeLabel.configure(text=f'{str(datetime.timedelta(seconds=totalSongLength))}')
    def ProgressbarMusictick():
        CurrentSongLength= mixer.music.get_pos()//1000
        ProgressbarMusic['value']=CurrentSongLength
        ProgressbarMusicStartTimeLabel.configure(text=f'{str(datetime.timedelta(seconds=CurrentSongLength))}')
        ProgressbarMusic.after(2,ProgressbarMusictick)
    ProgressbarMusictick()
    
def createwidthes():
    global imbrowse,ResumeButton,muteButton,unmuteButton, AudioStatusLabel, ProgressbarVolumeLabel, ProgressbarLabel, ProgressbarVolume,ProgressbarMusicLabel,ProgressbarMusic,ProgressbarMusicEndTimeLabel,ProgressbarMusicStartTimeLabel

    # Image registration
    implay=PhotoImage(file="play.png")
    impause=PhotoImage(file="pause.png")
    imbrowse=PhotoImage(file="browsing.png")
    imvolumeup=PhotoImage(file="volume-up.png")
    imvolumedown=PhotoImage(file="volume-down.png")
    # Size change of images
    imbrowse=imbrowse.subsample(1,1)
    implay=PhotoImage(file="play.png")
    implay=PhotoImage(file="play.png")
    implay=PhotoImage(file="play.png")
    # Label-1
    TrackLabel=Label(root,text="Select Audio Track : ",bg="lightskyblue",font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)


    # Audio status label
    AudioStatusLabel=Label(root,text="",bg="lightskyblue",font=('arial',15,'italic bold'),width=20)
    AudioStatusLabel.grid(row=2,column=1)

    # /Label-2
    TrackLabelentry = Entry(root,font=('arial',15,'italic bold'),width=35,textvariable=audiotrack)
    TrackLabelentry.grid(row=0,column=1,padx=20,pady=20)
    BrowseButton = Button(root,text='Search',bg='deeppink',font=('arial',15,'italic bold'),width=20,bd=5,
    activebackground='purple',command=musicurl)
    BrowseButton.grid(row=0,column=3,padx=20,pady=20)


    # Play Botton
    PlayButton = Button(root,text='Play',bg='green2',font=('arial',15,'italic bold'),width=20,bd=2,
    activebackground='white',command=playMusic)
    PlayButton.grid(row=1,column=0,padx=20,pady=20)

    # PauseButton
    root.PauseButton = Button(root,text='Pause',bg='yellow2',font=('arial',15,'italic bold'),width=20,bd=2,
    activebackground='white',command=pause)
    root.PauseButton.grid(row=1,column=1,padx=20,pady=20)
    
    # REsume button
    root.ResumeButton = Button(root,text='Resume',bg='yellow2',font=('arial',15,'italic bold'),width=20,bd=2,
    activebackground='white',command=resumeMusic)
    root.ResumeButton.grid(row=1,column=1,padx=20,pady=20)
    root.ResumeButton.grid_remove()
    # StopButton
    VolumeUp = Button(root,text='VolumeUp',bg='blue2',font=('arial',15,'italic bold'),width=20,bd=2,
    activebackground='white',command=volumeup)
    VolumeUp.grid(row=1,column=3,padx=20,pady=20)

    # stop
    Stop = Button(root,text='Stop',bg='red',font=('arial',15,'italic bold'),width=20,bd=2,
    activebackground='white',command=stopMusic)
    Stop.grid(row=2,column=0,padx=20,pady=20)

    # VolumeDown
    VolumeDown = Button(root,text='VolumeDown',bg='blue2',font=('arial',15,'italic bold'),width=20,bd=2,
    activebackground='white',command=volumedown)
    VolumeDown.grid(row=2,column=3,padx=20,pady=20)

    root.muteButton=Button(root,text="Mute",width=10,bg="yellow",activebackground="red2",bd=5,command=muteMusic)
    root.muteButton.grid(row=3,column=3)
    root.muteButton.grid_remove()
    root.unmuteButton=Button(root,text="UnMute",width=10,bg="yellow",activebackground="red2",bd=5,command=unmuteMusic)
    root.unmuteButton.grid(row=3,column=3)
    root.unmuteButton.grid_remove()    
    # PRGOGRESS BAR VOLUME
    ProgressbarLabel=Label(root,text="",bg="red")
    ProgressbarLabel.grid(row=0,column=4,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove();

    ProgressbarVolume=Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate',value=0,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)

    ProgressbarVolumeLabel = Label(ProgressbarLabel,text="0%",bg='lightgray',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)

    # PRogres BAr of music
    ProgressbarMusicLabel= Label(root,text="",bg="red")
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=4,padx=20,pady=20)


    ProgressbarMusicStartTimeLabel= Label(ProgressbarMusicLabel,text="0:00:00",bg="red",width=10)
    ProgressbarMusicStartTimeLabel.grid(row=0,column=0)


    # ProgressbarMusicLabel= Label(root,text="",bg="red")
    # ProgressbarMusicLabel.grid(row=3,column=4,columnspan=3,padx=20,pady=20)
    ProgressbarMusic=Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,mode="determinate",value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=370,ipady=3)
    ProgressbarMusicLabel.grid_remove()

    ProgressbarMusicEndTimeLabel= Label(ProgressbarMusicLabel,text="0:00:00",bg="red")
    ProgressbarMusicEndTimeLabel.grid(row=0,column=2)







from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3 

root = Tk()
root.geometry('1100x500+200+50')
root.title("Music Player")
root.iconbitmap('bg.ico')
root.resizable(False,False)
root.configure(bg='lightskyblue')
# ###########################
audiotrack=StringVar()
currentVol=0
totalSongLength=0
count=0
text=""
ss="Developed by nikunj Gupta"


# SLIDER 

SliderLabel = Label(root,text=ss,bg='lightskyblue',font=('arial',35,'italic bold'))
SliderLabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTrick():
    global count,text
    if(count>=len(ss)):
        count=-1
        text=""
        SliderLabel.configure(text=text)
    else:
        text+=ss[count]
        SliderLabel.configure(text=text)
    count+=1
    SliderLabel.after(200,IntroLabelTrick)

IntroLabelTrick()
mixer.init()
createwidthes()
root.mainloop()



