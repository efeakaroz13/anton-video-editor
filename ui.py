from tkinter import *
from tkinter import filedialog as fd
import functions
from tkinter import messagebox, Tk

myeditor = functions.Editor("Anton")

root = Tk()
def alert(title, message="", kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)
root.title("Anton V1.3 - EDITOR")
root.geometry("500x500")
myitem = Label(root,text="Anton V1.3 - EDITOR")
Label(text="    ").grid(row=0,column=0)
myitem.grid(row=0,column=1)
file1inp = Label(root,text="File 1")
file1inp.grid(row=1,column=0)
filesx = []
def selectfileone():
    file1 = fd.askopenfilename(filetypes=[("Video files","*.mp4")])
    tempfile1 = str(file1)
    filesx.insert(0,tempfile1)
    file1inp.config(text="Selected")
    alert(str(filesx))
selectfilebutton = Button(root,text="Select a file",command=selectfileone)
selectfilebutton.grid(row=2,column=0)

def compressfile():
    myeditor.compress(filesx[0])
compressbtn = Button(text="Compress",command=compressfile)
compressbtn.grid(row=3,column=0)
root.mainloop()

