from tkinter import simpledialog, messagebox,Tk

if __name __=="__main__":
    window = Tk()
    window.withdraw()

    answer = simplsdialog.askstring(None, prompt=How old are you?)

    age = int(answer)
    yearborn = 2020 - age

    messagebox.showinfo(None, message=you were born in" + str(yearborn")