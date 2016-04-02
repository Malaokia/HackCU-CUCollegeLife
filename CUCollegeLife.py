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
import Analysis


LARGE_FONT= ("Verdana", 12)


class CUCollegeApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        refer = tk.Frame(self)
        refer.pack(side="top", fill="both", expand = True)
        refer.grid_rowconfigure(0, weight=1)
        refer.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (HomePage, QuizPage, PredictHoursPage, EnterHoursData):
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
		img = self.img = ImageTk.PhotoImage(Image.open('maxresdefault.jpg'))
		panel = Tkinter.Label(self,image=img)
		panel.pack(side = "bottom", fill = "both", expand = "yes")
		button = tk.Button(self, text="Quiz: Which Major Is Right For You?",command=lambda: controller.show_frame(QuizPage))
		button.pack()
		button2 = tk.Button(self, text="How many hours should I in the next exam?",command=lambda: controller.show_frame(PredictHoursPage))
		button2.pack()


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
        entry = Tkinter.Entry(self,textvariable=self.entryVariable, width = 50)
        entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Ex: 1 D,2 C, ...")
        entry.pack()
        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self,textvariable=self.labelVariable,fg="yellow",bg="blue",width = 50)
        self.labelVariable.set(u"Hello!")
        label.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()
        
    def OnPressEnter(self,event):
		solution = self.entryVariable.get()
		result = Analysis.infoNEW(solution)
		self.labelVariable.set(result)


class EnterHoursData(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        self.entryVariable = Tkinter.StringVar()
        entry = Tkinter.Entry(self,textvariable=self.entryVariable, width = 50)
        entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Ex: ()")
        entry.pack()

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack()
        
    def OnPressEnter(self,event):
		solution = self.entryVariable.get()
       
class PredictHoursPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = tk.Button(self, text="Would you like to input your newest test grade and hours that you put on it?",
                            command=lambda: controller.show_frame(EnterHoursData))
        button1.pack()
        self.entryVariable = Tkinter.StringVar()
        entry = Tkinter.Entry(self,textvariable=self.entryVariable, width = 50)
        entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Ex: 1 D,2 C, ...")
        entry.pack()

        button2 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button2.pack()
        
    def OnPressEnter(self,event):
		solution = self.entryVariable.get()
		


if __name__ == '__main__':
	app = CUCollegeApp()
	app.title('CUCollegeLife')
	app.mainloop()
