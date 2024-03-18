from Classes import Hardware
from tkinter import *
from tkinter import messagebox
from PIL import Image
import csv  

class hardware_process:
    def __init__(self):
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

    def view(self):

        self.app = Tk()
        self.app.geometry('750x600')
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

        self.physical_cores_value = Label(self.app , text=self.physical_cores, font=("Arial", 30), fg="green")
        self.physical_cores_value.place(x=300,y=20)
        self.total_cores_value = Label(self.app , text=self.total_cores, font=("Arial", 30), fg="green")
        self.total_cores_value.place(x=230,y=90)
        self.cpu_freq_min_value = Label(self.app , text=self.cpu_freq_min, font=("Arial", 30), fg="green")
        self.cpu_freq_min_value.place(x=300,y=160)
        self.cpu_freq_max_value = Label(self.app , text=self.cpu_freq_max, font=("Arial", 30), fg="green")
        self.cpu_freq_max_value.place(x=300,y=230)
        self.cpu_usage_value = Label(self.app , text=self.cpu_usage, font=("Arial", 30), fg="green")
        self.cpu_usage_value.place(x=230,y=300)
        self.c_total_value = Label(self.app , text=self.c_total, font=("Arial", 30), fg="green")
        self.c_total_value.place(x=400,y=370)
        self.c_used_value = Label(self.app , text=self.c_used, font=("Arial", 30), fg="green")
        self.c_used_value.place(x=400,y=440)
        self.c_free_value = Label(self.app , text=self.c_free, font=("Arial", 30), fg="green")
        self.c_free_value.place(x=400,y=510)
        self.app.mainloop()

    def check(self):
        
        if self.total_cores < 8:
            self.tc = "LOW"
        else:
            self.tc = "BEST"
        if int(self.cpu_freq_max) < 2801:
            self.cfm = "LOW"
        else:
            self.cfm = "BEST"
        if self.cfm == "LOW" and self.tc == "LOW":
            messagebox.showwarning("Hardware is Low", "Unfortunately, you do not have the necessary hardware to run this program. You may encounter a decrease in speed or an error while continuing to work. It is better to upgrade your hardware.")

        with open("csv_file\\Hardware.csv", "w+")as f:
            data = csv.writer(f)
            data1 = data.writerow(["TOTAL_CORES","CPU_FREQ_MAX"])
            data3 = [self.tc , self.cfm]
            data4 = data.writerows([data3])


