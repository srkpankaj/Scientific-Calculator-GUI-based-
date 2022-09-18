import math
from tkinter import *
from tkinter.messagebox import *
import math as m
from audio_speaker import play_audio
import threading

# some useful variables
font=('Verdana',20,'bold')
ob = play_audio(voice='female')

# important function

def enterclick(event):
    print('hi')
    e=Event()
    e.widget=equal_Btn
    click_btn_function(e)

def calculate_sc(event):
    print('Btn..')
    Btn=event.widget
    text=Btn['text']
    ex=textField.get()
    print(text)
    answer=''
    if text=='Deg':
        print('Cal Degree')
        answer = str(m.degrees(float(ex)))
    elif text=='Rad':
        print('Cal Radian')
        answer = str(m.radians(float(ex)))
    elif text=='x!':
        print('Cal Factorial')
        answer = str(m.factorial(int(ex)))
    elif text == 'sinθ':
        print('Cal sin')
        answer = str(m.sin(m.radians(int(ex))))
    elif text == 'cosθ':
        print('Cal cos')
        answer = str(m.cos(m.radians(int(ex))))
    elif text == 'tanθ':
        print('Cal tan')
        answer = str(m.tan(m.radians(int(ex))))
    elif text == '√ ':
        print('Cal sqrt')
        answer=m.sqrt(int(ex))
    elif text == '^':
        print('Cal power')
        base,pow = ex.split(',')
        print(base)
        print(pow)
        answer=m.pow(int(base),int(pow))

    textField.delete(0,END)
    textField.insert(0,answer)


normalcalc=True

def sc_click():
    global normalcalc
    if normalcalc:
        # show scientific
        buttonFrame.pack_forget()

        # add sc Frame
        scFrame.pack(side=TOP,pady=20)
        buttonFrame.pack(side=TOP)
        window.geometry('550x690')
        print('show scientific')
        normalcalc=False
    else:
        print('show normal')
        scFrame.pack_forget()
        window.geometry('550x520')
        normalcalc=True
# end


def all_clear():
    textField.delete(0,END)


def clear():
    ex=textField.get()
    ex=ex[0:len(ex)-1]
    textField.delete(0,END)
    textField.insert(0,ex)



def click_btn_function(event):
    global p
    print('btn clicked')
    b=event.widget
    text=b['text']
    print(text)
    t=threading.Thread(target=ob.speak,args=(text,))
    t.start()

    if text=='x':
        textField.insert(END,'*')
        return

    if text=='=':
        try:
            expression = textField.get()
            answer = eval(expression)
            textField.delete(0, END)
            textField.insert(0, answer)
        except Exception as e:
            print('Error..',e)
            showerror('Error',e)
        return

    textField.insert(END,text)

# creating a window
window=Tk()
window.title('My Calculator')
window.geometry('550x520')

# picture_label
pic=PhotoImage(file='img/cal (1).png')
headingLabel=Label(window,image=pic)
headingLabel.pack(side=TOP,pady=15)

# heading_label
heading=Label(window,text='My Calculator',font=font,underline=0)
heading.pack(side=TOP)

# textfield
textField=Entry(window,font=font,justify=CENTER)
textField.pack(side=TOP,pady=10,fill=X,padx=10)

# buttons
buttonFrame=Frame(window)
buttonFrame.pack(side=TOP)

# adding_buttons
temp=1
for i in range(0,3):
    for j in range(0,3):
        btn=Button(buttonFrame,text=str(temp),font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
        btn.grid(row=i,column=j)
        temp+=1
        btn.bind('<Button-1>',click_btn_function)


zero_Btn=Button(buttonFrame,text='0' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
zero_Btn.grid(row=3,column=0)

dot_Btn=Button(buttonFrame,text='.' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
dot_Btn.grid(row=3,column=1)

equal_Btn=Button(buttonFrame,text='=' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
equal_Btn.grid(row=3,column=2)

plus_Btn=Button(buttonFrame,text='+' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
plus_Btn.grid(row=0,column=3)

minus_Btn=Button(buttonFrame,text='-' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
minus_Btn.grid(row=1,column=3)

multi_Btn=Button(buttonFrame,text='x' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
multi_Btn.grid(row=2,column=3)

divide_Btn=Button(buttonFrame,text='/' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
divide_Btn.grid(row=3,column=3)

clear_Btn=Button(buttonFrame,text='<--' ,font=font,width=13,relief='ridge',activebackground='orange',activeforeground='white',command=clear)
clear_Btn.grid(row=4,column=0,columnspan=2)

allClear_Btn=Button(buttonFrame,text='AC' ,font=font,width=13,relief='ridge',activebackground='orange',activeforeground='white',command=all_clear)
allClear_Btn.grid(row=4,column=2,columnspan=2)

# binding all buttons
plus_Btn.bind('<Button-1>',click_btn_function)
minus_Btn.bind('<Button-1>',click_btn_function)
multi_Btn.bind('<Button-1>',click_btn_function)
divide_Btn.bind('<Button-1>',click_btn_function)
zero_Btn.bind('<Button-1>',click_btn_function)
dot_Btn.bind('<Button-1>',click_btn_function)
equal_Btn.bind('<Button-1>',click_btn_function)


# press keyword enter button perform = button in calculator
textField.bind('<Return>',enterclick)


scFrame=Frame(window)

sqrt_Btn=Button(scFrame,text='√ ' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
sqrt_Btn.grid(row=0,column=0)

power_Btn=Button(scFrame,text='^' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
power_Btn.grid(row=0,column=1)

factorial_Btn=Button(scFrame,text='x!' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
factorial_Btn.grid(row=0,column=2)

radian_Btn=Button(scFrame,text='Rad' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
radian_Btn.grid(row=0,column=3)

degree_Btn=Button(scFrame,text='Deg' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
degree_Btn.grid(row=1,column=0)

sin_Btn=Button(scFrame,text='sinθ' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
sin_Btn.grid(row=1,column=1)

cos_Btn=Button(scFrame,text='cosθ' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
cos_Btn.grid(row=1,column=2)

tan_Btn=Button(scFrame,text='tanθ' ,font=font,width=6,relief='ridge',activebackground='orange',activeforeground='white')
tan_Btn.grid(row=1,column=3)

# binding sc buttions
sqrt_Btn.bind('<Button-1>',calculate_sc)
power_Btn.bind('<Button-1>',calculate_sc)
factorial_Btn.bind('<Button-1>',calculate_sc)
radian_Btn.bind('<Button-1>',calculate_sc)
degree_Btn.bind('<Button-1>',calculate_sc)
sin_Btn.bind('<Button-1>',calculate_sc)
cos_Btn.bind('<Button-1>',calculate_sc)
tan_Btn.bind('<Button-1>',calculate_sc)


fontMenu=('',15)
menubar=Menu(window)


mode=Menu(menubar,font=fontMenu,tearoff=0)
mode.add_checkbutton(label='Scientific Calculator',command=sc_click)

menubar.add_cascade(label='Mode',menu=mode)


window.config(menu=menubar)


window.mainloop()