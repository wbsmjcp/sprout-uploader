from tkinter import *

window = Tk()
window.title('My Window')
window.geometry('500x300') 
 
lbl_spr_user = Label(window, text='Sprout Username')
lbl_spr_pass = Label(window, text='Sprout Password')
lbl_spr_api = Label(window, text='Sprout API Key')
lbl_ott_user = Label(window, text='Otter Username')
lbl_ott_pass = Label(window, text='Otter Password')


ent_spr_user = Entry(window, show=None, font=('Arial', 14), text='Sprout Username')  
ent_spr_pass = Entry(window, show='*', font=('Arial', 14))   
ent_spr_API = Entry(window, show=None, font=('Arial', 14))  
ent_ott_user = Entry(window, show=None, font=('Arial', 14))  
ent_ott_pass = Entry(window, show='*', font=('Arial', 14))

lbl_spr_user.pack(side=LEFT)
ent_spr_user.pack(side=RIGHT)
lbl_spr_pass.pack(side=LEFT)
ent_spr_pass.pack(side=RIGHT)
lbl_spr_api.pack(side=LEFT)
ent_spr_API.pack(side=RIGHT)
lbl_ott_user.pack(side=LEFT)
ent_ott_user.pack(side=RIGHT)
lbl_ott_pass.pack(side=LEFT)
ent_ott_pass.pack(side=RIGHT)

window.mainloop()