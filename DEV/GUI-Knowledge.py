from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI=Tk() #ดึงโมดูล tkinter มาใช้งาน
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')  #ปรับขนาดหนร้าจอ Program


B1 = ttk.Button(GUI,text='ช้อมูลลูกค้า') #สร้างปุ่ม
B1.pack(ipadx=50,ipady=50) #แสดงปุ่มให้อยู่ตรงกลาง


L1=Label (GUI,text="โปรแกรมบันทึกความรู้",font=('angsana New',30),fg='red')
L1.place(x=30,y=20)

#########

def Button2():
    text= 'ใส่ข้อมูลให้ครบถ้วน'
    messagebox.showinfo('ใส่ข้อมูลให้ครบถ้วน',text)
FB1=LabelFrame(GUI,text="ใส่ชื่อจริง")#สร้างปุ่ม
FB1.place(x=100,y=300)

B2=ttk.Button(FB1,text='ชื่อลูกค้า',command=Button2)
B2.pack(ipadx=20,ipady=20)

#########

#def Button3():
#    text= 'ใส่ข้อมูลให้ครบถ้วน'
 #   messagebox.showinfo('ใส่ข้อมูลให้ครบถ้วน',text)
#FB1=LabelFrame(GUI,text="ใส่ชื่อจริง")#สร้างปุ่ม
#FB1.place(x=100,y=300)

#B2=ttk.Button(FB1,text='ชื่อลูกค้า',command=Button2)
#B2.pack(ipadx=20,ipady=20)











GUI.mainloop()
