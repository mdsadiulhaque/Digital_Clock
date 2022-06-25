# importing whole module

from tkinter import *
from tkinter.ttk import *

#import strftime

from time import strftime

#Called Clock

root = Tk()
root.title('SADIUL CLOCK') #Clock name


#display outputsize

def time():
	string = strftime('%H:%M:%S %p')
	lbl.config(text = string)
	lbl.after(1000, time)

#color code

lbl = Label(root, font = ('time new romans', 40, 'bold'),
			background = 'beige',
			foreground = 'black')

lbl.pack(anchor = 'center')
time()

mainloop()
