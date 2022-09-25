
# importing whole module

from tkinter import *
from tkinter import ttk
from threading import Thread
import time
import datetime
import winsound
from tkinter import filedialog 
from tkinter import messagebox
# importing strftime function to
# retrieve system's time

from time import strftime
from os import path
import os
import pyAesCrypt
# creating tkinter window

root = Tk()

root.title('Clock')
class encryption:
    def __init__(self,root,cwd):
        self.root = root
        self.cwd = cwd
        self.st = ""
        
        self.top = Toplevel()
        self.top.title('Encryption')
        self.top.geometry("700x500+500+200")
        ##Label(self.top,text = "hi").pack()
        button_frame = Frame(self.top)
        button_frame.grid(row = 0,column = 0,sticky = "w")
        button1 = ttk.Button(button_frame,text = "Upload",command = self.upload)
        button1.grid(row = 0,column = 0,sticky = "w")
        button2 = ttk.Button(button_frame,text = "Decrypt",command = self.decrypt)
        button2.grid(row = 0,column = 1,padx = 10,sticky = "w")
        button3 = ttk.Button(button_frame,text = "Delete",command = self.delete)
        button3.grid(row = 0,column = 2,sticky = "w")
        
        self.listframe = Frame(self.top)
        self.listframe.grid(row = 1,column =0,sticky = "news",pady = 10)
        self.list_box = Listbox(self.listframe,selectmode = "multiple")
        self.list_box.grid(row =0,column = 0,sticky= "news")
        
        ##print(self.cwd)
        
        Grid.columnconfigure(self.top,0, weight=1)
        Grid.rowconfigure(self.top,1, weight=1)
        Grid.columnconfigure(self.listframe,0, weigh=1)
        Grid.rowconfigure(self.listframe,0, weight=1)

        os.chdir(self.cwd +"\Modules")
        j=""
        with open("mod.txt") as fp:
            for i in fp.read():
                j+=i
                if(i==" "):
                    j = j.replace(" ","")
                    self.st += chr(int(j)^5)
                    j=""
        
        self.top.mainloop()
    """def notfound(self):
        pass_input = Toplevel()
        pass_input.title("create password")
        pass_input.geometry("450x250+500+200")
        pass_input.resizable(0,0)
        #pass_input.grab_set()
        #pass_input.attributes("-topmost", True)
        label_frame = ttk.LabelFrame(pass_input)
        label_frame.pack()

        pass_label = ttk.Label(label_frame,text = "Create new passward").grid(row = 0,column = 0)
        pass_text = ttk.Entry(label_frame,width = 30)
        pass_text.grid(row = 0,column =1,ipadx = "10")
        enter_button = ttk.Button(label_frame,text = "Create",command = lambda : self.writing(pass_text,pass_input)).grid(row = 1,column = 0)
        condition = ttk.Label(label_frame,text = "1.Create atleast  10 digit passward\n2.Only numbers and (dot) are allowed")
        condition.grid(row = 2,column = 0)


        pass_input.mainloop()
    def writing(self,val,toplevel):
        #creating Module folder if it is not exist 
        try:
            os.mkdir(os.getcwd() + r"\Modules")
        except:
            pass
        #changing current writing directory to Module
        try:
            os.chdir(os.getcwd() + r"\Modules")
        except:
            pass
        #importing from entry box to val variable
        val = val.get()
        # rules for creating password:
        #1. should be atleast 10 digit
        #2.should not contail and alphabet of other symbol
        #here checking whether length of password is more than equal to 10 
        if len(val) >= 10:
            #Checking wether password contaning only digits or not
            if all([True if i in ["0","1","2","3","4","5","6","7","8","9","."] else False for i in val]):
                st = val
                #writing password to mod.txt file after performing xor by 5
                #adding " " so that passward does not mix up in txt file
                with open("mod.txt","w") as fp:
                    for i in val:
                        if(i == "."):
                            fp.write(str(ord(i)^5)+" ")
                        else:
                            fp.write(str(int(i) ^ 5)+ " ")
                    fp.close()
                    toplevel.destroy()
            else:
                #if any rule for not followed during creation of password then show message box
                messagebox.showerror("Wrong","1.create 10 digit passward\n2. only number and .(dot) are allowed 1")
        else:
            #if any rule for not followed during creation of password then show message box
            messagebox.showerror("Wrong","1.create atleast 10 digit passward\n2. only number and .(dot) are allowed 2")"""
    def upload(self):
        paths = filedialog.askopenfilenames(title="select file")
        os.chdir(self.cwd + "\cashe")
        for item in paths:
            #cresting buffer 
            bufferSize = 64 * 1024
            #storing user password to a variable
            password = self.st
            # encrypting using pyAesCrypt API
            pyAesCrypt.encryptFile(item,path.basename(item) + ".aes", password, bufferSize)
            #removing file from its original path
            os.remove(item)
            self.list_box.insert("end",path.basename(item)+".aes")
    def decrypt(self):
        save_as = filedialog.askdirectory()
        dec_list_nums = self.list_box.curselection()
        dec_list = self.list_box.get(0,'end')
        temp = [dec_list[item] for item in dec_list_nums]
        ##print(temp)
        os.chdir(self.cwd+"\cashe")
        for file in temp:
            bufferSize = 64 * 1024
            password = self.st
            # decrypting file using pyAesCrypt API
            pyAesCrypt.decryptFile(file, save_as + r"/" + file.replace(".aes",""), password, bufferSize)
            #removing file from cache folder
            os.remove(file)
            self.list_box.delete(dec_list.index(file))
            temp.pop(temp.index(file))
    def delete(self):
        names = self.list_box.get(0,'end')
        filename = [names[item] for item in self.list_box.curselection()]
        
        os.chdir(self.cwd+"\cashe")
        choice = messagebox.askquestion("Delete File","Are you sure want to delete this file?")
        for item in filename:
            if choice == "yes":
                for item in filename:
                    os.remove(item)
                    ##self.delete()
            else:
                pass        
class clock:
    def __init__(self,root):
        self.root = root
        self.cwd = os.getcwd()
        #self.bj2 = encryption(root)
        self.st = ""
        self.lbl = Label(root, font = ('calibri',40,'bold'),background = 'purple',foreground = 'white')
        self.lbl.pack(anchor = 'center')
        self.time()
        self.alarm_button = ttk.Button(self.root,text = "set alarm" , command =  self.alarm)
        self.alarm_button.pack(side = "left")
        self.alarmlist = []
        
        if path.isdir(self.cwd+"\cashe"):
            paths = os.listdir(self.cwd+"\cashe")
            for item in paths:
                self.list_box.insert('end',item)
        else:
            os.mkdir(self.cwd+"\cashe")
        ##print("check 1")
        if path.isdir(self.cwd+"\Modules"):
            ##print("check 2",path.isfile(self.cwd+r"\Modules\mod.txt"),self.cwd + r"\Modules\mod.txt")
            if path.isfile(self.cwd+"\Modules\mod.txt"):
                ##print("check 3")
                os.chdir(self.cwd +"\Modules")
                j=""
                with open("mod.txt") as fp:
                    for i in fp.read():
                        j+=i
                        if(i==" "):
                            j = j.replace(" ","")
                            self.st += chr(int(j)^5)
                            j=""
                ##print(self.st)
            else:
                ##print("check 4")
                self.notfound()
        else:
            ##print("check 5")
            self.notfound()
        self.root.mainloop()
    # This function is used to 
    # display time on the label

    def notfound(self):
        pass_input = Toplevel()
        pass_input.title("create password")
        pass_input.geometry("450x250+500+200")
        pass_input.resizable(0,0)
        #pass_input.grab_set()
        #pass_input.attributes("-topmost", True)
        label_frame = ttk.LabelFrame(pass_input)
        label_frame.pack()

        pass_label = ttk.Label(label_frame,text = "Create new passward").grid(row = 0,column = 0)
        pass_text = ttk.Entry(label_frame,width = 30)
        pass_text.grid(row = 0,column =1,ipadx = "10")
        enter_button = ttk.Button(label_frame,text = "Create",command = lambda : self.writing(pass_text,pass_input)).grid(row = 1,column = 0)
        condition = ttk.Label(label_frame,text = "1.Create atleast  10 digit passward\n2.Only numbers and (dot) are allowed")
        condition.grid(row = 2,column = 0)


        pass_input.mainloop()
    def writing(self,val,toplevel):
        #creating Module folder if it is not exist 
        try:
            os.mkdir(os.getcwd() + r"\Modules")
        except:
            pass
        #changing current writing directory to Module
        try:
            os.chdir(os.getcwd() + r"\Modules")
        except:
            pass
        #importing from entry box to val variable
        val = val.get()
        # rules for creating password:
        #1. should be atleast 10 digit
        #2.should not contail and alphabet of other symbol
        #here checking whether length of password is more than equal to 10 
        if len(val) >= 10:
            #Checking wether password contaning only digits or not
            self.st = val
            #writing password to mod.txt file after performing xor by 5
            #adding " " so that passward does not mix up in txt file
            with open("mod.txt","w") as fp:
                for i in val:
                    fp.write(str(ord(i)^5)+" ")
                fp.close()
                toplevel.destroy()
            
        else:
            #if any rule for not followed during creation of password then show message box
            messagebox.showerror("Wrong","create atleast 10 digit passward")
    def time(self):
        string = strftime('%H:%M:%S %p')

        self.lbl.config(text = string)

        self.lbl.after(1000, self.time)
    def Threading(self,hour,minute,second,top,label_string,list_box):
        res = all([True if self.st[i] == label_string.get()[i] else False for i in range(len(self.st))])
        if res:
            self.obj2 = encryption(self.root,self.cwd)
        else:
            
            list_box.insert('end',f"{label_string.get()} {hour.get()}:{minute.get()}:{second.get()}")
            t1=Thread(target=lambda : self.infiloop(hour,minute,second,top,list_box))
            t1.setDaemon(True)
            
            t1.start()
    def infiloop(self,hour,minute,second,top,list_box):
            self.alarmlist.append(f"{hour.get()}:{minute.get()}:{second.get()}")
            while True:
                set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"

                # Wait for one seconds
                time.sleep(1)

                # Get current time
                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                ###print(current_time,set_alarm_time)

                # Check whether set alarm is equal to current time or not
                if self.alarmlist == []:
                    break
                if current_time in self.alarmlist:
                    set_alarm_time = current_time
                    ###print("Time to Wake up")
                    # Playing sound
                    ###print(self.alarmlist)
                    #self.alarmlist.remove(self.alarmlist.index(f"{hour.get()}:{minute.get()}:{second.get()}"))
                    ###print(self.alarmlist.index(f"{hour.get()}:{minute.get()}:{second.get()}"))
                    list_box.delete(self.alarmlist.index(set_alarm_time))
                    self.alarmlist.pop(self.alarmlist.index(set_alarm_time))
                    ###print(self.alarmlist)
                    winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
                    break
            
                #top.after(1000,self.infiloop(hour,minute,second,top))
    def deletealarm(self,list_box):
    
        self.alarmlist.pop(list_box.curselection()[0])
        list_box.delete(list_box.curselection()[0])
        ##print(self.alarmlist)

    def alarm(self):
        # Infinite Loop
        top = Toplevel()
        top.title("set alarm")
        ttk.Label(top,text="Alarm Clock",font=("Helvetica 20 bold"),foreground="red").pack(pady=10)
        ttk.Label(top,text="Set Time",font=("Helvetica 15 bold")).pack()
        
        frame = Frame(top)
        frame.pack()
        
        hour = StringVar(top)
        hours = ('00', '01', '02', '03', '04', '05', '06', '07',
                '08', '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23', '24'
                )
        hour.set(hours[0])
        
        hrs = ttk.OptionMenu(frame, hour, *hours)
        hrs.pack(side=LEFT)
        
        minute = StringVar(top)
        minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
                '08', '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23',
                '24', '25', '26', '27', '28', '29', '30', '31',
                '32', '33', '34', '35', '36', '37', '38', '39',
                '40', '41', '42', '43', '44', '45', '46', '47',
                '48', '49', '50', '51', '52', '53', '54', '55',
                '56', '57', '58', '59', '60')
        minute.set(minutes[0])
        
        mins = ttk.OptionMenu(frame, minute, *minutes)
        mins.pack(side=LEFT)
        
        second = StringVar(top)
        seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
                '08', '09', '10', '11', '12', '13', '14', '15',
                '16', '17', '18', '19', '20', '21', '22', '23',
                '24', '25', '26', '27', '28', '29', '30', '31',
                '32', '33', '34', '35', '36', '37', '38', '39',
                '40', '41', '42', '43', '44', '45', '46', '47',
                '48', '49', '50', '51', '52', '53', '54', '55',
                '56', '57', '58', '59', '60')
        second.set(seconds[0])
        
        secs = ttk.OptionMenu(frame, second, *seconds)
        secs.pack(side=LEFT)
        ttk.Label(top,text = "Enter Label",font =  ('Helvetica', '16')).pack()
        label_string = StringVar()
        label_entry = Entry(top,textvariable=label_string)
        label_entry.pack()
        
        list_box = Listbox(top)
        
        ttk.Button(top,text="Set Alarm",command = lambda : self.Threading(hour, minute, second,top,label_string,list_box)).pack(pady = 10)
        ttk.Button(top,text="delete Alarm",command = lambda : self.deletealarm(list_box)).pack(pady = 10)
        ttk.Label(top,text = "Alarms are",font =  ('Helvetica', '16')).pack()
        
        list_box.pack()
        top.mainloop()
        
obj = clock(root)
#

# Placing clock at the center
# of the tkinter window


 

