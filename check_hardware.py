from Classes import Hardware
from tkinter import *
from PIL import Image

def check():

    hardware = Hardware()
    physical_cores = hardware.physical_cores()
    total_cores = hardware.total_cores()
    cpu_frequency = hardware.cpu_frequency()
    cpu_freq_min = cpu_frequency[0]    
    cpu_freq_max = cpu_frequency[1]    
    cpu_usage = hardware.cpu_usage()
    main_partition_info = hardware.main_partition_info()
    c_total = main_partition_info[0]
    c_used = main_partition_info[1]
    c_free = main_partition_info[2]

    app = Tk()
    app.geometry('600x600')
    app.title("Hardware Info")
    app.resizable(0 , 0)
    physical_cores_label = Label(app , text="physical cores :", font=("Arial", 30))
    physical_cores_label.place(x=20,y=20)
    total_cores_label = Label(app , text="total cores :", font=("Arial", 30))
    total_cores_label.place(x=20,y=90)
    cpu_freq_min_label = Label(app , text="cpu_freq_min :", font=("Arial", 30))
    cpu_freq_min_label.place(x=20,y=160)
    cpu_freq_max_label = Label(app , text="cpu_freq_max :", font=("Arial", 30))
    cpu_freq_max_label.place(x=20,y=230)
    cpu_usage_label = Label(app , text="cpu usage :", font=("Arial", 30))
    cpu_usage_label.place(x=20,y=300)
    c_total_label = Label(app , text="c drive total storage :", font=("Arial", 30))
    c_total_label.place(x=20,y=370)
    c_used_label = Label(app , text="c drive used storage :", font=("Arial", 30))
    c_used_label.place(x=20,y=440)
    c_free_label = Label(app , text="c drive free storage :", font=("Arial", 30))
    c_free_label.place(x=20,y=510)



    app.mainloop()


check()