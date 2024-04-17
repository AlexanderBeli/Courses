import tkinter as tk
from tkinter import ttk  # виджеты

from tkcalendar import Calendar, DateEntry

import expenses_helper as eh


class App(tk.Tk):
    def __init__(self, screenName: str | None = None, baseName: str | None = None, className: str = "Tk", useTk: bool = True, sync: bool = False, use: str | None = None) -> None:
        super().__init__(screenName, baseName, className, useTk, sync, use)
        self.title('My App')
        self['background'] = '#EBEBEB'
        self.conf = {'padx':(10, 30), 'pady':10}
        self.bold_font = 'Helvetica 13 bold'
        self.put_frames()
        
    def put_frames(self):
        self.add_form_frame = AddForm(self).grid(row=0,column=0,sticky='nswe')
        self.stat_frame = StatFrame(self).grid(row=0,column=1,sticky='nswe')
        self.table_frame = TableFrame(self).grid(row=0,column=0,columnspan=2,sticky='nswe')
        
        
class AddForm(tk.Frame):
    def __init__(self.parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        
    def put_widgets(self):
        l_most_common_text = tk.Label(frame_statistic, text="The most common item") 
        l_most_common_value = tk.Label(frame_statistic, text=eh.get_most_common_item(), font=self.master.bold_font)
        l_exp_item_text = tk.Label(frame_statistic, text="The most expensive item") 
        l_exp_item_value = tk.Label(frame_statistic, text=eh.get_most_exp_item(), font=self.master.bold_font)
        l_exp_day_text = tk.Label(frame_statistic, text="The most expensive day")
        l_exp_item_value = tk.Label(frame_statistic, text="Friday", font=self.master.bold_font)
        l_exp_month_text = tk.Label(frame_statistic, text="The most expensive month")
        l_exp_month_value = tk.Label(frame_statistic, text="July", font=self.master.bold_font)
        
        
        
app = App()
app.mainloop()