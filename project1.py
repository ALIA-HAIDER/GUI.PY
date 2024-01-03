#importing tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Combobox
#inertialsing window 
root=Tk()
#giving title to window
root.title("simple gui")
root.geometry("200x200")
#inertialising frame because fram ewill hold all the widges we will add
app=Frame(root)
#adding gring becuse without it nothing works or it provide definite space on frame
app.grid(column=2,row=1)
#creating a lable 
l1=Label(app,text="first lable text")
l1.grid(row=0,column=0)
l2=Label(app,text="my second lable")
l2.grid()
###        button ##
#my first button
b1=Button(app,text="i do nothing",bg="yellow",fg="green")
#here app is the leader of button and text is presented on button
b1.grid(row=1,column=2)
#now let's create second button
b2=Button(app)
b2.grid()
#here you notice that i gave only leader app as an atribute so it is an empty button 
#we can add text to button by following steps
b2.configure(text="me too!")
#now lets build third button
#now lets try to configure this button by another way 
# b3["text"]="same here!"
def clicked1():
    l=Label(app,text="hello!you succeded in making clickable button")
    l.grid(row=4,column=3)
b3=Button(app,text="click hear",command=clicked1)
b3.grid(row=2,column=2)
# noe lets make another button clickable
def click3():
    x=Label(app,text="bravo! u also succeded in making clickable  button 2")
    x.grid(row=3,column=2)
b4=Button(app,text="clickable button 2",command=click3)
b4.grid()
#combo box weidgt
combo=Combobox(app)
combo['values']=(1,2,3,4,5,"text")
combo.current(2)
combo.grid(row=3,column=3)
#importing second combo box 
combo2=Combobox(app)
combo2['values']=(22,44,66,97,"helli")
combo2.current(0)
combo2.grid(row=3,column=4)
#check button widget 
#to create a check button widget you can use Checkbutton class
check1_state=BooleanVar()
check1_state.set(True)
check1=Checkbutton(app,text='select',var=check1_state)
check1.grid()
#creating chedck button 2
check2_state=BooleanVar()
check2_state.set(False)
def if_true():
    z=Label(app,text="succeded")
    z.grid(row=4, column=2)
check2=Checkbutton(app,text='button2',var=check2_state,command=if_true)
check2.grid()
#creating check button 3
check3_state=BooleanVar()
check3_state.set(True)
check3=Checkbutton(app,text="checkbutton3",var=check3_state)
check3.grid()
#radio button making
rad1=Radiobutton(app,text='python',value=1)
rad2=Radiobutton(app,text='java',value=2)
rad3=Radiobutton(app,text='cpp',value=4)
rad1.grid()
rad2.grid()
rad3.grid()
#scrolles text widget
txt=scrolledtext.ScrolledText(app,width=20,height=20)
txt.insert(INSERT,"heelo ! i'm Scrolled text widget")
txt.grid()
#message box
def click5():
    messagebox.showinfo("Message title","message content")
btn=Button(app,text="message box",command=click5)
btn.grid()
#spinBox Widget
spin=Spinbox(app,from_=0,to=100,width=10)
spin.grid()
 # spin box 2
spin2=Spinbox(app,from_=9,to=19,width=5)
spin2.grid()
#  ,,,, organizing layout and widgets
# we use frame to arrange Layouts in window



# text input weidget
my_text=Text(app,width=20,height=20)
my_text.grid()


root.mainloop()