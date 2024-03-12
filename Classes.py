import pyautogui as pg
from psutil import *
class Resolution:
    def __init__(self) -> None:
        pass
    def get_resolution():        
        resolution = pg.size()  
        x = resolution.width
        y = resolution.height
        if x == 1366 and y == 768:
            return x , y
        else:
            real_x = 1366-x
            real_y = 768-y
            return real_x, real_y
class Hardware:
    def physical_cores(self) -> int:
        return cpu_count(logical=False)
    def total_cores(self):
        return cpu_count(logical=True)
    def cpu_frequency(self):
        self.cpu_freq = cpu_freq()
        self.freq_min = self.cpu_freq.min
        self.freq_max = self.cpu_freq.max
        return self.freq_min , self.freq_max
    def cpu_usage(self):
        self.usage = f"{cpu_percent(percpu=True, interval=1)[0]} %"
        return self.usage
        
    def main_partition_info(self):
        self.partitions = disk_partitions()
        self.c_drive = self.partitions[0].mountpoint
        self.partition_usage = disk_usage(self.c_drive)
        self.total = self.partition_usage.total
        self.used = self.partition_usage.used
        self.free = self.partition_usage.free
        return f"{self.total:,}" , f"{self.used:,}" , f"{self.free:,}"
    

