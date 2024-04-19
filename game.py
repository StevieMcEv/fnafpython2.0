from tkinter import *

import time
import threading
import random

page = 1.0
doorleft_toggle = False
doorright_toggle = False
lightleft_toggle = False
lightright_toggle = False
bonniedoor = False
chicadoor = False
markdoor = False


root = Tk()
root.geometry("1280x577")
root.title("FNAF PYTHON 2.0")

def changePage():
    global page
    if page == 1.0:
        office.pack_forget()
        
        menu.pack()
    elif page == 2.0:
        
        menu.pack_forget()
        cams1a.pack_forget()
        cams1b.pack_forget()
        cams1c.pack_forget()
        cams2a.pack_forget()
        cams2b.pack_forget()
        cams3.pack_forget()
        cams4a.pack_forget()
        cams4b.pack_forget()
        cams5.pack_forget()
        cams7.pack_forget()
        office.pack()
        
    elif page == 1.1:
        cams1a.pack()
        cams1b.pack_forget()
        cams1c.pack_forget()
        cams2a.pack_forget()
        cams2b.pack_forget()
        cams3.pack_forget()
        cams4a.pack_forget()
        cams4b.pack_forget()
        cams5.pack_forget()
        cams7.pack_forget()
        office.pack_forget()
    elif page == 2.1:
        cams1a.pack_forget()
        cams1b.pack()
        cams1c.pack_forget()
        cams2a.pack_forget()
        cams2b.pack_forget()
        cams3.pack_forget()
        cams4a.pack_forget()
        cams4b.pack_forget()
        cams5.pack_forget()
        cams7.pack_forget()
        office.pack_forget()
    elif page == 3.1:
        cams1a.pack_forget()
        cams1c.pack()
        cams1b.pack_forget()
        cams2a.pack_forget()
        cams2b.pack_forget()
        cams3.pack_forget()
        cams4a.pack_forget()
        cams4b.pack_forget()
        cams5.pack_forget()
        cams7.pack_forget()
        office.pack_forget()
    elif page == 4.1:
        cams1a.pack_forget()
        cams2a.pack()
        cams1c.pack_forget()
        cams1b.pack_forget()
        cams2b.pack_forget()
        cams3.pack_forget()
        cams4a.pack_forget()
        cams4b.pack_forget()
        cams5.pack_forget()
        cams7.pack_forget()
        office.pack_forget()
    elif page == 5.1:
        cams1a.pack_forget()
        cams2b.pack()
        cams1c.pack_forget()
        cams2a.pack_forget()
        cams1b.pack_forget()
        cams3.pack_forget()
        cams4a.pack_forget()
        cams4b.pack_forget()
        cams5.pack_forget()
        cams7.pack_forget()
        office.pack_forget()
    elif page == 6.1:
        cams1a.pack_forget()
        cams3.pack()
        cams1c.pack_forget()
        cams2a.pack_forget()
        cams2b.pack_forget()
        cams1b.pack_forget()
        cams4a.pack_forget()
        cams4b.pack_forget()
        cams5.pack_forget()
        cams7.pack_forget()
        office.pack_forget()
    elif page == 7.1:
        cams1a.pack_forget()
        cams4a.pack()
        cams1c.pack_forget()
        cams2a.pack_forget()
        cams2b.pack_forget()
        cams3.pack_forget()
        cams1b.pack_forget()
        cams4b.pack_forget()
        cams5.pack_forget()
        cams7.pack_forget()
        office.pack_forget()
    elif page == 8.1:
        cams1a.pack_forget()
        cams4b.pack()
        cams1c.pack_forget()
        cams2a.pack_forget()
        cams2b.pack_forget()
        cams3.pack_forget()
        cams4a.pack_forget()
        cams1b.pack_forget()
        cams5.pack_forget()
        cams7.pack_forget()
        office.pack_forget()
    elif page == 9.1:
        cams1a.pack_forget()
        cams5.pack()
        cams1c.pack_forget()
        cams2a.pack_forget()
        cams2b.pack_forget()
        cams3.pack_forget()
        cams4a.pack_forget()
        cams4b.pack_forget()
        cams1b.pack_forget()
        cams7.pack_forget()
        office.pack_forget()
    elif page == 10.1:
        cams1a.pack_forget()
        cams7.pack()
        cams1c.pack_forget()
        cams2a.pack_forget()
        cams2b.pack_forget()
        cams3.pack_forget()
        cams4a.pack_forget()
        cams4b.pack_forget()
        cams1b.pack_forget()
        cams5.pack_forget()
        office.pack_forget()
night = 0
def select_1():
    global page, night
    page = 2.0
    night = 1
    nightselect()
    changePage()

def select_2():
    global page, night
    page = 2.0
    night = 2
    nightselect()
    changePage()

def select_3():
    global page, night
    page = 2.0
    night = 3
    nightselect()
    changePage()

def select_4():
    global page, night
    page = 2.0
    night = 4
    nightselect()
    changePage()

def select_5():
    global page, night
    page = 2.0
    night = 5
    nightselect()
    changePage()

def select_6():
    global page, night
    page = 2.0
    night = 6
    nightselect()
    changePage()

def backoffice():
    global page
    page = 2.0
    changePage()

def camoffice():
    global page
    page = 1.1
    changePage()

def cam1a():
    global page
    page = 1.1
    changePage()

def cam1b():
    global page
    page = 2.1
    changePage()

def cam1c():
    global page
    page = 3.1
    changePage()

def cam2a():
    global page
    page = 4.1
    changePage()

def cam2b():
    global page
    page = 5.1
    changePage()

def cam3():
    global page
    page = 6.1
    changePage()

def cam4a():
    global page
    page = 7.1
    changePage()

def cam4b():
    global page
    page = 8.1
    changePage()

def cam5():
    global page
    page = 9.1
    changePage()

def cam7():
    global page
    page = 10.1
    changePage()

menu = Frame(root, bg='grey')
office = Frame(root, bg='grey')
cams1a = Frame(root, bg='grey')
cams1b = Frame(root, bg='grey')
cams1c = Frame(root, bg='grey')
cams2a = Frame(root, bg='grey')
cams2b = Frame(root, bg='grey')
cams3 = Frame(root, bg='grey')
cams4a = Frame(root, bg='grey')
cams4b = Frame(root, bg='grey')
cams5 = Frame(root, bg='grey')
cams7 = Frame(root, bg='grey')






clock12 = PhotoImage(file='fnafpython2.0-main/assets/12AM.png')
clock1 = PhotoImage(file='fnafpython2.0-main/assets/1AM.png')
clock2 = PhotoImage(file='fnafpython2.0-main/assets/2AM.png')
clock3 = PhotoImage(file='fnafpython2.0-main/assets/3AM.png')
clock4 = PhotoImage(file='fnafpython2.0-main/assets/4AM.png')
clock5 = PhotoImage(file='fnafpython2.0-main/assets/5AM.png')
clock6 = PhotoImage(file='fnafpython2.0-main/assets/6AM.png')





#### Menu ####
menuback = PhotoImage(file='fnafpython2.0-main/assets/menu.png')
menuimg = Label(menu,image=menuback)
menuimg.pack() 
txt_night1 = Button(menu, text="Night 1", font=('Terminal',20),fg= 'white', bg= 'black', command=lambda: select_1())
txt_night1.place(x= 76, y= 370)
txt_night2 = Button(menu, text="Night 2", font=('Terminal',20),fg= 'white', bg= 'black', command=lambda: select_2())
txt_night2.place(x= 236, y=370)
txt_night3 = Button(menu, text="Night 3", font=('Terminal',20),fg= 'white', bg= 'black', command=lambda: select_3())
txt_night3.place(x= 76, y=410)
txt_night4 = Button(menu, text="Night 4", font=('Terminal',20),fg= 'white', bg= 'black', command=lambda: select_4())
txt_night4.place(x= 236, y=410)
txt_night5 = Button(menu, text="Night 5", font=('Terminal',20),fg= 'white', bg= 'black', command=lambda: select_5())
txt_night5.place(x= 76, y=450)
txt_night6 = Button(menu, text="Night 6", font=('Terminal',20),fg= 'red', bg= 'black', command=lambda: select_6())
txt_night6.place(x= 236, y=450)

#### Office ####
office_canvas = Canvas(office, bg='grey', width=1280, height=577)
office_canvas.pack()

officeimg = PhotoImage(file='fnafpython2.0-main/assets/office.png')
office_canvas.create_image(640,288, image=officeimg)


lightleft_img = PhotoImage(file='fnafpython2.0-main/assets/lightleft.png')
if lightleft_toggle == True:
    office_canvas.create_image(640,288, image=lightleft_img)



lightright_img = PhotoImage(file='fnafpython2.0-main/assets/lightright.png')

if lightright_toggle == True:
    office_canvas.create_image(640,288, image=lightright_img)

btnleftdr_img = PhotoImage(file='fnafpython2.0-main/assets/btnleftdr.png')
office_canvas.create_image(640,288, image=btnleftdr_img)

btnleftlit_img = PhotoImage(file='fnafpython2.0-main/assets/btnleftlit.png')
office_canvas.create_image(640,288, image=btnleftlit_img)

btnrightdr_img = PhotoImage(file='fnafpython2.0-main/assets/btnrightdr.png')
office_canvas.create_image(630,288, image=btnrightdr_img)

btnrightlit_img = PhotoImage(file='fnafpython2.0-main/assets/btnrightlit.png')
office_canvas.create_image(630,288, image=btnrightlit_img)

chica_doorimg = PhotoImage(file='fnafpython2.0-main/assets/chica_door.png')


foxy_doorimg = PhotoImage(file='fnafpython2.0-main/assets/foxy_door.png')


goldenfred_officeimg = PhotoImage(file='fnafpython2.0-main/assets/goldenfred_office.png')


mark_doorimg = PhotoImage(file='fnafpython2.0-main/assets/mark_door.png')


bonnie_doorimg = PhotoImage(file='fnafpython2.0-main/assets/bonnie_door.png')


cambtn_img = PhotoImage(file='fnafpython2.0-main/assets/cambtn2.png')
officecambtn = Button(office, bg = 'black', image=cambtn_img, command=lambda: camoffice())
officecambtn.place(x= 320, y= 510)


door_leftimg = PhotoImage(file='fnafpython2.0-main/assets/door_left.png')
if doorleft_toggle == True:
    office_canvas.create_image(640,288, image=door_leftimg)

door_rightimg = PhotoImage(file='fnafpython2.0-main/assets/door_right.png')
if doorright_toggle == True:
    office_canvas.create_image(640,288, image=door_rightimg)
#### Cameras ####


#### Camera 1a####

canvas = Canvas(cams1a, bg="black", width=1280, height=577)
canvas.pack()


stage = PhotoImage(file="fnafpython2.0-main/assets/stage.png")
canvas.create_image(640,288,image=stage)

fredstage = PhotoImage(file="fnafpython2.0-main/assets/fredstage.png")


bonstage = PhotoImage(file="fnafpython2.0-main/assets/bonstage.png")



c1a2 = PhotoImage(file="fnafpython2.0-main/assets/1a2.png")
c1b2 = PhotoImage(file="fnafpython2.0-main/assets/1b2.png")
c1c2 = PhotoImage(file="fnafpython2.0-main/assets/1c2.png")
c2a2 = PhotoImage(file="fnafpython2.0-main/assets/2a2.png")
c2b2 = PhotoImage(file="fnafpython2.0-main/assets/2b2.png")
c32 = PhotoImage(file="fnafpython2.0-main/assets/32.png")
c4a2 = PhotoImage(file="fnafpython2.0-main/assets/4a2.png")
c4b2 = PhotoImage(file='fnafpython2.0-main/assets/4b2.png')
c52 = PhotoImage(file='fnafpython2.0-main/assets/52.png')
c72 = PhotoImage(file='fnafpython2.0-main/assets/72.png')

c1abtn1 = Button(canvas, bg = 'black', image=c1a2, command=lambda: cam1a())
c1abtn1.place(x= 990, y= 275)

c1bbtn1 = Button(canvas, bg = 'black', image=c1b2, command=lambda: cam1b())
c1bbtn1.place(x= 975, y= 320)

c1cbtn1 = Button(canvas, bg = 'black', image=c1c2, command=lambda: cam1c())
c1cbtn1.place(x= 950, y= 375)

c2abtn1 = Button(canvas, bg = 'black', image=c2a2, command=lambda: cam2a())
c2abtn1.place(x= 990, y= 455)

c2bbtn1 = Button(canvas, bg = 'black', image=c2b2, command=lambda: cam2b())
c2bbtn1.place(x= 990, y= 485)

c3btn1 = Button(canvas, bg = 'black', image=c32, command=lambda: cam3())
c3btn1.place(x= 930, y= 445)

c4abtn1 = Button(canvas, bg = 'black', image=c4a2, command=lambda: cam4a())
c4abtn1.place(x= 1070, y= 455)

c4bbtn1 = Button(canvas, bg = 'black', image=c4b2, command=lambda: cam4b())
c4bbtn1.place(x= 1070, y= 485)

c5btn1 = Button(canvas, bg = 'black', image=c52, command=lambda: cam5())
c5btn1.place(x= 900, y= 335)

c7btn1 = Button(canvas, bg = 'black', image=c72, command=lambda: cam7())
c7btn1.place(x= 1150, y= 335)

c1acambtn = Button(canvas, bg = 'black', image=cambtn_img, command=lambda: backoffice())
c1acambtn.place(x= 300, y= 510)




## Cam 1b ##

canvas2 = Canvas(cams1b, bg="black", width=1280, height=577)
canvas2.pack()


dinning = PhotoImage(file="fnafpython2.0-main/assets/dinning.png")
canvas2.create_image(640,288,image=dinning)

freddin = PhotoImage(file="fnafpython2.0-main/assets/freddin.png")


bondin = PhotoImage(file="fnafpython2.0-main/assets/bondin.png")


chicadin = PhotoImage(file="fnafpython2.0-main/assets/chicadin.png")


c1abtn2 = Button(canvas2, bg = 'black', image=c1a2, command=lambda: cam1a())
c1abtn2.place(x= 990, y= 275)

c1bbtn2 = Button(canvas2, bg = 'black', image=c1b2, command=lambda: cam1b())
c1bbtn2.place(x= 975, y= 320)

c1cbtn2 = Button(canvas2, bg = 'black', image=c1c2, command=lambda: cam1c())
c1cbtn2.place(x= 950, y= 375)

c2abtn2 = Button(canvas2, bg = 'black', image=c2a2, command=lambda: cam2a())
c2abtn2.place(x= 990, y= 455)

c2bbtn2 = Button(canvas2, bg = 'black', image=c2b2, command=lambda: cam2b())
c2bbtn2.place(x= 990, y= 485)

c3btn2= Button(canvas2, bg = 'black', image=c32, command=lambda: cam3())
c3btn2.place(x= 930, y= 445)

c4abtn2 = Button(canvas2, bg = 'black', image=c4a2, command=lambda: cam4a())
c4abtn2.place(x= 1070, y= 455)

c4bbtn2 = Button(canvas2, bg = 'black', image=c4b2, command=lambda: cam4b())
c4bbtn2.place(x= 1070, y= 485)

c5btn2 = Button(canvas2, bg = 'black', image=c52, command=lambda: cam5())
c5btn2.place(x= 900, y= 335)

c7btn2 = Button(canvas2, bg = 'black', image=c72, command=lambda: cam7())
c7btn2.place(x= 1150, y= 335)

c2acambtn = Button(canvas2, bg = 'black', image=cambtn_img, command=lambda: backoffice())
c2acambtn.place(x= 300, y= 510)



## Cam 1c ##

canvas3 = Canvas(cams1c, bg="black", width=1280, height=577)
canvas3.pack()


cove = PhotoImage(file="fnafpython2.0-main/assets/cove.png")
canvas3.create_image(640,288,image=cove)

foxyattack = PhotoImage(file="fnafpython2.0-main/assets/foxyattack.png")


foxyhome = PhotoImage(file="fnafpython2.0-main/assets/foxyhome.png")

c1abtn3 = Button(canvas3, bg = 'black', image=c1a2, command=lambda: cam1a())
c1abtn3.place(x= 990, y= 275)

c1bbtn3 = Button(canvas3, bg = 'black', image=c1b2, command=lambda: cam1b())
c1bbtn3.place(x= 975, y= 320)

c1cbtn3 = Button(canvas3, bg = 'black', image=c1c2, command=lambda: cam1c())
c1cbtn3.place(x= 950, y= 375)

c2abtn3 = Button(canvas3, bg = 'black', image=c2a2, command=lambda: cam2a())
c2abtn3.place(x= 990, y= 455)

c2bbtn3 = Button(canvas3, bg = 'black', image=c2b2, command=lambda: cam2b())
c2bbtn3.place(x= 990, y= 485)

c3btn3 =  Button(canvas3, bg = 'black', image=c32, command=lambda: cam3())
c3btn3.place(x= 930, y= 445)

c4abtn3 = Button(canvas3, bg = 'black', image=c4a2, command=lambda: cam4a())
c4abtn3.place(x= 1070, y= 455)

c4bbtn3 = Button(canvas3, bg = 'black', image=c4b2, command=lambda: cam4b())
c4bbtn3.place(x= 1070, y= 485)

c5btn3 = Button(canvas3, bg = 'black', image=c52, command=lambda: cam5())
c5btn3.place(x= 900, y= 335)

c7btn3 = Button(canvas3, bg = 'black', image=c72, command=lambda: cam7())
c7btn3.place(x= 1150, y= 335)

c3acambtn = Button(canvas3, bg = 'black', image=cambtn_img, command=lambda: backoffice())
c3acambtn.place(x= 300, y= 510)



###Cam 2a###

canvas4 = Canvas(cams2a, bg="black", width=1280, height=577)
canvas4.pack()

whall_img = PhotoImage(file="fnafpython2.0-main/assets/whall.png")
canvas4.create_image(640,288,image=whall_img)

bonhall_img = PhotoImage(file="fnafpython2.0-main/assets/bonhall.png")


c1abtn4 = Button(canvas4, bg = 'black', image=c1a2, command=lambda: cam1a())
c1abtn4.place(x= 990, y= 275)

c1bbtn4 = Button(canvas4, bg = 'black', image=c1b2, command=lambda: cam1b())
c1bbtn4.place(x= 975, y= 320)

c1cbtn4 = Button(canvas4, bg = 'black', image=c1c2, command=lambda: cam1c())
c1cbtn4.place(x= 950, y= 375)

c2abtn4 = Button(canvas4, bg = 'black', image=c2a2, command=lambda: cam2a())
c2abtn4.place(x= 990, y= 455)

c2bbtn4 = Button(canvas4, bg = 'black', image=c2b2, command=lambda: cam2b())
c2bbtn4.place(x= 990, y= 485)

c3btn4 = Button(canvas4, bg = 'black', image=c32, command=lambda: cam3())
c3btn4.place(x= 930, y= 445)

c4abtn4 = Button(canvas4, bg = 'black', image=c4a2, command=lambda: cam4a())
c4abtn4.place(x= 1070, y= 455)

c4bbtn4 = Button(canvas4, bg = 'black', image=c4b2, command=lambda: cam4b())
c4bbtn4.place(x= 1070, y= 485)

c5btn4 = Button(canvas4, bg = 'black', image=c52, command=lambda: cam5())
c5btn4.place(x= 900, y= 335)

c7btn4 = Button(canvas4, bg = 'black', image=c72, command=lambda: cam7())
c7btn4.place(x= 1150, y= 335)


c4acambtn = Button(canvas4, bg = 'black', image=cambtn_img, command=lambda: backoffice())
c4acambtn.place(x= 300, y= 510)


####Cam 2b####

canvas5= Canvas(cams2b, bg="black", width=1280, height=577)
canvas5.pack()

whallcorner_img = PhotoImage(file="fnafpython2.0-main/assets/whallcorner.png")
canvas5.create_image(640,288,image=whallcorner_img)

boncorner_img = PhotoImage(file="fnafpython2.0-main/assets/boncorner.png")


markcorner_img = PhotoImage(file="fnafpython2.0-main/assets/markcorner.png")


c1abtn5 = Button(canvas5, bg = 'black', image=c1a2, command=lambda: cam1a())
c1abtn5.place(x= 990, y= 275)

c1bbtn5 = Button(canvas5, bg = 'black', image=c1b2, command=lambda: cam1b())
c1bbtn5.place(x= 975, y= 320)

c1cbtn5 = Button(canvas5, bg = 'black', image=c1c2, command=lambda: cam1c())
c1cbtn5.place(x= 950, y= 375)

c2abtn5 = Button(canvas5, bg = 'black', image=c2a2, command=lambda: cam2a())
c2abtn5.place(x= 990, y= 455)

c2bbtn5 = Button(canvas5, bg = 'black', image=c2b2, command=lambda: cam2b())
c2bbtn5.place(x= 990, y= 485)

c3btn5 = Button(canvas5, bg = 'black', image=c32, command=lambda: cam3())
c3btn5.place(x= 930, y= 445)

c4abtn5 = Button(canvas5, bg = 'black', image=c4a2, command=lambda: cam4a())
c4abtn5.place(x= 1070, y= 455)

c4bbtn5 = Button(canvas5, bg = 'black', image=c4b2, command=lambda: cam4b())
c4bbtn5.place(x= 1070, y= 485)

c5btn5 = Button(canvas5, bg = 'black', image=c52, command=lambda: cam5())
c5btn5.place(x= 900, y= 335)

c7btn5 = Button(canvas5, bg = 'black', image=c72, command=lambda: cam7())
c7btn5.place(x= 1150, y= 335)


c5acambtn = Button(canvas5, bg = 'black', image=cambtn_img, command=lambda: backoffice())
c5acambtn.place(x= 300, y= 510)



####Cam 3####

canvas6 = Canvas(cams3, bg="black", width=1280, height=577)
canvas6.pack()

closet_img = PhotoImage(file="fnafpython2.0-main/assets/closet.png")
canvas6.create_image(640,288, image=closet_img)

boncloset_img = PhotoImage(file="fnafpython2.0-main/assets/boncloset.png")


c1abtn6 = Button(canvas6, bg = 'black', image=c1a2, command=lambda: cam1a())
c1abtn6.place(x= 990, y= 275)

c1bbtn6 = Button(canvas6, bg = 'black', image=c1b2, command=lambda: cam1b())
c1bbtn6.place(x= 975, y= 320)

c1cbtn6 = Button(canvas6, bg = 'black', image=c1c2, command=lambda: cam1c())
c1cbtn6.place(x= 950, y= 375)

c2abtn6 = Button(canvas6, bg = 'black', image=c2a2, command=lambda: cam2a())
c2abtn6.place(x= 990, y= 455)

c2bbtn6 = Button(canvas6, bg = 'black', image=c2b2, command=lambda: cam2b())
c2bbtn6.place(x= 990, y= 485)

c3btn6= Button(canvas6, bg = 'black', image=c32, command=lambda: cam3())
c3btn6.place(x= 930, y= 445)

c4abtn6 = Button(canvas6, bg = 'black', image=c4a2, command=lambda: cam4a())
c4abtn6.place(x= 1070, y= 455)

c4bbtn6 = Button(canvas6, bg = 'black', image=c4b2, command=lambda: cam4b())
c4bbtn6.place(x= 1070, y= 485)

c5btn6 = Button(canvas6, bg = 'black', image=c52, command=lambda: cam5())
c5btn6.place(x= 900, y= 335)

c7btn6 = Button(canvas6, bg = 'black', image=c72, command=lambda: cam7())
c7btn6.place(x= 1150, y= 335)

c6acambtn = Button(canvas6, bg = 'black', image=cambtn_img, command=lambda: backoffice())
c6acambtn.place(x= 300, y= 510)



#### Cam 4a####
canvas7 = Canvas(cams4a, bg="black", width=1280, height=577)
canvas7.pack()


ehall_img= PhotoImage(file="fnafpython2.0-main/assets/ehall.png")
canvas7.create_image(640,288,image=ehall_img)

chicaehall_img= PhotoImage(file="fnafpython2.0-main/assets/chicaehall.png")


c1abtn7 = Button(canvas7, bg = 'black', image=c1a2, command=lambda: cam1a())
c1abtn7.place(x= 990, y= 275)

c1bbtn7 = Button(canvas7, bg = 'black', image=c1b2, command=lambda: cam1b())
c1bbtn7.place(x= 975, y= 320)

c1cbtn7 = Button(canvas7, bg = 'black', image=c1c2, command=lambda: cam1c())
c1cbtn7.place(x= 950, y= 375)

c2abtn7 = Button(canvas7, bg = 'black', image=c2a2, command=lambda: cam2a())
c2abtn7.place(x= 990, y= 455)

c2bbtn7 = Button(canvas7, bg = 'black', image=c2b2, command=lambda: cam2b())
c2bbtn7.place(x= 990, y= 485)

c3btn7= Button(canvas7, bg = 'black', image=c32, command=lambda: cam3())
c3btn7.place(x= 930, y= 445)

c4abtn7 = Button(canvas7, bg = 'black', image=c4a2, command=lambda: cam4a())
c4abtn7.place(x= 1070, y= 455)

c4bbtn7 = Button(canvas7, bg = 'black', image=c4b2, command=lambda: cam4b())
c4bbtn7.place(x= 1070, y= 485)

c5btn7 = Button(canvas7, bg = 'black', image=c52, command=lambda: cam5())
c5btn7.place(x= 900, y= 335)

c7btn7 = Button(canvas7, bg = 'black', image=c72, command=lambda: cam7())
c7btn7.place(x= 1150, y= 335)

c7acambtn = Button(canvas7, bg = 'black', image=cambtn_img, command=lambda: backoffice())
c7acambtn.place(x= 300, y= 510)



####Cam 4b####
canvas8 = Canvas(cams4b, bg="black", width=1280, height=577)
canvas8.pack()

ehallcorner_img= PhotoImage(file="fnafpython2.0-main/assets/ehallcorner.png")
canvas8.create_image(640,288,image=ehallcorner_img)

chicacorner_img= PhotoImage(file="fnafpython2.0-main/assets/chicacorner.png")


fredcorner_img = PhotoImage(file="fnafpython2.0-main/assets/fredcorner.png")

c1abtn8 = Button(canvas8, bg = 'black', image=c1a2, command=lambda: cam1a())
c1abtn8.place(x= 990, y= 275)

c1bbtn8 = Button(canvas8, bg = 'black', image=c1b2, command=lambda: cam1b())
c1bbtn8.place(x= 975, y= 320)

c1cbtn8 = Button(canvas8, bg = 'black', image=c1c2, command=lambda: cam1c())
c1cbtn8.place(x= 950, y= 375)

c2abtn8 = Button(canvas8, bg = 'black', image=c2a2, command=lambda: cam2a())
c2abtn8.place(x= 990, y= 455)

c2bbtn8 = Button(canvas8, bg = 'black', image=c2b2, command=lambda: cam2b())
c2bbtn8.place(x= 990, y= 485)

c3btn8= Button(canvas8, bg = 'black', image=c32, command=lambda: cam3())
c3btn8.place(x= 930, y= 445)

c4abtn8 = Button(canvas8, bg = 'black', image=c4a2, command=lambda: cam4a())
c4abtn8.place(x= 1070, y= 455)

c4bbtn8 = Button(canvas8, bg = 'black', image=c4b2, command=lambda: cam4b())
c4bbtn8.place(x= 1070, y= 485)

c5btn8 = Button(canvas8, bg = 'black', image=c52, command=lambda: cam5())
c5btn8.place(x= 900, y= 335)

c7btn8 = Button(canvas8, bg = 'black', image=c72, command=lambda: cam7())
c7btn8.place(x= 1150, y= 335)

c8acambtn = Button(canvas8, bg = 'black', image=cambtn_img, command=lambda: backoffice())
c8acambtn.place(x= 300, y= 510)



## Cam 5 ##

canvas9 = Canvas(cams5, bg="black", width=1280, height=577)
canvas9.pack()


backstage = PhotoImage(file="fnafpython2.0-main/assets/partservice.png")
canvas9.create_image(640,288,image=backstage)

bonparts = PhotoImage(file="fnafpython2.0-main/assets/bonparts.png")


c1abtn9 = Button(canvas9, bg = 'black', image=c1a2, command=lambda: cam1a())
c1abtn9.place(x= 990, y= 275)

c1bbtn9 = Button(canvas9, bg = 'black', image=c1b2, command=lambda: cam1b())
c1bbtn9.place(x= 975, y= 320)

c1cbtn9 = Button(canvas9, bg = 'black', image=c1c2, command=lambda: cam1c())
c1cbtn9.place(x= 950, y= 375)

c2abtn9 = Button(canvas9, bg = 'black', image=c2a2, command=lambda: cam2a())
c2abtn9.place(x= 990, y= 455)

c2bbtn9 = Button(canvas9, bg = 'black', image=c2b2, command=lambda: cam2b())
c2bbtn9.place(x= 990, y= 485)

c3btn9= Button(canvas9, bg = 'black', image=c32, command=lambda: cam3())
c3btn9.place(x= 930, y= 445)

c4abtn9 = Button(canvas9, bg = 'black', image=c4a2, command=lambda: cam4a())
c4abtn9.place(x= 1070, y= 455)

c4bbtn9 = Button(canvas9, bg = 'black', image=c4b2, command=lambda: cam4b())
c4bbtn9.place(x= 1070, y= 485)

c5btn9 = Button(canvas9, bg = 'black', image=c52, command=lambda: cam5())
c5btn9.place(x= 900, y= 335)

c7btn9 = Button(canvas9, bg = 'black', image=c72, command=lambda: cam7())
c7btn9.place(x= 1150, y= 335)

c9acambtn = Button(canvas9, bg = 'black', image=cambtn_img, command=lambda: backoffice())
c9acambtn.place(x= 300, y= 510)



## Cam 7 ##

canvas10 = Canvas(cams7, bg="black", width=1280, height=577)
canvas10.pack()


bath = PhotoImage(file="fnafpython2.0-main/assets/bath.png")
canvas10.create_image(640,288,image=bath)

chicabath = PhotoImage(file="fnafpython2.0-main/assets/chicabath.png")


fredbath = PhotoImage(file="fnafpython2.0-main/assets/fredbath.png")


c1abtn10 = Button(canvas10, bg = 'black', image=c1a2, command=lambda: cam1a())
c1abtn10.place(x= 990, y= 275)

c1bbtn10 = Button(canvas10, bg = 'black', image=c1b2, command=lambda: cam1b())
c1bbtn10.place(x= 975, y= 320)

c1cbtn10 = Button(canvas10, bg = 'black', image=c1c2, command=lambda: cam1c())
c1cbtn10.place(x= 950, y= 375)

c2abtn10 = Button(canvas10, bg = 'black', image=c2a2, command=lambda: cam2a())
c2abtn10.place(x= 990, y= 455)

c2bbtn10 = Button(canvas10, bg = 'black', image=c2b2, command=lambda: cam2b())
c2bbtn10.place(x= 990, y= 485)

c3btn10= Button(canvas10, bg = 'black', image=c32, command=lambda: cam3())
c3btn10.place(x= 930, y= 445)

c4abtn10 = Button(canvas10, bg = 'black', image=c4a2, command=lambda: cam4a())
c4abtn10.place(x= 1070, y= 455)

c4bbtn10 = Button(canvas10, bg = 'black', image=c4b2, command=lambda: cam4b())
c4bbtn10.place(x= 1070, y= 485)

c5btn10 = Button(canvas10, bg = 'black', image=c52, command=lambda: cam5())
c5btn10.place(x= 900, y= 335)

c7btn10 = Button(canvas10, bg = 'black', image=c72, command=lambda: cam7())
c7btn10.place(x= 1150, y= 335)

c10acambtn = Button(canvas10, bg = 'black', image=cambtn_img, command=lambda: backoffice())
c10acambtn.place(x= 300, y= 510)

bonlvl = 3
chiclvl = 1
fredlvl = 0
foxlvl = 0
marklvl = 0

def nightselect():
    global bonlvl, chiclvl, fredlvl, foxlvl, marklvl
    if night == 1:
        bonlvl = 4
        chiclvl = 2
        fredlvl = 1
        foxlvl = 1
        marklvl = 1
    elif night == 2:
        bonlvl = 4
        chiclvl = 4
        fredlvl = 1
        foxlvl = 1
        marklvl = 1
    elif night == 3:
        bonlvl = 5
        chiclvl = 4
        fredlvl = 3
        foxlvl = 2
        marklvl = 2
    elif night == 4:
        bonlvl = 6
        chiclvl = 5
        fredlvl = 7
        foxlvl = 3
        marklvl = 3
    elif night == 5:
        bonlvl = 7
        chiclvl = 7
        fredlvl = 9
        foxlvl = 4
        marklvl = 5
    elif night == 6:
        bonlvl = 10
        chiclvl = 10
        fredlvl = 12
        foxlvl = 5
        marklvl = 6
    thread.start()
    
    

freddyroom = ["stage","dining","bathroom","east hall","east hall corner","office",] #These are lists of the possible locations, and a number to keep track of where they are from the indexes.
fredloc = 0
bonnieroom = ["stage", "dining","parts and services","west hall","closet","east hall corner","office"]
bonloc = 0
chicaroom= ["stage", "dining", "bathroom","east hall","east hall corner", "office"]
chicaloc = 0
foxyroom = ["cove", "office"]
foxyloc = 0
markloc = 0
goldloc = 0
dead = 0

def gamestart():
    global dead,officeimg, page, chica_doorimg,bonnie_doorimg,mark_doorimg,goldenfred_officeimg,foxy_doorimg,goldloc,fredbath, fredcorner_img,freddin,fredloc, fredlvl, fredstage, boncloset_img,boncorner_img,bondin,bonloc,bonlvl, bonparts, bonstage,bonhall_img ,chicabath,chicacorner_img,chicadin,chicaehall_img,chicaloc ,chiclvl,foxlvl,foxyattack, foxyhome,foxyloc,stage,dinning,backstage,bath,whall_img,whallcorner_img,ehall_img,ehallcorner_img,closet_img,cove, markcorner_img, markloc, marklvl
    clock = 0.0
    while dead == 0:

        # LOCATION CODE ---------------------------------------------------------

        #STAGE --- 1a
        if fredloc == 0 and bonloc == 0:
            canvas.create_image(640,288,image=fredstage)
            canvas.create_image(640,288,image=bonstage)
        elif fredloc == 0:
            canvas.delete('all')
            canvas.create_image(640,288,image=stage)
            canvas.create_image(640,288,image=fredstage)
        elif bonloc == 0:
            canvas.delete('all')
            canvas.create_image(640,288,image=stage)
            canvas.create_image(640,288,image=bonstage)
        else:
            canvas.delete('all')
            canvas.create_image(640,288,image=stage)

        #DINNING --- 1b
        if fredloc == 1 and bonloc == 1 and chicaloc == 1:
            canvas2.create_image(640,288,image=freddin)
            canvas2.create_image(640,288,image=chicadin)
            canvas2.create_image(640,288,image=bondin)
        elif fredloc == 1 and bonloc == 1 :
            canvas2.delete('all')
            canvas2.create_image(640,288,image=dinning)
            canvas2.create_image(640,288,image=freddin)
        
            canvas2.create_image(640,288,image=bondin)
        elif fredloc == 1 and chicaloc == 1 :
            canvas2.delete('all')
            canvas2.create_image(640,288,image=dinning)
            canvas2.create_image(640,288,image=freddin)
        
            canvas2.create_image(640,288,image=chicadin)
        elif chicaloc == 1 and bonloc == 1 :
            canvas2.delete('all')
            canvas2.create_image(640,288,image=dinning)
            canvas2.create_image(640,288,image=chicadin)
        
            canvas2.create_image(640,288,image=bondin)
        elif fredloc == 1:
            canvas2.delete('all')
            canvas2.create_image(640,288,image=dinning)
            canvas2.create_image(640,288,image=freddin)
        elif chicaloc == 1:
            canvas2.delete('all')
            canvas2.create_image(640,288,image=dinning)
            canvas2.create_image(640,288,image=chicadin)
        elif bonloc == 1:
            canvas2.delete('all')
            canvas2.create_image(640,288,image=dinning)
            canvas2.create_image(640,288,image=bondin)
        else:
            canvas2.delete('all')
            canvas2.create_image(640,288,image=dinning)

    
    
    
    
    
        #Cove --- 1c
        if foxyloc == 0:
            canvas3.delete('all')
            canvas3.create_image(640,288,image=cove)
            canvas3.create_image(640,288,image=foxyhome)
        elif foxyloc == 1:
            canvas3.delete('all')
            canvas3.create_image(640,288,image=cove)
            canvas3.create_image(640,288,image=foxyattack)
        else:
            canvas3.delete('all')
            canvas3.create_image(640,288,image=cove)

        #Lhall --- 2a

        if bonloc == 3:
            canvas4.create_image(640,288,image=bonhall_img)
        else:
            canvas4.delete('all')
            canvas4.create_image(640,288,image=whall_img)
    
        #Lhallcorner --- 2b

        if bonloc == 5 and markloc == 1:
            canvas5.create_image(640,288,image=boncorner_img)
            canvas5.create_image(640,288,image=markcorner_img)
        elif bonloc == 5:
            canvas5.delete('all')
            canvas5.create_image(640,288,image=whallcorner_img) 
            canvas5.create_image(640,288,image=boncorner_img) 
        elif markloc == 1:
            canvas5.delete('all')
            canvas5.create_image(640,288,image=whallcorner_img) 
            canvas5.create_image(640,288,image=markcorner_img)
        else:
            canvas5.delete('all')
            canvas5.create_image(640,288,image=whallcorner_img)
    
        #closet --- 3
        if bonloc == 4:
            canvas6.create_image(640,288, image=boncloset_img)
        else:
            canvas6.delete('all')
            canvas6.create_image(640,288, image=closet_img)

        #rhall --- 4a

        if chicaloc == 4:
            canvas7.create_image(640,288,image=chicaehall_img)
        else:
            canvas7.delete('all')
            canvas7.create_image(640,288,image=ehall_img)

        #rhallcorner --- 4b

        if chicaloc == 5 and fredloc == 5:
            canvas8.create_image(640,288,image=chicacorner_img)
            canvas8.create_image(640,288,image=fredcorner_img)
        elif chicaloc == 5:
            canvas8.delete('all')
            canvas8.create_image(640,288,image=ehallcorner_img)
            canvas8.create_image(640,288,image=chicacorner_img)
        elif fredloc == 5:
            canvas8.delete('all')
            canvas8.create_image(640,288,image=ehallcorner_img)
            canvas8.create_image(640,288,image=fredcorner_img)
        else:
            canvas8.delete('all')
            canvas8.create_image(640,288,image=ehallcorner_img)
    
        #partservice --- 5

        if bonloc == 2:
            canvas9.create_image(640,288,image=bonparts)
        else:
            canvas9.delete('all')
            canvas9.create_image(640,288,image=backstage)

        #bathroom --- 7
        if chicaloc == 2 and fredloc == 2:
            canvas10.create_image(640,288,image=chicabath)
            canvas10.create_image(640,288,image=fredbath)
        elif chicaloc == 2:
            canvas10.delete('all')
            canvas10.create_image(640,288,image=bath)
            canvas10.create_image(640,288,image=chicabath)
        elif fredloc == 2:
            canvas10.delete('all')
            canvas10.create_image(640,288,image=bath)
            canvas10.create_image(640,288,image=fredbath)
        else:
            canvas10.delete('all')
            canvas10.create_image(640,288,image=bath)
        

        #office

        if bonloc == 6 and foxyloc == 2 and chicaloc == 6 and markloc == 2 and goldloc == 1:
            office_canvas.create_image(640,288, image=chica_doorimg)
            office_canvas.create_image(640,288, image=bonnie_doorimg)
            office_canvas.create_image(640,288, image=foxy_doorimg)
            office_canvas.create_image(640,288, image=mark_doorimg)
            office_canvas.create_image(640,288, image=goldenfred_officeimg)
        elif bonloc == 6 and foxyloc == 2 and chicaloc == 6 and markloc == 2:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=chica_doorimg)
            office_canvas.create_image(640,288, image=bonnie_doorimg)
            office_canvas.create_image(640,288, image=foxy_doorimg)
            office_canvas.create_image(640,288, image=mark_doorimg)
        elif bonloc == 6 and foxyloc == 2 and chicaloc == 6:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=chica_doorimg)
            office_canvas.create_image(640,288, image=bonnie_doorimg)
            office_canvas.create_image(640,288, image=foxy_doorimg)
            
        elif bonloc == 6 and foxyloc == 2:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=bonnie_doorimg)
            office_canvas.create_image(640,288, image=foxy_doorimg)
        elif bonloc == 6:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=bonnie_doorimg)
        elif foxyloc == 2 and chicaloc == 6 and markloc == 2 and goldloc == 1:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=chica_doorimg)
            office_canvas.create_image(640,288, image=foxy_doorimg)
            office_canvas.create_image(640,288, image=mark_doorimg)    
            office_canvas.create_image(640,288, image=goldenfred_officeimg)
        elif foxyloc == 2 and chicaloc == 6:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=chica_doorimg)
            office_canvas.create_image(640,288, image=foxy_doorimg)
        elif foxyloc == 2:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=foxy_doorimg)
        elif chicaloc == 6 and markloc == 2 and goldloc:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=chica_doorimg)
            office_canvas.create_image(640,288, image=mark_doorimg)
            office_canvas.create_image(640,288, image=goldenfred_officeimg)
        elif chicaloc == 6 and markloc == 2:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=chica_doorimg)
            office_canvas.create_image(640,288, image=mark_doorimg)
        elif chicaloc == 6:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=chica_doorimg)
        elif markloc == 2 and goldloc:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=mark_doorimg)
            office_canvas.create_image(640,288, image=goldenfred_officeimg)
        elif markloc == 2:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=mark_doorimg)
        elif goldloc == 1: 
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=goldenfred_officeimg)
        elif bonloc == 6 and markloc == 2:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=bonnie_doorimg)
            office_canvas.create_image(640,288, image=mark_doorimg)
        elif chicaloc == 6 and bonloc == 6:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=chica_doorimg)
            office_canvas.create_image(640,288, image=bonnie_doorimg)
        elif chicaloc == 6 and foxyloc == 2:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)
            office_canvas.create_image(640,288, image=chica_doorimg)
            office_canvas.create_image(640,288, image=foxy_doorimg)
        else:
            office_canvas.delete('all')
            office_canvas.create_image(640,288, image=officeimg)


        #MOVEMENT ----------------------------------------------------------------------------------------------------------------
        who = random.randint(0,4) #Chooses who moves at random
        if who == 0: 
            movement = random.randint(1,(2 * (bonlvl))) #This makes a number that needs to surpass a generated integer between (0,2), 
            if movement > random.randint(2,4): #The higher agressive level can make it more likely for an animatronic to move
                bonloc = bonloc + 1 #This makes them move
        if who == 1: 
            movement = random.randint(1,(2 * (fredlvl)))
            if movement > random.randint(4,8):
                fredloc = fredloc + 1
        if who == 2: 
            movement = random.randint(1,(2 * (chiclvl)))
            if movement > random.randint(2,4):
                chicaloc = chicaloc + 1
        if who == 3: 
            movement = random.randint(1,(2 * (foxlvl)))
            if movement > random.randint(4,8):
                foxyloc = foxyloc + 1

        if who == 4: 
            movement = random.randint(1,(2 * (marklvl)))
            if movement > random.randint(2,8):
                markloc = markloc + 1
    
        if clock < 60.0:
            
            office_canvas.create_image(640,288, image=clock12)

        elif clock >= 60 and clock < 120:
            
                
            office_canvas.create_image(640,288, image=clock1)
        elif clock >= 120 and clock < 180:
             
                
            office_canvas.create_image(640,288, image=clock2)
        elif clock >= 180 and clock < 240:
            
                
            office_canvas.create_image(640,288, image=clock3)
        elif clock >= 240 and clock < 300:
            
                
            office_canvas.create_image(640,288, image=clock4)
        elif clock >= 300 and clock < 360:
            
                
            office_canvas.create_image(640,288, image=clock5)
        elif clock >= 360:
            
            office_canvas.create_image(640,288, image=clock6)
            time.sleep(1)
            dead = True
        time.sleep(5)
        clock = clock + 5.0
    page = 1.0
    changePage()






thread = threading.Thread(target=gamestart)


changePage()

root.mainloop()
