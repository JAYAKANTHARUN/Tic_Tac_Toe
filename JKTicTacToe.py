from tkinter import *
from tkinter import messagebox,filedialog
from PIL import ImageTk,Image
import os

def quitgame():
    messagebox.showinfo("MESSAGE","THANK YOU FOR PLAYING")
    top.destroy()

def startgame():
    global win,count,flag,button1flag,button2flag,button3flag,button4flag,button5flag,button6flag,button7flag,button8flag,button9flag
    root=Tk()

    root.title("TIC TAC TOE")
    root.configure(bg="light yellow")

    win=0
    count=0
    flag=0
    button1flag=0
    button2flag=0
    button3flag=0
    button4flag=0
    button5flag=0
    button6flag=0
    button7flag=0
    button8flag=0
    button9flag=0

    def checkwin():
        global win
        if (button1['text']=="X" and button2['text']=="X" and button3['text']=="X") or (button4['text']=="X" and button5['text']=="X" and button6['text']=="X") or (button7['text']=="X" and button8['text']=="X" and button9['text']=="X") or (button1['text']=="X" and button4['text']=="X" and button7['text']=="X") or (button2['text']=="X" and button5['text']=="X" and button8['text']=="X") or (button3['text']=="X" and button6['text']=="X" and button9['text']=="X") or (button1['text']=="X" and button5['text']=="X" and button9['text']=="X") or (button3['text']=="X" and button5['text']=="X" and button7['text']=="X"):
            messagebox.showinfo("MESSAGE","PLAYER 1 WINS")
            win=1
            root.destroy()
        elif (button1['text']=="O" and button2['text']=="O" and button3['text']=="O") or (button4['text']=="O" and button5['text']=="O" and button6['text']=="O") or (button7['text']=="O" and button8['text']=="O" and button9['text']=="O") or (button1['text']=="O" and button4['text']=="O" and button7['text']=="O") or (button2['text']=="O" and button5['text']=="O" and button8['text']=="O") or (button3['text']=="O" and button6['text']=="O" and button9['text']=="O") or (button1['text']=="O" and button5['text']=="O" and button9['text']=="O") or (button3['text']=="O" and button5['text']=="O" and button7['text']=="O"):
            messagebox.showinfo("MESSAGE","PLAYER 2 WINS")
            win=1
            root.destroy()    

    def checkdraw():
        if count==9 and win==0:
            messagebox.showinfo("MESSAGE","GAME DRAW")
            root.destroy()

    def buttonclick1():
        global flag,button1flag,count
        
        if flag==0 and button1flag==0:
            button1['text']="X"
            button1flag=1
            flag=1
            count+=1
        elif flag==1 and button1flag==0:
            button1['text']="O"
            button1flag=1
            flag=0
            count+=1
        else:
            messagebox.showerror("ERROR","INVALID SELECTION , CLICK UNCLICKED BUTTON")
        checkwin()    
        checkdraw()    
    def buttonclick2():
        global flag,button2flag,count
        
        if flag==0 and button2flag==0:
            button2['text']="X"
            button2flag=1
            flag=1
            count+=1
        elif flag==1 and button2flag==0:
            button2['text']="O"
            button2flag=1
            flag=0
            count+=1
        else:
            messagebox.showerror("ERROR","INVALID SELECTION , CLICK UNCLICKED BUTTON")
        checkwin()
        checkdraw() 
    def buttonclick3():
        global flag,button3flag,count
        
        if flag==0 and button3flag==0:
            button3['text']="X"
            button3flag=1
            flag=1
            count+=1
        elif flag==1 and button3flag==0:
            button3['text']="O"
            button3flag=1
            flag=0
            count+=1
        else:
            messagebox.showerror("ERROR","INVALID SELECTION , CLICK UNCLICKED BUTTON")
        
        checkwin()
        checkdraw() 
    def buttonclick4():
        global flag,button4flag,count
        
        if flag==0 and button4flag==0:
            button4['text']="X"
            button4flag=1
            flag=1
            count+=1
        elif flag==1 and button4flag==0:
            button4['text']="O"
            button4flag=1
            flag=0
            count+=1
        else:
            messagebox.showerror("ERROR","INVALID SELECTION , CLICK UNCLICKED BUTTON")  
        checkwin()
        checkdraw()                                
    def buttonclick5():
        global flag,button5flag,count
        
        if flag==0 and button5flag==0:
            button5['text']="X"
            button5flag=1
            flag=1
            count+=1
        elif flag==1 and button5flag==0:
            button5['text']="O"
            button5flag=1
            flag=0
            count+=1
        else:
            messagebox.showerror("ERROR","INVALID SELECTION , CLICK UNCLICKED BUTTON")
        checkwin()
        checkdraw()     
    def buttonclick6():
        global flag,button6flag,count
        
        if flag==0 and button6flag==0:
            button6['text']="X"
            button6flag=1
            flag=1
            count+=1
        elif flag==1 and button6flag==0:
            button6['text']="O"
            button6flag=1
            flag=0
            count+=1
        else:
            messagebox.showerror("ERROR","INVALID SELECTION , CLICK UNCLICKED BUTTON")
        checkwin()
        checkdraw()     
    def buttonclick7():
        global flag,button7flag,count
        
        if flag==0 and button7flag==0:
            button7['text']="X"
            button7flag=1
            flag=1
            count+=1
        elif flag==1 and button7flag==0:
            button7['text']="O"
            button7flag=1
            flag=0
            count+=1
        else:
            messagebox.showerror("ERROR","INVALID SELECTION , CLICK UNCLICKED BUTTON")  
        checkwin()
        checkdraw()                           
    def buttonclick8():
        global flag,button8flag,count
        
        if flag==0 and button8flag==0:
            button8['text']="X"
            button8flag=1
            flag=1
            count+=1
        elif flag==1 and button8flag==0:
            button8['text']="O"
            button8flag=1
            flag=0
            count+=1
        else:
            messagebox.showerror("ERROR","INVALID SELECTION , CLICK UNCLICKED BUTTON")
        checkwin()
        checkdraw()     
    def buttonclick9():
        global flag,button9flag,count
        
        if flag==0 and button9flag==0:
            button9['text']="X"
            button9flag=1
            flag=1
            count+=1
        elif flag==1 and button9flag==0:
            button9['text']="O"
            button9flag=1
            flag=0
            count+=1
        else:
            messagebox.showerror("ERROR","INVALID SELECTION , CLICK UNCLICKED BUTTON")  
        checkwin()
        checkdraw()                    

    frame1 = Frame(root,highlightbackground="saddle brown", highlightthickness=20)
    frame1.grid(padx=30,pady=30)

    button1=Button(frame1,text="  ",padx=55,pady=50,command=buttonclick1,fg="maroon",bg="khaki",font="stix")
    button2=Button(frame1,text="  ",padx=55,pady=50,command=buttonclick2,fg="maroon",bg="khaki",font="stix")
    button3=Button(frame1,text="  ",padx=55,pady=50,command=buttonclick3,fg="maroon",bg="khaki",font="stix")
    button4=Button(frame1,text="  ",padx=55,pady=50,command=buttonclick4,fg="maroon",bg="khaki",font="stix")
    button5=Button(frame1,text="  ",padx=55,pady=50,command=buttonclick5,fg="maroon",bg="khaki",font="stix")
    button6=Button(frame1,text="  ",padx=55,pady=50,command=buttonclick6,fg="maroon",bg="khaki",font="stix")
    button7=Button(frame1,text="  ",padx=55,pady=50,command=buttonclick7,fg="maroon",bg="khaki",font="stix")
    button8=Button(frame1,text="  ",padx=55,pady=50,command=buttonclick8,fg="maroon",bg="khaki",font="stix")
    button9=Button(frame1,text="  ",padx=55,pady=50,command=buttonclick9,fg="maroon",bg="khaki",font="stix")

    button1.grid(row=0,column=0)
    button2.grid(row=0,column=1)
    button3.grid(row=0,column=2)
    button4.grid(row=1,column=0)
    button5.grid(row=1,column=1)
    button6.grid(row=1,column=2)
    button7.grid(row=2,column=0)
    button8.grid(row=2,column=1)
    button9.grid(row=2,column=2)

    root.mainloop()

top=Tk()

top.title("JK TIC TAC TOE")

top.attributes("-fullscreen",True)

top.configure(bg="light yellow")

image1=PhotoImage(file="tic.png")
top.iconphoto(False,image1)

label=Label(top,text="\n\n\n",bg="light yellow").pack()
label1=Label(top,text="JK TIC TAC TOE",font=("algerian",50),fg="brown",bg="light yellow").pack()

image=Image.open("tic.jpg")
resize_image = image.resize((50,50))
img=ImageTk.PhotoImage(resize_image)
imagelabel=Label(top,image=img)
imagelabel.pack()

label=Label(top,text="\n\n",bg="light yellow").pack()
label2=Label(top,text="\n\nPLAYER 1 --> X",font=("algerian",25),bg="light yellow",fg="maroon").pack(anchor=CENTER)
label3=Label(top,text="PLAYER 2 --> O",font=("algerian",25),bg="light yellow",fg="maroon").pack(anchor=CENTER)

label8=Label(top,text="\n\n\n\n",bg="light yellow").pack()
button2=Button(top,text="\nSTART THE GAME\n",bg="tan",command=startgame,width=20).pack()
label9=Label(top,text="\n\n\n",bg="light yellow").pack()
button3=Button(top,text="\nQUIT GAME\n",bg="tan",command=quitgame,width=20).pack()

top.mainloop()    