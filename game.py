from tkinter import *
import time

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

def select_1():
    global page
    page = 2.0
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



#### Menu ####
menuback = PhotoImage(file='assets/menu.png')
menuimg = Label(menu,image=menuback)
menuimg.pack() 
txt_night1 = Button(menu, text="Night 1", font=('Terminal',20),fg= 'white', bg= 'black', command=lambda: select_1())
txt_night1.place(x= 76, y= 370)
txt_night2 = Button(menu, text="Night 2", font=('Terminal',20),fg= 'white', bg= 'black', command=lambda: select_1())
txt_night2.place(x= 236, y=370)
txt_night3 = Button(menu, text="Night 3", font=('Terminal',20),fg= 'white', bg= 'black', command=lambda: select_1())
txt_night3.place(x= 76, y=410)
txt_night4 = Button(menu, text="Night 4", font=('Terminal',20),fg= 'white', bg= 'black', command=lambda: select_1())
txt_night4.place(x= 236, y=410)
txt_night5 = Button(menu, text="Night 5", font=('Terminal',20),fg= 'white', bg= 'black', command=lambda: select_1())
txt_night5.place(x= 76, y=450)
txt_night6 = Button(menu, text="Night 6", font=('Terminal',20),fg= 'red', bg= 'black', command=lambda: select_1())
txt_night6.place(x= 236, y=450)

#### Office ####
office_canvas = Canvas(office, bg='grey', width=1280, height=577)
office_canvas.pack()

officeimg = PhotoImage(file='assets/office.png')
office_canvas.create_image(640,288, image=officeimg)


lightleft_img = PhotoImage(file='assets/lightleft.png')
if lightleft_toggle == True:
    office_canvas.create_image(640,288, image=lightleft_img)



lightright_img = PhotoImage(file='assets/lightright.png')

if lightright_toggle == True:
    office_canvas.create_image(640,288, image=lightright_img)

btnleftdr_img = PhotoImage(file='assets/btnleftdr.png')
office_canvas.create_image(640,288, image=btnleftdr_img)

btnleftlit_img = PhotoImage(file='assets/btnleftlit.png')
office_canvas.create_image(640,288, image=btnleftlit_img)

btnrightdr_img = PhotoImage(file='assets/btnrightdr.png')
office_canvas.create_image(630,288, image=btnrightdr_img)

btnrightlit_img = PhotoImage(file='assets/btnrightlit.png')
office_canvas.create_image(630,288, image=btnrightlit_img)

chica_doorimg = PhotoImage(file='assets/chica_door.png')
office_canvas.create_image(640,288, image=chica_doorimg)

foxy_doorimg = PhotoImage(file='assets/foxy_door.png')
# office_canvas.create_image(640,288, image=foxy_doorimg) [Hiding Foxy for now]

goldenfred_officeimg = PhotoImage(file='assets/goldenfred_office.png')
office_canvas.create_image(640,288, image=goldenfred_officeimg)

mark_doorimg = PhotoImage(file='assets/mark_door.png')
office_canvas.create_image(640,288, image=mark_doorimg)

bonnie_doorimg = PhotoImage(file='assets/bonnie_door.png')
office_canvas.create_image(640,288, image=bonnie_doorimg )

cambtn_img = PhotoImage(file='assets/cambtn2.png')
officecambtn = Button(office, bg = 'black', image=cambtn_img, command=lambda: camoffice())
officecambtn.place(x= 320, y= 510)


door_leftimg = PhotoImage(file='assets/door_left.png')
if doorleft_toggle == True:
    office_canvas.create_image(640,288, image=door_leftimg)

door_rightimg = PhotoImage(file='assets/door_right.png')
if doorright_toggle == True:
    office_canvas.create_image(640,288, image=door_rightimg)
#### Cameras ####


#### Camera 1a####

canvas = Canvas(cams1a, bg="black", width=1280, height=577)
canvas.pack()


stage = PhotoImage(file="assets/stage.png")
canvas.create_image(640,288,image=stage)

fredstage = PhotoImage(file="assets/fredstage.png")
canvas.create_image(640,288,image=fredstage)

bonstage = PhotoImage(file="assets/bonstage.png")
canvas.create_image(640,288,image=bonstage)


c1a2 = PhotoImage(file="assets/1a2.png")
c1b2 = PhotoImage(file="assets/1b2.png")
c1c2 = PhotoImage(file="assets/1c2.png")
c2a2 = PhotoImage(file="assets/2a2.png")
c2b2 = PhotoImage(file="assets/2b2.png")
c32 = PhotoImage(file="assets/32.png")
c4a2 = PhotoImage(file="assets/4a2.png")
c4b2 = PhotoImage(file='assets/4b2.png')
c52 = PhotoImage(file='assets/52.png')
c72 = PhotoImage(file='assets/72.png')

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


dinning = PhotoImage(file="assets/dinning.png")
canvas2.create_image(640,288,image=dinning)

freddin = PhotoImage(file="assets/freddin.png")
canvas2.create_image(640,288,image=freddin)

bondin = PhotoImage(file="assets/bondin.png")
canvas2.create_image(640,288,image=bondin)

chicadin = PhotoImage(file="assets/chicadin.png")
canvas2.create_image(640,288,image=chicadin)

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


cove = PhotoImage(file="assets/cove.png")
canvas3.create_image(640,288,image=cove)

foxyattack = PhotoImage(file="assets/foxyattack.png")
canvas3.create_image(640,286,image=foxyattack)

foxyhome = PhotoImage(file="assets/foxyhome.png")

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

whall_img = PhotoImage(file="assets/whall.png")
canvas4.create_image(640,288,image=whall_img)

bonhall_img = PhotoImage(file="assets/bonhall.png")
canvas4.create_image(640,288,image=bonhall_img)

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

whallcorner_img = PhotoImage(file="assets/whallcorner.png")
canvas5.create_image(640,288,image=whallcorner_img)

boncorner_img = PhotoImage(file="assets/boncorner.png")
canvas5.create_image(640,288, image=boncorner_img)

markcorner_img = PhotoImage(file="assets/markcorner.png")
canvas5.create_image(640,288,image=markcorner_img)

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

partservice_img = PhotoImage(file="assets/partservice.png")
canvas6.create_image(640,288, image=partservice_img)

boncloset_img = PhotoImage(file="assets/boncloset.png")
canvas6.create_image(640,288,image=boncloset_img)

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


ehall_img= PhotoImage(file="assets/ehall.png")
canvas7.create_image(640,288,image=ehall_img)

chicaehall_img= PhotoImage(file="assets/chicaehall.png")
canvas7.create_image(640,288,image=chicaehall_img)

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

whallcorner_img= PhotoImage(file="assets/whallcorner.png")
canvas8.create_image(640,288,image=whallcorner_img)

chicacorner_img= PhotoImage(file="assets/chicacorner.png")
canvas8.create_image(640,288, image=chicacorner_img)

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


backstage = PhotoImage(file="assets/partservice.png")
canvas9.create_image(640,288,image=backstage)

bonparts = PhotoImage(file="assets/bonparts.png")
canvas9.create_image(640,286,image=bonparts)

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


bath = PhotoImage(file="assets/bath.png")
canvas10.create_image(640,288,image=bath)

chicabath = PhotoImage(file="assets/chicabath.png")
canvas10.create_image(640,286,image=chicabath)

fredbath = PhotoImage(file="assets/fredbath.png")
canvas10.create_image(640,286,image=fredbath)

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

changePage()
root.mainloop()
