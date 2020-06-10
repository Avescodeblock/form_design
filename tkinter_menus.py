import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox



filename = ""


def close_file():
    textArea.delete('1.0', tk.END)

def save_file_as():
    try:
        save_text_as = filedialog.asksaveasfile(mode="w", defaultextension = ".txt")
        if save_text_as:
            text_area = textArea.get("1.0", "end - 1c")
            save_text_as.write(text_area)
            save_text_as.close()
            messagebox.showinfo("success", "file saved")
        else:
            messagebox.showinfo("error", "no file open")
    except:
        messagebox.showinfo("error", "no name typed")


def save_file():
    global filename
    try:
        if filename:
            text_area = textArea.get("1.0","end - 1c")
            save_text = open (filename,"w")
            save_text.write(text_area)
            save_text.close()
            messagebox.showinfo("success","file saved")
        else:
            messagebox.showinfo("error", "no file open")
    except:
        messagebox.showinfo("error", "not saved")



def parseline(line):
    parse_line = line.strip()
    space_pos = parse_line.rfind(" ")

    new_text_line = parse_line[space_pos:] + " " + parse_line[:space_pos]
    return new_text_line.strip()


def open_file():
    global filename
    print("open file")
    filename = filedialog.askopenfilename(initialdir="/", title="Open file",
                                          filetypes=(("Text files", ".txt"), ("All files", ".*")))
    try:
        # if filename:
        #     the_file = open(filename)
        #     textArea.delete('1.0',tk.END)
        #     textArea.insert(tk.END, the_file.read())
        # elif filename =="":
        #     messagebox.showinfo("you clicked cancel")
        if filename:
            the_file = open(filename)
            for line in the_file.readlines():
                textline = parseline(line)
                textArea.delete('1.0', tk.END)
                textArea.insert(tk.END, textline + "\n")
            the_file.close()

    except:
        messagebox.showinfo("error", "could not open file")
        print(filename)


form = tk.Tk()
form.title("menus")

menubar = tk.Menu(form)
fileMenuItem = tk.Menu(menubar, bg="red", tearoff=0, fg="white")
editMenuItem = tk.Menu(menubar, bg="green", tearoff=0, fg="cyan")

fileMenuItem.add_command(label="open", command=open_file)
fileMenuItem.add_command(label="save", command=save_file)
fileMenuItem.add_command(label="save as", command=save_file_as)
fileMenuItem.add_command(label="close", command=close_file)
fileMenuItem.add_command(label="quit", command=form.quit())

fileMenuItem.add_separator()

editMenuItem.add_command(label="cut", command=open_file)
editMenuItem.add_command(label="copy", command=open_file)
editMenuItem.add_command(label="paste", command=open_file)
editMenuItem.add_command(label="rename", command=open_file)

menubar.add_cascade(label="file", menu=fileMenuItem)
menubar.add_cascade(label="edit", menu=editMenuItem)

form.config(menu=menubar)

textArea = tk.Text(form, height=12, width=80, wrap=tk.NONE)

textArea.insert(tk.END, "this is the default text")

textArea.configure(font=("Ariel", 14, "bold", "italic"))

scrollV = tk.Scrollbar(form, orient=tk.VERTICAL)
scrollV.config(command=textArea.yview)
textArea.configure(yscrollcommand=scrollV.set)
scrollV.pack(side=tk.RIGHT, fill=tk.Y)

scrollH = tk.Scrollbar(form, orient=tk.HORIZONTAL)
scrollH.config(command=textArea.xview)
textArea.configure(xscrollcommand=scrollH.set)
scrollH.pack(side=tk.BOTTOM, fill=tk.X)

textArea.pack()

form.mainloop()