import pyautogui as pg

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
        
