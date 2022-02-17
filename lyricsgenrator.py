from tkinter import *
from lyrics_extractor import SongLyrics
 

def get_lyrics():
    extract_lyrics = SongLyrics("GCS_API_KEY", "GCS_ENGINE_KEY")
    temp=extract_lyrics.get_lyrics(str(e.get()))
    res=temp['lyrics']
    result.set(res)
    
    
master=Tk()
master.geometry("650x750")
master.title("Lyrics Extractor")
master.configure(bg='light blue')
result=StringVar()
Label(master, text="Lyrics Generator",bg="light blue", font="comicsansms 18 bold", justify=CENTER, pady=15, padx=20).grid(row=0, column=1)
Label(master, text="Enter Song name : ",
      bg="cyan",font="comicsansms 13 bold",width=20).grid(row=1, sticky=W)

Label(master, text="Result :",
      bg="cyan",font="comicsansms 13 bold",width=20).grid(row=4, sticky=W)
Label(master, text="", textvariable=result,
      bg="light blue").grid(row=5, column=1)
e = Entry(master, width=50)
e.grid(row=1, column=1)
 
# creating a button using the widget
b = Button(master, text="Show",
           command=get_lyrics, bg="White")
 
b.grid(row=1, column=2, columnspan=2,
       rowspan=2, padx=5, pady=5,)
 
mainloop()
