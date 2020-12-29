from tkinter import *
import tkinter.ttk as ttk
import math as m
import random as rand

window = Tk()
window.title("Calculator")
TAB_CONTROL = ttk.Notebook(window)

e = Entry(window, width=50, borderwidth=5, relief=RIDGE, fg="white", bg="Black")
e.pack(expand=1, padx=10, pady=15)

TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Standard')
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Numerals')
TAB_CONTROL.pack(expand=1, fill="both")
TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text='Trigonometric')
TAB_CONTROL.pack(expand=1, fill="both")

def click(to_print):
    old = e.get()
    e.delete(0, END)
    e.insert(0, old+to_print)
    return


def clear():
    e.delete(0, END)
    return

def bksps():
    current = e.get()
    length = len(current)-1
    e.delete(length, END)

def evaluate():
    ans = e.get()
    ans = eval(ans)
    e.delete(0, END)
    e.insert(0, ans)

def sc(event):
    key = event.widget
    text = key['text']
    no = e.get()
    result = ''
    if text == 'deg':
        result = str(m.degrees(float(no)))
    if text == 'rad':
        result = str(m.radians(float(no)))
    if text == 'rand':
        result = str(rand.random())
    if text == 'ceil':
        result = str(m.ceil(no))
    if text == 'floor':
        result = str(m.floor(no))
    if text == 'sin':
        result = str(m.sin(float(no)))
    if text == 'cos':
        result = str(m.cos(float(no)))
    if text == 'tan':
        result = str(m.tan(float(no)))
    if text == 'sinh':
        result = str(m.sinh(float(no)))
    if text == 'asin':
        result = str(m.asin(float(no)))
    if text == 'asinh':
        result = str(m.asinh(float(no)))
    if text == 'cos':
        result = str(m.cos(float(no)))
    if text == 'cosh':
        result = str(m.cosh(float(no)))
    if text == 'acos':
        result = str(m.acos(float(no)))
    if text == 'acosh':
        result = str(m.acosh(float(no)))
    if text == 'tan':
        result = str(m.tan(float(no)))
    if text == 'tanh':
        result = str(m.tanh(float(no)))
    if text == 'atan':
        result = str(m.atan(float(no)))
    if text == 'atanh':
        result = str(m.atanh(float(no)))
    if text == 'lg':
        result = str(m.log10(float(no)))
    if text == 'ln':
        result = str(m.log(float(no)))
    if text == 'sqrt':
        result = str(m.sqrt(float(no)))
    if text == 'x!':
        result = str(m.factorial(float(no)))
    if text == '1/x':
        result = str(1/(float(no)))
    if text == 'pi':
        if no == '':
            result = str(m.pi)
        else:
            result = str(float(no) * m.pi)
    if text == 'e':
        if no == '':
            result = str(m.e)
        else:
            result = str(float(no) * m.e)
    if text == 'twopw':
        if no == '':
            result = str(m.pi)
        else:
            result = str(float(no) * m.pi)
    if text == '2^':
        if no == '':
            result = "2**"
        else:
            result = str(2**float(no))
    if text == '10^':
        if no == '':
            result = "10**"
        else:
            result = str(10**float(no))

    e.delete(0, END)
    e.insert(0, result)

'''------------------------------------------------------------------------------------------------------'''
ac = Button(TAB2, text='C', padx=29, pady=10, relief=RAISED, bg="#C82C0B", fg="White", command=lambda: clear())
bksp = Button(TAB2, text='bksp', padx=19.45, pady=10, relief=RAISED, bg="#C82C0B", fg="White", command=lambda: bksps())

twopw = Button(TAB2, text='2^', padx=26, pady=10, relief=RAISED, bg="Black", fg="White")
twopw.bind("<Button-1>", sc)
randb = Button(TAB2, text='rand', padx=20, pady=10, relief=RAISED, bg="Black", fg="White")
randb.bind("<Button-1>", sc)
exp = Button(TAB2, text='exp', padx=22, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("e+"))
ceil = Button(TAB2, text='ceil', padx=24, pady=10, relief=RAISED, bg="Black", fg="White")
floor = Button(TAB2, text='floor', padx=20, pady=10, relief=RAISED, bg="Black", fg="white")

square = Button(TAB2, text="^2", padx=26, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("**2"))
frac = Button(TAB2, text="1/x", padx=23, pady=10, relief=RAISED, bg="Black", fg="White")
frac.bind("<Button-1>", sc)
absb = Button(TAB2, text="|x|", padx=26, pady=10, relief=RAISED, bg="black", fg='white', command=lambda: click("abs("))
e_b = Button(TAB2, text='e', padx=30, pady=10, relief=RAISED, bg="Black", fg="White")
e_b.bind("<Button-1>", sc)
pib = Button(TAB2, text="pi", padx=27, pady=10, relief=RAISED, bg="Black", fg="White")
pib.bind("<Button-1>", sc)

sqrtm = Button(TAB2, text='√x', padx=26, pady=10, relief=RAISED, bg="Black", fg="White")
sqrtm.bind("<Button-1>", sc)
par1st = Button(TAB2, text='(', padx=29, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("("))
par2nd = Button(TAB2, text=')', padx=30, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click(")"))
fact = Button(TAB2, text="x!", padx=28, pady=10, relief=RAISED,bg="Black", fg="White")
fact.bind("<Button-1>", sc)
mod = Button(TAB2, text='mod', padx=20, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("%"))

power = Button(TAB2, text='^', padx=29, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("**"))
seven = Button(TAB2, text="7", padx=28, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("7"))
eight = Button(TAB2, text="8", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("8"))
nine = Button(TAB2, text="9", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("9"))
div = Button(TAB2, text='/', padx=29, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("/"))

tenpw = Button(TAB2, text='10^', padx=23, pady=10, relief=RAISED, bg="Black", fg='white', command=lambda: click("10**"))
tenpw = Button(TAB2, text='10^', padx=23, pady=10, relief=RAISED, bg="Black", fg='white')
tenpw.bind("<Button-1>", sc)
four = Button(TAB2, text="4", padx=28, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("4"))
five = Button(TAB2, text="5", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("5"))
six = Button(TAB2, text="6", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("6"))
mult = Button(TAB2, text="*", padx=29, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("*"))

lg = Button(TAB2, text='log', padx=24, pady=10, relief=RAISED, bg="Black", fg="White")
lg.bind("<Button-1>", sc)
one = Button(TAB2, text="1", padx=28, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("1"))
two = Button(TAB2, text="2", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("2"))
three = Button(TAB2, text="3", padx=29, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("3"))
minus = Button(TAB2, text="-", padx=29, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("-"))

ln = Button(TAB2, text='ln', padx=28, pady=10, relief=RAISED, bg="Black", fg="White")
lg.bind("<Button-1>", sc)
dot = Button(TAB2, text='.', padx=29.5, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("."))
zero = Button(TAB2, text='0', padx=28, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("0"))
equal = Button(TAB2, text='=', padx=28, pady=10, relief=RAISED, bg="Orange", fg="Black", command=lambda: evaluate())
plus = Button(TAB2, text="+", padx=28, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("+"))

ac.grid(row=1, column=3)
bksp.grid(row=1, column=4)

twopw.grid(row=2, column=0)
randb.grid(row=2, column=1)
exp.grid(row=2, column=2)
ceil.grid(row=2, column=3)
floor.grid(row=2, column=4)

square.grid(row=3, column=0)
frac.grid(row=3, column=1)
absb.grid(row=3, column=2)
e_b.grid(row=3, column=3)
pib.grid(row=3, column=4)

sqrtm.grid(row=4, column=0)
par1st.grid(row=4, column=1)
par2nd.grid(row=4, column=2)
fact.grid(row=4, column=3)
mod.grid(row=4, column=4)

power.grid(row=5, column=0)
seven.grid(row=5, column=1)
eight.grid(row=5, column=2)
nine.grid(row=5, column=3)
div.grid(row=5, column=4)

tenpw.grid(row=6, column=0)
four.grid(row=6, column=1)
five.grid(row=6, column=2)
six.grid(row=6, column=3)
mult.grid(row=6, column=4)

lg.grid(row=7, column=0)
one.grid(row=7, column=1)
two.grid(row=7, column=2)
three.grid(row=7, column=3)
minus.grid(row=7, column=4)

ln.grid(row=8, column=0)
dot.grid(row=8, column=1)
zero.grid(row=8, column=2)
equal.grid(row=8, column=3)
plus.grid(row=8, column=4)



'''------------------------------------------------------------------------------------------------------'''

ac = Button(TAB1, text='C', padx=36.5, pady=15, relief=RAISED, bg="#C82C0B", fg="White", command=lambda: clear())
bksp = Button(TAB1, text='bksp', padx=30, pady=15, relief=RAISED, bg="#C82C0B", fg="White", command=lambda: bksps())

frac = Button(TAB1, text="1/x", padx=33, pady=15, relief=RAISED, bg="Black", fg="White")
frac.bind("<Button-1>", sc)
fact = Button(TAB1, text="x!", padx=35, pady=15, relief=RAISED,bg="Black", fg="White")
fact.bind("<Button-1>", sc)
square = Button(TAB1, text="^2", padx=35, pady=15, relief=RAISED, bg="Black", fg="White", command=lambda: click("**2"))
sqrtm = Button(TAB1, text='√x', padx=35, pady=15, relief=RAISED, bg="Black", fg="White")
sqrtm.bind("<Button-1>", sc)

seven = Button(TAB1, text="7", padx=38, pady=15, relief=RAISED, bg="Grey", fg="White", command=lambda: click("7"))
eight = Button(TAB1, text="8", padx=37, pady=15, relief=RAISED, bg="Grey", fg="White", command=lambda: click("8"))
nine = Button(TAB1, text="9", padx=38, pady=15, relief=RAISED, bg="Grey", fg="White", command=lambda: click("9"))
div = Button(TAB1, text='/', padx=40, pady=15, relief=RAISED, bg="Black", fg="White", command=lambda: click("/"))

four = Button(TAB1, text="4", padx=38, pady=15, relief=RAISED, bg="Grey", fg="White", command=lambda: click("4"))
five = Button(TAB1, text="5", padx=37, pady=15, relief=RAISED, bg="Grey", fg="White", command=lambda: click("5"))
six = Button(TAB1, text="6", padx=38, pady=15, relief=RAISED, bg="Grey", fg="White", command=lambda: click("6"))
mult = Button(TAB1, text="*", padx=40, pady=15, relief=RAISED, bg="Black", fg="White", command=lambda: click("*"))


one = Button(TAB1, text="1", padx=38, pady=15, relief=RAISED, bg="Grey", fg="White", command=lambda: click("1"))
two = Button(TAB1, text="2", padx=37, pady=15, relief=RAISED, bg="Grey", fg="White", command=lambda: click("2"))
three = Button(TAB1, text="3", padx=38, pady=15, relief=RAISED, bg="Grey", fg="White", command=lambda: click("3"))
minus = Button(TAB1, text="-", padx=40, pady=15, relief=RAISED, bg="Black", fg="White", command=lambda: click("-"))


dot = Button(TAB1, text='.', padx=40, pady=15, relief=RAISED, bg="Black", fg="White", command=lambda: click("."))
zero = Button(TAB1, text='0', padx=37, pady=15, relief=RAISED, bg="Grey", fg="White", command=lambda: click("0"))
equal = Button(TAB1, text='=', padx=38, pady=15, relief=RAISED, bg="Orange", fg="Black", command=lambda: evaluate())
plus = Button(TAB1, text="+", padx=38, pady=15, relief=RAISED, bg="Black", fg="White", command=lambda: click("+"))

ac.grid(row=1, column=2)
bksp.grid(row=1, column=3)

frac.grid(row=2, column=0)
fact.grid(row=2, column=1)
square.grid(row=2, column=2)
sqrtm.grid(row=2, column=3)

seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
div.grid(row=3, column=3)

four.grid(row=4, column=0)
five.grid(row=4, column=1)
six.grid(row=4, column=2)
mult.grid(row=4, column=3)

one.grid(row=5, column=0)
two.grid(row=5, column=1)
three.grid(row=5, column=2)
minus.grid(row=5, column=3)

dot.grid(row=6, column=0)
zero.grid(row=6, column=1)
equal.grid(row=6, column=2)
plus.grid(row=6, column=3)
'''------------------------------------------------------------------------------------------------------'''


sinh = Button(TAB3, text="sinh", padx=29, pady=10, relief=RAISED, bg='black', fg='white')
sinh.bind("<Button-1>", sc)
asin = Button(TAB3, text="asin", padx=29, pady=10, relief=RAISED, bg='black', fg='white')
asin.bind("<Button-1>", sc)
acos = Button(TAB3, text='acos', padx=29, pady=10, relief=RAISED, bg='black', fg='white')
acos.bind("<Button-1>", sc)
atan = Button(TAB3, text='atan', padx=29, pady=10, relief=RAISED, bg='black', fg='white')
atan.bind("<Button-1>", sc)
ac = Button(TAB3, text='C', padx=34, pady=10, relief=RAISED, bg="#C82C0B", fg="White", command=lambda: clear())

cosh = Button(TAB3, text='cosh', padx=27, pady=10, relief=RAISED, bg='black', fg='white')
cosh.bind("<Button-1>", sc)
asinh = Button(TAB3, text='asinh', padx=25, pady=10, relief=RAISED, bg='black', fg='white')
asinh.bind("<Button-1>", sc)
acosh = Button(TAB3, text='acosh', padx=25, pady=10, relief=RAISED, bg='black', fg='white')
acosh.bind("<Button-1>", sc)
atanh = Button(TAB3, text='atanh', padx=25, pady=10, relief=RAISED, bg='black', fg='white')
atanh.bind("<Button-1>", sc)
bksp = Button(TAB3, text='bksp', padx=25, pady=10, relief=RAISED, bg="#C82C0B", fg="White", command=lambda: bksps())

tanh = Button(TAB3, text='tanh', padx=28, pady=10, relief=RAISED, bg='black', fg='white')
tanh.bind("<Button-1>", sc)
degb = Button(TAB3, text='deg', padx=29, pady=10, relief=RAISED, bg='black', fg='white')
degb.bind("<Button-1>", sc)
radb = Button(TAB3, text='radb', padx=29, pady=10, relief=RAISED, bg='black', fg='white')
radb.bind("<Button-1>", sc)
pib = Button(TAB3, text="pi", padx=34, pady=10, relief=RAISED, bg="Black", fg="White")
pib.bind("<Button-1>", sc)
div = Button(TAB3, text='/', padx=35, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("/"))

sin = Button(TAB3, text='sin', padx=32, pady=10, relief=RAISED, bg='black', fg='white')
sin.bind("<Button-1>", sc)
seven = Button(TAB3, text="7", padx=36, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("7"))
eight = Button(TAB3, text="8", padx=36, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("8"))
nine = Button(TAB3, text="9", padx=36, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("9"))
mult = Button(TAB3, text="*", padx=36, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("*"))

cos = Button(TAB3, text='cos', padx=31, pady=10, relief=RAISED, bg='black', fg='white')
cos.bind("<Button-1>", sc)
four = Button(TAB3, text="4", padx=36, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("4"))
five = Button(TAB3, text="5", padx=36, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("5"))
six = Button(TAB3, text="6", padx=36, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("6"))
minus = Button(TAB3, text="-", padx=36, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("-"))

tan = Button(TAB3, text='tan', padx=32, pady=10, relief=RAISED, bg='black', fg='white')
tan.bind("<Button-1>", sc)
one = Button(TAB3, text="1", padx=36, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("1"))
two = Button(TAB3, text="2", padx=36, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("2"))
three = Button(TAB3, text="3", padx=36, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("3"))
plus = Button(TAB3, text="+", padx=35, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("+"))

dot = Button(TAB3, text='.', padx=36, pady=10, relief=RAISED, bg="Black", fg="White", command=lambda: click("."))
zero = Button(TAB3, text='0', padx=36, pady=10, relief=RAISED, bg="Grey", fg="White", command=lambda: click("0"))
equal = Button(TAB3, text='=', padx=36, pady=10, relief=RAISED, bg="Orange", fg="Black", command=lambda: evaluate())

sinh.grid(row=1, column=0)
asin.grid(row=1, column=1)
acos.grid(row=1, column=2)
atan.grid(row=1, column=3)
ac.grid(row=1, column=4)

cosh.grid(row=2, column=0)
asinh.grid(row=2, column=1)
acosh.grid(row=2, column=2)
atanh.grid(row=2, column=3)
bksp.grid(row=2, column=4)

tanh.grid(row=3, column=0)
degb.grid(row=3, column=1)
radb.grid(row=3, column=2)
pib.grid(row=3, column=3)
div.grid(row=3, column=4)

sin.grid(row=4, column=0)
seven.grid(row=4, column=1)
eight.grid(row=4, column=2)
nine.grid(row=4, column=3)
mult.grid(row=4, column=4)

cos.grid(row=5, column=0)
four.grid(row=5, column=1)
five.grid(row=5, column=2)
six.grid(row=5, column=3)
minus.grid(row=5, column=4)

tan.grid(row=6, column=0)
one.grid(row=6, column=1)
two.grid(row=6, column=2)
three.grid(row=6, column=3)
plus.grid(row=6, column=4)

dot.grid(row=7, column=1)
zero.grid(row=7, column=2)
equal.grid(row=7, column=3)


TAB1.mainloop()
TAB2.mainloop()
TAB3.mainloop()
window.mainloop()