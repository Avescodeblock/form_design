import tkinter as tk
# tk is a varible & tkinter is the value

form = tk.Tk()
form.title("my form")
myLabel = tk.Label(form, text = "toba doko ma lole \n bye bye!!! marlian ",
                   bg = "cyan", fg = "purple", font = "Ariel 24 bold italic",width = 5, height = 5)
myLabel2 = tk.Label(form, text = "Eyin omo instagram \n eyin lema pa mi!!!! ", width = 55, height = 5,
                     bg = "pink", fg = "blue", font = "Ariel 20 bold")
myLabel2.pack()
myLabel.pack() #the pack() is called a layout manager

form.mainloop() #last line : displays the box other lines above draws&design












