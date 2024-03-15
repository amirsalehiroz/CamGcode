from Classes import Hardware

def check():
    physical_cores = Hardware.physical_cores()
    total_cores = Hardware.total_cores()
    cpu_frequency = Hardware.cpu_frequency()
    cpu_freq_min = cpu_frequency[0]    
    cpu_freq_max = cpu_frequency[1]    
    cpu_usage = Hardware.cpu_usage()
    