from tkinter import *

page = 5.1

root = Tk()
root.geometry("1280x577")
root.title("FNAF PYTHON 2.0")

def changePage(root, menu, office):
    global page
    if page == 1.0:
        office.pack_forget()
        menu.pack()
    elif page == 2.0:
        menu.pack_forget()
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
txt_night1 = Label(menu, text="Night 1", font=('Terminal',20),fg= 'white', bg= 'black')
txt_night1.place(x= 76, y= 370)
txt_night2 = Label(menu, text="Night 2", font=('Terminal',20),fg= 'white', bg= 'black')
txt_night2.place(x= 236, y=370)
txt_night2 = Label(menu, text="Night 3", font=('Terminal',20),fg= 'white', bg= 'black')
txt_night2.place(x= 76, y=410)
txt_night2 = Label(menu, text="Night 4", font=('Terminal',20),fg= 'white', bg= 'black')
txt_night2.place(x= 236, y=410)
txt_night2 = Label(menu, text="Night 5", font=('Terminal',20),fg= 'white', bg= 'black')
txt_night2.place(x= 76, y=450)
txt_night2 = Label(menu, text="Night 6", font=('Terminal',20),fg= 'red', bg= 'black')
txt_night2.place(x= 236, y=450)

#### Office ####
office_canvas = Canvas(office, bg='grey', width=1280, height=577)
office_canvas.pack()

officeimg = PhotoImage(file='assets/office.png')
office_canvas.create_image(640,288, image=officeimg)

lightleft_img = PhotoImage(file='assets/lightleft.png')
office_canvas.create_image(640,288, image=lightleft_img)

lightright_img = PhotoImage(file='assets/lightright.png')
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
office_canvas.create_image(640,288, image=foxy_doorimg)

goldenfred_officeimg = PhotoImage(file='assets/goldenfred_office.png')
office_canvas.create_image(640,288, image=goldenfred_officeimg)

mark_doorimg = PhotoImage(file='assets/mark_door.png')
office_canvas.create_image(640,288, image=mark_doorimg)

bonnie_doorimg = PhotoImage(file='assets/bonnie_door.png')
office_canvas.create_image(640,288, image=bonnie_doorimg )

cambtn_img = PhotoImage(file='assets/cambtn.png')
office_canvas.create_image(640,288, image=cambtn_img)

door_leftimg = PhotoImage(file='assets/door_left.png')
office_canvas.create_image(640,288, image=door_leftimg)

door_rightimg = PhotoImage(file='assets/door_right.png')
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

c1a = PhotoImage(file="assets/1a.png")
c1b = PhotoImage(file="assets/1b.png")
c1c = PhotoImage(file="assets/1c.png")
c2a = PhotoImage(file="assets/2a.png")
c2b = PhotoImage(file="assets/2b.png")
c3 = PhotoImage(file="assets/3.png")
c4a = PhotoImage(file="assets/4a.png")
c4b = PhotoImage(file="assets/4b.png")
c5 = PhotoImage(file="assets/5.png")
c7 = PhotoImage(file="assets/7.png")
cam = PhotoImage(file="assets/cambtn.png")
camui = PhotoImage(file='assets/camui.png')

canvas.create_image(640,288,image=camui)
canvas.create_image(640,288,image=c1a)
canvas.create_image(640,288,image=c1b)
canvas.create_image(640,288,image=c1c)
canvas.create_image(640,288,image=c2a)
canvas.create_image(640,288,image=c2b)
canvas.create_image(640,288,image=c3)
canvas.create_image(640,288,image=c4a)
canvas.create_image(640,288,image=c4b)
canvas.create_image(640,288,image=c5)
canvas.create_image(640,288,image=c7)
canvas.create_image(640,288,image=cam)

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

canvas2.create_image(640,288,image=camui)
canvas2.create_image(640,288,image=c1a)
canvas2.create_image(640,288,image=c1b)
canvas2.create_image(640,288,image=c1c)
canvas2.create_image(640,288,image=c2a)
canvas2.create_image(640,288,image=c2b)
canvas2.create_image(640,288,image=c3)
canvas2.create_image(640,288,image=c4a)
canvas2.create_image(640,288,image=c4b)
canvas2.create_image(640,288,image=c5)
canvas2.create_image(640,288,image=c7)
canvas2.create_image(640,288,image=cam)

## Cam 1c ##

canvas3 = Canvas(cams1c, bg="black", width=1280, height=577)
canvas3.pack()


cove = PhotoImage(file="assets/cove.png")
canvas3.create_image(640,288,image=cove)

foxyattack = PhotoImage(file="assets/foxyattack.png")
canvas3.create_image(640,286,image=foxyattack)

foxyhome = PhotoImage(file="assets/foxyhome.png")

canvas3.create_image(640,288,image=camui)
canvas3.create_image(640,288,image=c1a)
canvas3.create_image(640,288,image=c1b)
canvas3.create_image(640,288,image=c1c)
canvas3.create_image(640,288,image=c2a)
canvas3.create_image(640,288,image=c2b)
canvas3.create_image(640,288,image=c3)
canvas3.create_image(640,288,image=c4a)
canvas3.create_image(640,288,image=c4b)
canvas3.create_image(640,288,image=c5)
canvas3.create_image(640,288,image=c7)
canvas3.create_image(640,288,image=cam)
###Cam 2a###

canvas4 = Canvas(cams2a, bg="black", width=1280, height=577)
canvas4.pack()

whall_img = PhotoImage(file="assets/whall.png")
canvas4.create_image(640,288,image=whall_img)

bonhall_img = PhotoImage(file="assets/bonhall.png")
canvas4.create_image(640,288,image=bonhall_img)

canvas4.create_image(640,288,image=camui)
canvas4.create_image(640,288,image=c1a)
canvas4.create_image(640,288,image=c1b)
canvas4.create_image(640,288,image=c1c)
canvas4.create_image(640,288,image=c2a)
canvas4.create_image(640,288,image=c2b)
canvas4.create_image(640,288,image=c3)
canvas4.create_image(640,288,image=c4a)
canvas4.create_image(640,288,image=c4b)
canvas4.create_image(640,288,image=c5)
canvas4.create_image(640,288,image=c7)
canvas4.create_image(640,288,image=cam)
####Cam 2b####

canvas5= Canvas(cams2b, bg="black", width=1280, height=577)
canvas5.pack()

whallcorner_img = PhotoImage(file="assets/whallcorner.png")
canvas5.create_image(640,288,image=whallcorner_img)

boncorner_img = PhotoImage(file="assets/boncorner.png")
canvas5.create_image(640,288, image=boncorner_img)

markcorner_img = PhotoImage(file="assets/markcorner.png")
canvas5.create_image(640,288,image=markcorner_img)

canvas5.create_image(640,288,image=camui)
canvas5.create_image(640,288,image=c1a)
canvas5.create_image(640,288,image=c1b)
canvas5.create_image(640,288,image=c1c)
canvas5.create_image(640,288,image=c2a)
canvas5.create_image(640,288,image=c2b)
canvas5.create_image(640,288,image=c3)
canvas5.create_image(640,288,image=c4a)
canvas5.create_image(640,288,image=c4b)
canvas5.create_image(640,288,image=c5)
canvas5.create_image(640,288,image=c7)
canvas5.create_image(640,288,image=cam)
####Cam 3####

canvas6 = Canvas(cams3, bg="black", width=1280, height=577)
canvas6.pack()

partservice_img = PhotoImage(file="assets/partservice.png")
canvas6.create_image(640,288, image=partservice_img)

boncloset_img = PhotoImage(file="assets/boncloset.png")
canvas6.create_image(640,288,image=boncloset_img)

canvas6.create_image(640,288,image=camui)
canvas6.create_image(640,288,image=c1a)
canvas6.create_image(640,288,image=c1b)
canvas6.create_image(640,288,image=c1c)
canvas6.create_image(640,288,image=c2a)
canvas6.create_image(640,288,image=c2b)
canvas6.create_image(640,288,image=c3)
canvas6.create_image(640,288,image=c4a)
canvas6.create_image(640,288,image=c4b)
canvas6.create_image(640,288,image=c5)
canvas6.create_image(640,288,image=c7)
canvas6.create_image(640,288,image=cam)
#### Cam 4a####
canvas7 = Canvas(cams4a, bg="black", width=1280, height=577)
canvas7.pack()

ehall_img= PhotoImage(file="assets/ehall.png")
canvas7.create_image(640,288,image=ehall_img)

chicaehall_img= PhotoImage(file="assets/chicaehall.png")
canvas7.create_image(640,288,image=chicaehall_img)

canvas7.create_image(640,288,image=camui)
canvas7.create_image(640,288,image=c1a)
canvas7.create_image(640,288,image=c1b)
canvas7.create_image(640,288,image=c1c)
canvas7.create_image(640,288,image=c2a)
canvas7.create_image(640,288,image=c2b)
canvas7.create_image(640,288,image=c3)
canvas7.create_image(640,288,image=c4a)
canvas7.create_image(640,288,image=c4b)
canvas7.create_image(640,288,image=c5)
canvas7.create_image(640,288,image=c7)
canvas7.create_image(640,288,image=cam)
####Cam 4b####
canvas8 = Canvas(cams4b, bg="black", width=1280, height=577)
canvas8.pack()

whallcorner_img= PhotoImage(file="assets/whallcorner.png")
canvas8.create_image(640,288,image=whallcorner_img)

chicacorner_img= PhotoImage(file="assets/chicacorner.png")
canvas8.create_image(640,288, image=chicacorner_img)

canvas8.create_image(640,288,image=camui)
canvas8.create_image(640,288,image=c1a)
canvas8.create_image(640,288,image=c1b)
canvas8.create_image(640,288,image=c1c)
canvas8.create_image(640,288,image=c2a)
canvas8.create_image(640,288,image=c2b)
canvas8.create_image(640,288,image=c3)
canvas8.create_image(640,288,image=c4a)
canvas8.create_image(640,288,image=c4b)
canvas8.create_image(640,288,image=c5)
canvas8.create_image(640,288,image=c7)
canvas8.create_image(640,288,image=cam)

## Cam 5 ##

canvas9 = Canvas(cams5, bg="black", width=1280, height=577)
canvas9.pack()


backstage = PhotoImage(file="assets/partservice.png")
canvas9.create_image(640,288,image=backstage)

bonparts = PhotoImage(file="assets/bonparts.png")
canvas9.create_image(640,286,image=bonparts)

canvas9.create_image(640,288,image=camui)
canvas9.create_image(640,288,image=c1a)
canvas9.create_image(640,288,image=c1b)
canvas9.create_image(640,288,image=c1c)
canvas9.create_image(640,288,image=c2a)
canvas9.create_image(640,288,image=c2b)
canvas9.create_image(640,288,image=c3)
canvas9.create_image(640,288,image=c4a)
canvas9.create_image(640,288,image=c4b)
canvas9.create_image(640,288,image=c5)
canvas9.create_image(640,288,image=c7)
canvas9.create_image(640,288,image=cam)


## Cam 7 ##

canvas10 = Canvas(cams7, bg="black", width=1280, height=577)
canvas10.pack()


bath = PhotoImage(file="assets/bath.png")
canvas10.create_image(640,288,image=bath)

chicabath = PhotoImage(file="assets/chicabath.png")
canvas10.create_image(640,286,image=chicabath)

fredbath = PhotoImage(file="assets/fredbath.png")
canvas10.create_image(640,286,image=fredbath)


canvas10.create_image(640,288,image=camui)
canvas10.create_image(640,288,image=c1a)
canvas10.create_image(640,288,image=c1b)
canvas10.create_image(640,288,image=c1c)
canvas10.create_image(640,288,image=c2a)
canvas10.create_image(640,288,image=c2b)
canvas10.create_image(640,288,image=c3)
canvas10.create_image(640,288,image=c4a)
canvas10.create_image(640,288,image=c4b)
canvas10.create_image(640,288,image=c5)
canvas10.create_image(640,288,image=c7)
canvas10.create_image(640,288,image=cam)



changePage(root,menu,office)
root.mainloop()
