#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CUCollegeLife.py
#  
#  Copyright 2016 user <user@cu-cs-vm>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  Reference: https://pythonprogramming.net/change-show-new-frame-tkinter/
try:
	import Tkinter
except ImportError:
	raise ImportError,"The Tkinter module is required to run this program"

try:
	import ImageTk, Image
except ImportError:
	raise ImportError,"The ImageTk module is required to run this program"

import Tkinter as tk
import rw_csv
import Analysis
import ttk


LARGE_FONT= ("Verdana", 12)


class CUCollegeApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        refer = tk.Frame(self)
        refer.pack(side="top", fill="both", expand = True)
        refer.grid_rowconfigure(0, weight=1)
        refer.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (HomePage, QuizPage, PredictHoursPage, EnterHoursData, BalanceLife,LookatGraph):
            frame = F(refer, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        
class HomePage(tk.Frame):

    def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		img = self.img = ImageTk.PhotoImage(Image.open('cuboulder.jpg'))
		panel = Tkinter.Label(self,image=img)
		panel.place(x=0,y=0)
		#panel.pack(side = "bottom",fill="both",expand="yes")
		button = tk.Button(self, text="Quiz: Which Major Is Right For You?",command=lambda: controller.show_frame(QuizPage))
		button.pack()
		button2 = tk.Button(self, text="How many hours should I study for the next exam?",command=lambda: controller.show_frame(PredictHoursPage))
		button2.pack()
		button3 = tk.Button(self, text="Balance Life ",command=lambda: controller.show_frame(BalanceLife))
		button3.pack()


class QuizPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img = self.img = ImageTk.PhotoImage(Image.open('build_your_career.jpg'))
        panel = Tkinter.Label(self,image=img)
        panel.place(x="0",y="0")
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side="right", fill="y")
        result = Analysis.infoOLD()
        text_field = "Quiz: Which Major Is Right For You?\nYour last result: "+result+"\nSource: http://getcollegecredit.com/blog/article/which_major_is_right_for_you\n"
        f = open('quiz.txt','r')
        text_field = text_field + str(f.read())
        text = tk.Text(self)
        text.insert("end",text_field)
        text.pack()
        text.config(state="disabled",yscrollcommand=scrollbar.set)
        scrollbar.config(command=text.yview)
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable, width = 50)
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Ex: 1 D,2 C, ...")
        self.entry.pack()
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,justify="left",wraplength=500,fg="yellow",bg="blue",width = 80,height=10)
        self.labelVariable.set(u"Hello!")
        
        label.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()
        
    def OnPressEnter(self,event):
		solution = self.entryVariable.get()
		(trait,text) = Analysis.infoNEW(solution)
		self.labelVariable.set(trait+": "+text)


class EnterHoursData(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img = self.img = ImageTk.PhotoImage(Image.open('study_time.jpg'))
        panel = Tkinter.Label(self,image=img)
        panel.place(x=0,y=0)
        label = tk.Label(self, text="Please Enter Your Score and Hours That You Put to Study for Last Exam:", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self,textvariable=self.entryVariable, width = 50)
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Ex: 50 8")
        self.entry.pack()
        data_point = rw_csv.readStudyHrs()
        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side="right", fill="y")
        self.listbox = tk.Listbox(self)
        self.listbox.pack()
        self.listbox.insert("end", "A list of our data points:")
        for item in data_point:
			self.listbox.insert("end", str(item))
        scrollbar.config(command=self.listbox.yview)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()
        
    def OnPressEnter(self,event):
		string = self.entryVariable.get()
		item = string.split(" ")
		rw_csv.writeStudyHrs({item[0]:item[1]})
		self.listbox.insert("end",str(item))
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)
       
class PredictHoursPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        img = self.img = ImageTk.PhotoImage(Image.open('study_time.jpg'))
        panel = Tkinter.Label(self,image=img)
        panel.place(x=0,y=0)
        label = tk.Label(self, text="How many hours should I study for the next exam?", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Would you like to input your newest test grade and hours that you put on it?",
                            command=lambda: controller.show_frame(EnterHoursData))
        button1.pack()
        data_point = rw_csv.readStudyHrs()
        if len(data_point) >= 5:
			self.entryVariable = Tkinter.StringVar()
			self.entry = Tkinter.Entry(self,textvariable=self.entryVariable, width = 50)
			self.entry.bind("<Return>", self.OnPressEnter)
			self.entryVariable.set(u"Please enter the grade that you expect to have for next exam!")
			self.entry.pack()
			button2 = tk.Button(self, text="Look at Graph",command=lambda: controller.show_frame(LookatGraph))
			button2.pack()

        self.text = tk.Text(self)
        button2 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button2.pack()
        
    def OnPressEnter(self,event):
		solution = self.entryVariable.get()
		data_point = rw_csv.readStudyHrs()
		x = []
		y = []
		for point in data_point:
			x.append(int(point[0]))
			y.append(int(point[1]))
		(anal,predict_value) = Analysis.regression(x,y,int(solution))
		self.text.insert("end",anal+"You should study for "+str(predict_value)+" hours for next exam!!!")
		self.text.pack()
		self.entry.focus_set()
		self.entry.selection_range(0, Tkinter.END)
		
class BalanceLife(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Balance Life", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        result = rw_csv.readScore()
        self.tree = ttk.Treeview(self)
        self.tree["columns"]=("Family","Travel","Studying","Friend","Volunteer")
        self.tree.column("Family", width=200 )
        self.tree.column("Travel", width=200)
        self.tree.column("Studying", width=200 )
        self.tree.column("Friend", width=200)
        self.tree.column("Volunteer", width=200 )
        self.tree.heading("Family", text="Family")
        self.tree.heading("Travel", text="Travel")
        self.tree.heading("Studying", text="Studying")
        self.tree.heading("Friend", text="Friend")
        self.tree.heading("Volunteer", text="Volunteer")
        self.tree.insert("" , 0,    text="Score", values=(result["Family"],result["Travel"],result["Studying"],result["Friend"],result["Volunteer"]))
        goal = rw_csv.readGoal()
        id2 = self.tree.insert("", 1, "Task", text="Task")
        family_text = ""
        for x in goal["Family"]:
			family_text = family_text + x+ "\n"
        travel_text = ""
        for x in goal["Travel"]:
			travel_text = travel_text + x+ "\n"
        studying_text = ""
        for x in goal["Studying"]:
			studying_text = studying_text + x+"\n"
			
        friend_text = ""
        for x in goal["Friend"]:
			friend_text = friend_text + x+"\n"
        volunteer_text = ""
        for x in goal["Volunteer"]:
			volunteer_text = volunteer_text + x+"\n"
        self.tree.insert(id2, "end", text="", values=(family_text,travel_text,studying_text,friend_text,volunteer_text))
        self.tree.pack()
        self.entryVariable1 = Tkinter.StringVar()
        entry1 = Tkinter.Entry(self,textvariable=self.entryVariable1, width = 100)
        entry1.bind("<Return>", self.OnPressEnter1)
        self.entryVariable1.set(u"Enter here if you want to ADD task (Sample Format:Family-Visit grandfather 3)")
        entry1.pack()
        self.entryVariable2 = Tkinter.StringVar()
        entry2 = Tkinter.Entry(self,textvariable=self.entryVariable2, width = 100)
        entry2.bind("<Return>", self.OnPressEnter2)
        self.entryVariable2.set(u"Enter the task you have DONE from the remaining task (Sample Format:Family-Visit grandfather 3)")
        entry2.pack()   
        button1 = tk.Button(self, text="Back to Home",command=lambda: controller.show_frame(HomePage))
        button1.pack()
        img = self.img = ImageTk.PhotoImage(Image.open('BalanceLifeGraph.png'))
        self.panel = Tkinter.Label(self,image=img)     
        self.panel.pack(side = "left")
        img2 = self.img2 = ImageTk.PhotoImage(Image.open('giphy.gif'))
        self.panel2 = Tkinter.Label(self,image=img2)
        self.panel2.pack(side = "right")
        
        
    def OnPressEnter1(self,event):
		solution = self.entryVariable1.get()
		result = rw_csv.readScore()
		rw_csv.writeNewGoal(solution)
		for i in self.tree.get_children():
			self.tree.delete(i)
		self.tree.insert("" , 0,    text="Score", values=(result["Family"],result["Travel"],result["Studying"],result["Friend"],result["Volunteer"]))
		goal = rw_csv.readGoal()
		id2 = self.tree.insert("", 1, "Task", text="Task")
		family_text = ""
		for x in goal["Family"]:
			family_text = family_text + x+ "\n"
		travel_text = ""
		for x in goal["Travel"]:
			travel_text = travel_text + x+ "\n"
		studying_text = ""
		for x in goal["Studying"]:
			studying_text = studying_text + x+"\n"
		friend_text = ""
		for x in goal["Friend"]:
			friend_text = friend_text + x+"\n"
		volunteer_text = ""
		for x in goal["Volunteer"]:
			volunteer_text = volunteer_text + x+"\n"
		self.tree.insert(id2, "end", text="", values=(family_text,travel_text,studying_text,friend_text,volunteer_text))
		
	
    def OnPressEnter2(self,event):
		solution = self.entryVariable2.get()
		part = solution.split("-")
		rw_csv.deleteOldGoal(part[1])
		item = part[1].split(" ")
		score = item[len(item)-1]
		rw_csv.writeScore({part[0]:int(score)})
		for i in self.tree.get_children():
			self.tree.delete(i)
		result = rw_csv.readScore()
		self.tree.insert("" , 0,    text="Score", values=(result["Family"],result["Travel"],result["Studying"],result["Friend"],result["Volunteer"]))
		goal = rw_csv.readGoal()
		id2 = self.tree.insert("", 1, "Task", text="Task")
		family_text = ""
		for x in goal["Family"]:
			family_text = family_text + x+ "\n"
		travel_text = ""
		for x in goal["Travel"]:
			travel_text = travel_text + x+ "\n"
		studying_text = ""
		for x in goal["Studying"]:
			studying_text = studying_text + x+"\n"
		friend_text = ""
		for x in goal["Friend"]:
			friend_text = friend_text + x+"\n"
		volunteer_text = ""
		for x in goal["Volunteer"]:
			volunteer_text = volunteer_text + x+"\n"
		self.tree.insert(id2, "end", text="", values=(family_text,travel_text,studying_text,friend_text,volunteer_text))
		Analysis.makingBalanceLifeGraph(result["Family"],result["Travel"],result["Studying"],result["Friend"],result["Volunteer"])
		img = self.img = ImageTk.PhotoImage(Image.open('BalanceLifeGraph.png'))
		self.panel = Tkinter.Label(self,image=img)
		self.panel.pack(side = "left")  
		
		

class LookatGraph(tk.Frame):

    def __init__(self, parent, controller):
		tk.Frame.__init__(self,parent)
		img = self.img = ImageTk.PhotoImage(Image.open('LinearRegressionGraph.png'))
		panel = Tkinter.Label(self,image=img)
		panel.pack(side = "bottom",fill="both",expand="yes")
		button = tk.Button(self, text="HomePage",command=lambda: controller.show_frame(HomePage))
		button.pack()



if __name__ == '__main__':
	app = CUCollegeApp()
	app.title('CUCollegeLife')
	app.mainloop()
