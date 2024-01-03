
from tkinter import *
from tkinter import scrolledtext
root=Tk()
root.title("alias_mad_lib_game")
root.geometry("600x600")
app=Frame(root)
app.grid()
l1=Label(app,text="Enter the information of New Story-->")
l1.grid()
l2=Label(app,text="Person:")
l2.grid()
person=Text(app,width=20,height=1)
person.grid(row=1,column=1)
l3=Label(app,text="Plural Noune:")
l3.grid()
noune=Text(app,width=20,height=1)
noune.grid(row=2,column=1)
l3=Label(app,text="verb:")
l3.grid()
verb=Text(app,width=20,height=1)
verb.grid(row=3,column=1)
l4=Label(app,text="Adjective(s)")
l4.grid()
# reating check button
#check_button1
chk_state1=BooleanVar()
chk_state1.set(False)
chk1=Checkbutton(app,text="itchy", variable='itchya')
chk1.grid(row=4,column=1)
chk_state2=BooleanVar()
chk_state2.set(False)
chk2=Checkbutton(app,text="joyous",variable="joyous")
chk2.grid(row=4,column=2)
chk_state3=BooleanVar()
chk_state3.set(False)
chk3=Checkbutton(app,text="electric",variable="electric")
chk3.grid(row=4,column=3)
# check_button2
l5=Label(app,text="Body parts:")
l5.grid()
chk_state4=BooleanVar()
chk_state4.set(False)
chk4=Checkbutton(app,text="bellybutton")
chk4.grid(row=5,column=1)
chk_state5=BooleanVar()
chk_state5.set(False)
chk5=Checkbutton(app,text="big toe")
chk5.grid(row=5,column=2)
chk_state6=BooleanVar()
chk_state6.set(False)
chk6=Checkbutton(app,text="medulla oblongata")
chk6.grid(row=5,column=3)

def clicked():
    # Get the values from the Text widgets and Checkbuttons
    person_value = person.get("1.0", "end").strip()
    noun_value = noune.get("1.0", "end").strip()
    verb_value = verb.get("1.0", "end").strip()
    
    adjectives = [chk1.cget("itchy") if chk_state1.get() else "",
                  chk2.cget("joyous") if chk_state2.get() else "",
                  chk3.cget("electric") if chk_state3.get() else ""]
    
    body_parts = [chk4.cget("bellybutton") if chk_state4.get() else "",
                  chk5.cget("big toe") if chk_state5.get() else "",
                  chk6.cget("medulla oblongata") if chk_state6.get() else ""]
    
    story2 = "The famous explorer "+ person_value+" had nearly given up a lifelong quest to find the Lost City of "+noun_value+"s " \
        "when one day, the "+noun_value+"found "+person_value+". A strong and peculiar feeling overwhelmed the explorer. " \
        "After all this time, the quest was finally over. A tear came to "+person_value+"'s eyes."
    
    story_text = scrolledtext.ScrolledText(app, width=40, height=10)
    story_text.grid(row=7, column=0, columnspan=3)
    story_text.delete(1.0, END)  # Clear previous content
    story_text.insert(INSERT, story2)
    # Optional: Print the values for debugging
    print("Person:", person_value)
    print("Noun:", noun_value)
    print("Verb:", verb_value)
    print("Adjectives:", adjectives)
    print("Body Parts:", body_parts)


but=Button(app,text="lock information ",command=clicked)
but.grid()


root.mainloop()