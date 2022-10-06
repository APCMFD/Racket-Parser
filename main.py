Solution::::

import tkinter as tk
window = tk.Tk()
window.geometry("600x350")
window.title("SOS Game")
window.configure(bg="white")
tk.Label(text="SOS", font=('Arial', 12, 'bold'), bg="white").place(x=145, y=7)
SELECT = tk.IntVar()
SELECT.set(2)
tk.Radiobutton(text="Simple game", variable=SELECT, value=2, font=('Arial', 12, 'bold'), selectcolor="silver", bg="white", activebackground="white").place(x=190, y=5)
tk.Radiobutton(text="General game", variable=SELECT, value=3, font=('Arial', 12, 'bold'), selectcolor="silver", bg="white", activebackground="white").place(x=330, y=5)
SELECT_1 = tk.IntVar()
SELECT_1.set(2)
tk.Label(text="Blue Player", font=('Arial', 12, 'bold'), bg="white").place(x=10, y=80)
tk.Radiobutton(text="S", variable=SELECT_1, value=2, font=('Arial', 12, 'bold'), selectcolor="silver", bg="white", activebackground="white").place(x=30, y=120)
tk.Radiobutton(text="O", variable=SELECT_1, value=3, font=('Arial', 12, 'bold'), selectcolor="silver", bg="white", activebackground="white").place(x=30, y=140)
SELECT_2 = tk.IntVar()
SELECT_2.set(2)
tk.Label(text="Red Player", font=('Arial', 12, 'bold'), bg="white").place(x=470, y=80)
tk.Radiobutton(text="S", variable=SELECT_2, value=2, font=('Arial', 12, 'bold'), selectcolor="silver", bg="white", activebackground="white").place(x=490, y=120)
tk.Radiobutton(text="O", variable=SELECT_2, value=3, font=('Arial', 12, 'bold'), selectcolor="silver", bg="white", activebackground="white").place(x=490, y=140)
### CREATE BOX START ###
X = 160
for i in range(8):
tk.Frame(window, bg="white", width=35, height=30, highlightthickness=1, highlightbackground="black", highlightcolor="black").place(x=X, y=50)
X += 34
X = 160
for i in range(8):
tk.Frame(window, bg="white", width=35, height=30, highlightthickness=1, highlightbackground="black", highlightcolor="black").place(x=X, y=79)
X += 34
X = 160
for i in range(8):
tk.Frame(window, bg="white", width=35, height=30, highlightthickness=1, highlightbackground="black", highlightcolor="black").place(x=X, y=108)
X += 34
X = 160
for i in range(8):
tk.Frame(window, bg="white", width=35, height=30, highlightthickness=1, highlightbackground="black", highlightcolor="black").place(x=X, y=137)
X += 34
X = 160
for i in range(8):
tk.Frame(window, bg="white", width=35, height=30, highlightthickness=1, highlightbackground="black", highlightcolor="black").place(x=X, y=166)
X += 34
X = 160
for i in range(8):
tk.Frame(window, bg="white", width=35, height=30, highlightthickness=1, highlightbackground="black", highlightcolor="black").place(x=X, y=195)
X += 34
X = 160
for i in range(8):
tk.Frame(window, bg="white", width=35, height=30, highlightthickness=1, highlightbackground="black", highlightcolor="black").place(x=X, y=224)
X += 34
X = 160
for i in range(8):
tk.Frame(window, bg="white", width=35, height=30, highlightthickness=1, highlightbackground="black", highlightcolor="black").place(x=X, y=253)
X += 34
### CREATE BOX END ###
tk.Label(text="Current turn: blue (or red)", font=('Arial', 12, 'bold'), bg="white").place(x=190, y=300)
window.mainloop()
