from Classes import Hardware
from tkinter import *
from PIL import Image

class hardware_process:

    def view(self):
        self.hardware = Hardware()
        self.physical_cores = self.hardware.physical_cores()
        self.total_cores = self.hardware.total_cores()
        self.cpu_frequency = self.hardware.cpu_frequency()
        self.cpu_freq_min = self.cpu_frequency[0]    
        self.cpu_freq_max = self.cpu_frequency[1]    
        self.cpu_usage = self.hardware.cpu_usage()
        self.main_partition_info = self.hardware.main_partition_info()
        self.c_total = self.main_partition_info[0]
        self.c_used = self.main_partition_info[1]
        self.c_free = self.main_partition_info[2]

        self.app = Tk()
        self.app.geometry('600x600')
        self.app.title("Hardware Info")
        self.app.resizable(0 , 0)
        self.physical_cores_label = Label(self.app , text="physical cores :", font=("Arial", 30))
        self.physical_cores_label.place(x=20,y=20)
        self.total_cores_label = Label(self.app , text="total cores :", font=("Arial", 30))
        self.total_cores_label.place(x=20,y=90)
        self.cpu_freq_min_label = Label(self.app , text="cpu_freq_min :", font=("Arial", 30))
        self.cpu_freq_min_label.place(x=20,y=160)
        self.cpu_freq_max_label = Label(self.app , text="cpu_freq_max :", font=("Arial", 30))
        self.cpu_freq_max_label.place(x=20,y=230)
        self.cpu_usage_label = Label(self.app , text="cpu usage :", font=("Arial", 30))
        self.cpu_usage_label.place(x=20,y=300)
        self.c_total_label = Label(self.app , text="c drive total storage :", font=("Arial", 30))
        self.c_total_label.place(x=20,y=370)
        self.c_used_label = Label(self.app , text="c drive used storage :", font=("Arial", 30))
        self.c_used_label.place(x=20,y=440)
        self.c_free_label = Label(self.app , text="c drive free storage :", font=("Arial", 30))
        self.c_free_label.place(x=20,y=510)
        self.app.mainloop()

    def check(self):
        pass

