# -*- coding: utf-8 -*-
"""
B1042090
B1043023
"""

import tkinter as tk
from PIL import Image, ImageTk


def switch_frame(hide,appear):
    hide.forget()
    appear.tkraise()
    appear.pack()

    
    

window = tk.Tk() #GUI 核心，需用來建立架構
window.configure(background='#ffffe0')
window.title('看見你與身體的生活對話') # GUI title 

# add = 0
# tt = tk.StringVar()
# tt.set(add)
# def enter():
#     global add
#     add += 1
#     tt.set(add)

win_width = window.winfo_screenwidth() #取得螢幕寬度
win_height = window.winfo_screenheight() #取得螢幕高度

width = 384
height = 512
left = int((win_width - width)/2) #計算左上x座標
top = int((win_height - height)/2) # 計算左上y座標
window.geometry(f'{width}x{height}+{left}+{top}') # 長寬設設定
window.resizable(False,False) #設定可否被使用者自行縮放視窗，False -> 無法調整

frame1 = tk.Frame(window,width=width,height=height,background='#ffffe0')

frame2 = tk.Frame(window,width=width,height=height,background='#ffffe0')
test = tk.Label(frame2,text='hello',font=('Arial',17,))

notes = Image.open('notes.png')
BMI = Image.open('BMI.png')
diet = Image.open('diet.png')
water = Image.open('water.png')
sleep = Image.open('sleep.png')
emotions = Image.open('emotions.png')
form = Image.open('write.png')
back = Image.open('back.png')

resized_notes = notes.resize((40,40))
resized_BMI = BMI.resize((40,40))
resized_diet = diet.resize((40,40))
resized_water = water.resize((40,40))
resized_sleep = sleep.resize((40,40))
resized_emotions = emotions.resize((40,40))
resized_form = form.resize((55,55))
resized_back = back.resize((12,12))

tk_notes = ImageTk.PhotoImage(resized_notes)
tk_BMI = ImageTk.PhotoImage(resized_BMI)
tk_diet = ImageTk.PhotoImage(resized_diet)
tk_water = ImageTk.PhotoImage(resized_water)
tk_sleep = ImageTk.PhotoImage(resized_sleep)
tk_emotions = ImageTk.PhotoImage(resized_emotions)
tk_form = ImageTk.PhotoImage(resized_form)
tk_back = ImageTk.PhotoImage(resized_back)

btna = tk.Button(frame1,cursor="heart", text= '今日紀錄',width=140,font=('Arial',17,),padx=5,pady=5,relief='ridge',bd=3,image=tk_notes,compound='left',bg='#ffffff',command=lambda:switch_frame(frame1, frame2))
btnb = tk.Button(frame1,cursor="heart", text= 'BMI趨勢',width=140,font=('Arial',17,),padx=5,pady=5,relief='ridge',bd=3,image=tk_BMI,compound='left',bg='#ffffff')
btnc = tk.Button(frame1,cursor="heart", text= '睡眠分析',width=140,font=('Arial',17,),padx=5,pady=5,relief='ridge',bd=3,image=tk_sleep,compound='left',bg='#ffffff')
btnd = tk.Button(frame1,cursor="heart", text= '飲食建議',width=140,font=('Arial',17,),padx=5,pady=5,relief='ridge',bd=3,image=tk_diet,compound='left',bg='#ffffff')
btne = tk.Button(frame1,cursor="heart", text= '喝水提醒',width=140,font=('Arial',17,),padx=5,pady=5,relief='ridge',bd=3,image=tk_water,compound='left',bg='#ffffff')
btnf = tk.Button(frame1,cursor="heart", text= '心情趨勢',width=140,font=('Arial',17,),padx=5,pady=5,relief='ridge',bd=3,image=tk_emotions,compound='left',bg='#ffffff')
btng = tk.Button(frame1,anchor='center',cursor="heart", text= '填寫今日資料',width=270,heigh=110,font=('Arial',25,),padx=5,pady=5,relief='ridge',bd=3,image=tk_form,compound='left',bg='#ffffff',command=lambda:switch_frame(frame1, frame2))


str_weight = tk.StringVar()
str_weight.set('')
str_height = tk.StringVar()
str_height.set('')
str_drink = tk.StringVar()
str_drink.set('')
str_sleep = tk.StringVar()
str_sleep.set('')
str_journal = tk.StringVar()
str_journal.set('')
btn_frame21 = tk.Button(frame2,text= 'Back',width=50,font=('Arial',10,),padx=5,pady=5,relief='ridge',bd=3,image=tk_back,compound='left',bg='#ffffff',command=lambda:switch_frame(frame2, frame1))
btn_save = tk.Button(frame2,text= 'Save',width=6,font=('Arial',13,),padx=2,pady=2,relief='ridge',bd=3,compound='left',bg='#ffffff')
weight = tk.Label(frame2,text='體重',anchor= 'e',width=8,font=('Arial',18,),padx=5,pady=5,relief='ridge',bd=0,compound='left',background='#ffffe0')
height = tk.Label(frame2,text='身高',anchor = 'e',width=8,font=('Arial',18,),padx=5,pady=5,relief='ridge',bd=0,compound='left',background='#ffffe0')
drink = tk.Label(frame2,text='飲水量',anchor = 'e',width=8,font=('Arial',18,),padx=5,pady=5,relief='ridge',bd=0,compound='left',background='#ffffe0')
sleep = tk.Label(frame2,text='睡眠時長',anchor = 'e',width=8,font=('Arial',18,),padx=5,pady=5,relief='ridge',bd=0,compound='left',background='#ffffe0')
journal = tk.Label(frame2,text='心情日記',anchor = 'e',width=8,font=('Arial',18,),padx=5,pady=5,relief='ridge',bd=0,compound='left',background='#ffffe0')
entry_weight = tk.Entry(frame2,width=27,textvariable= str_weight,bd=3)
entry_height = tk.Entry(frame2,width=27,textvariable= str_height,bd=3)
entry_drink = tk.Entry(frame2,width=27,textvariable= str_drink,bd=3)
entry_sleep = tk.Entry(frame2,width=27,textvariable= str_sleep,bd=3)
entry_journal = tk.Text(frame2, height = 15,width=27,bd=3)

# frame1
btna.place(relx=0.05, rely=0.1)
btnb.place(relx=0.55, rely=0.1)
btnc.place(relx=0.05, rely=0.25)
btnd.place(relx=0.55, rely=0.25)
btne.place(relx=0.05, rely=0.4)
btnf.place(relx=0.55, rely=0.4)
btng.place(relx=0.12, rely=0.6)
 
# frame2
btn_frame21.place(relx=0.01,rely=0.01)
btn_save.place(relx=0.79,rely=0.92 )
weight.place(relx=0.01,rely=0.1)
entry_weight.place(relx = 0.33,rely= 0.115)
height.place(relx=0.01,rely=0.2)
entry_height.place(relx = 0.33,rely= 0.215)
drink.place(relx=0.01,rely=0.3)
entry_drink.place(relx = 0.33,rely= 0.315)
sleep.place(relx=0.01,rely=0.4)
entry_sleep.place(relx = 0.33,rely= 0.415)
journal.place(relx=0.01,rely=0.5)
entry_journal.place(relx = 0.33,rely= 0.515)


frame1.pack()
frame2.pack()


window.mainloop() # 放在主迴圈中(沒有這行的話因為程式執行完的關係所以你甚麼都不會看到，記得要打在程式的最後一行)








