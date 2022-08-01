from tkinter import *
from tkinter import filedialog as fd




root = Tk()
root.title("Anton V1.3 - EDITOR")
root.geometry("500x500")
myitem = Label(root,text="Anton V1.3 - EDITOR")
Label(text="    ").grid(row=0,column=0)
myitem.grid(row=0,column=1)
file1inp = Label(root,text="File 1")
file1inp.grid(row=1,column=0)
def selectfileone():
	file1 = fd.askopenfilename(filetypes=[("Video files","*.mp4")])
	file1inp.config(text="Selected")
selectfilebutton = Button(root,text="Select a file",command=selectfileone)
selectfilebutton.grid(row=2,column=0)



root.mainloop()

