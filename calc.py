from tkinter import *
from tkinter import font as tkFont  # for convenience

r = ''
c = 0
v = 100
p = ''
san1 = 0
san2 = 0
u = ''


def add():
    global san1, r, u, p
    san1 = int(r)
    r = ''
    p = str(san1)+'+'
    label['text'] = str(san1)+'+'
    u = '+'


def ayyr():
    global san1, r, u, p
    san1 = int(r)
    r = ''
    p = str(san1)+'-'
    label['text'] = str(san1)+'-'
    u = '-'


def kopelt():
    global san1, r, u, p
    san1 = int(r)
    r = ''
    p = str(san1)+'*'
    label['text'] = str(san1)+'*'
    u = '*'


def bol():
    global san1, r, u, p
    san1 = int(r)
    r = ''
    p = str(san1)+'/'
    label['text'] = str(san1)+'/'
    u = '/'


def but(s):
    global r, san1, p
    r = r+s
    if san1 == 0:
        label['text'] = str(san1+int(r))
    else:
        label['text'] = p+r


def equel():
    global r, san1, san2, u
    if u == '+':
        san2 = int(r)
        r = ''
        label['text'] = str(san1+san2)
    elif u == '-':
        san2 = int(r)
        r = ''
        label['text'] = str(san1-san2)
    elif u == '*':
        san2 = int(r)
        r = ''
        label['text'] = str(san1*san2)
    elif u == '/':
        san2 = int(r)
        r = ''
        label['text'] = str(san1/san2)


def poz():
    global r, san1, san2
    r = ''
    san1 = 0
    san2 = 0
    label['text'] = ''


root = Tk()
root.geometry('280x400')
label = Label(root, text='', height=2, width=30,
              font=('bold', 25), bg='black', fg='white')
root.resizable(False, False)
label.pack()
a = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(1, len(a)+1):
    s = a[i-1]
    s = Button(root, text=str(i), height=3, width=7, font=('Arial', 13),
               bd=3, bg='gray', command=lambda x=str(i): but(x), relief=RAISED)
    s.place(x=c, y=v)
    if i == 3 or i == 6:
        v += 60
        c = 0
    else:
        c += 70
ico = PhotoImage(file='ping.png')
root['bg'] = 'black'
root.iconphoto(False, ico)
root.iconbitmap(r'C:\Users\Atashka\Downloads\ping.ico')
a0 = Button(root, text='0', height=3, width=23,
            command=lambda x='0': but(x), bd=3, bg='gray')
a0.place(x=-15, y=283)
a11 = Button(root, text='-', height=3, width=3, command=ayyr,
             bd=4, relief=RAISED, bg='orange', font=('Arial', 31))
a11.place(x=211, y=165)
a22 = Button(root, text='+', height=3, width=8, command=add,
             bd=4, relief=RAISED, bg='orange', font=('Arial', 10))
a22.place(x=210, y=100)
a33 = Button(root, text='=', height=3, width=7, command=equel,
             bd=4, relief=RAISED, bg='orange', font=('Arial', 11))
a33.place(x=210, y=283)
a44 = Button(root, text='/', height=3, width=8, command=bol,
             bd=4, relief=RAISED, bg='orange', font=('Arial', 11))
a44.place(x=210, y=160)
a33 = Button(root, text='*', height=3, width=7, command=kopelt,
             bd=4, relief=RAISED, bg='orange', font=('Arial', 10))
a33.place(x=140, y=283)
C = Button(root, text='AC', height=3, width=30, fg='black',
           command=poz, bd=3, relief=RAISED, bg='#D4D4D2', font=('Arial', 13))
C.place(x=0, y=340)
root.mainloop()
