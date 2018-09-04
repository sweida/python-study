# 微信跳一跳

# 不要跟我说深度神经网络和图像模式识别啥的，虽然本人也会一丢丢，但是不想弄得跟上世纪90年代神经网络的泡沫化一样，解决跳一跳这个小游戏常规方法还是很多的。


# 这个辅助程序是半自动化的，先说说大致的工作原理和过程吧。

# 使用安卓模拟器运行微信跳一跳小游戏；
# Python脚本屏幕区域截图，获取棋子的中心区域位置图像，定义为目标图像
# 将目标图像按比例放大（屏幕越大，放大比例越大，计算精度越高）
# 为放大后的目标图像绘制GRID，作为参照系便于手动选点。同时鼠标移动时，绘制十字架，进一步便于选点。
# 玩家在放大后的目标图像区域，用鼠标分别选择棋子跳的起点和终点位置。位置处绘制黄色小圆圈，便于观察。
# 计算得到的起点和终点的几何距离，然后乘以相应的时间系数得到棋子的蓄力时间t，最后通过脚本向安卓模拟器位置发送鼠标press release事件，press和release时间间隔就是蓄力时间t。这里的时间系数是经验所得，自己试验几次就能得到准确值了。
# 关于效果，看下图。后面是在觉得无聊，不愿意点了 kill itself，不然根本不会死的。哪里不会点哪里~~基本操作如下：1）抓取屏幕，更新目标图像；2）选取棋子起点（可以是棋子的头或者底部）；3）选择终点，因为精度很高，所以后面终点就是直接选择小白点，每次得分都是32分。


# Python代码才120行，大家参考参考，还是很简单的，我贴一下吧。代码前几行是配置参数，实际使用大家配置一下，具体介绍几个：

# BBOX_TOP/LEFT/RIGHT/BOTTOM：指安卓模拟器中运行的跳一跳小游戏，相对于电脑屏幕的坐标，这个不用很精确，试几次就知道了
# IMG_RATIO：该参数是破解这个游戏的最大功臣了，可以将游戏区域放大以提高精度。该参数越大越好，最大是多少取决你的电脑屏幕， 我14寸的电脑只能配置成2.5了
# TIME_COE：这个是几何距离到实际蓄力时间的系数，跟IMG_RATIO相关，也是经验值，试几次微调下就好了。
# 具体运行起来的操作如下，按键'j'， 每个回合按三次（具体看下代码啦）
# 第一次按'j'，获取目标图像区域并放大，绘制GRID
# 第二次按'j'，同时鼠标移到放大后图像的棋子位置（最好是底部）。这时程序采样到起点的位置
# 第三次按'j'，同时鼠标移到放大后图像的目标位置（有小白点果断放在小白点上），这是程序采样终点位置，然后计算出起点和终点几何距离，并转换成蓄力时间，最后通过PyMouse去控制鼠标点击真正的跳一跳游戏区域。
# 代码设计到pythin tkinter和PyMouse，应该不难的。Python3按照PyMouse(PyUserInput)有点麻烦，自行百度哈。


import time
import datetime
import sys
import math
from PIL import Image, ImageTk
from PIL import ImageGrab
from pymouse import PyMouse
if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk
 
BBOX_LEFT = 30
BBOX_RIGHT = 360
BBOX_TOP = 200
BBOX_BOTTOM = 480
IMG_RATIO = 2.5   
BUTTON_ID = 1
GRID_SIZE = 20
MARK_SIZE = 20
POS_SIZE = 10
 
TIME_COE = 3.90/IMG_RATIO
 
 
class GUI(tk.Tk, object):
    def __init__(self):
        super(GUI, self).__init__()
        # self.grab_set_global()
        self.start_pos = [0, 0]
        self.end_pos = [0, 0]
        self.st = 0
        self.ms = PyMouse()
        self.c_mark_init = 0
        self._build_gui()
        self.bind('<KeyPress-j>', self._MyEvent)
        self.bind('<Motion>', self._MouseMotion)
 
    def _build_gui(self):
        self.title('Jumper Broker')
        w = int((BBOX_RIGHT - BBOX_LEFT)*IMG_RATIO)
        h = int((BBOX_BOTTOM - BBOX_TOP)*IMG_RATIO)
        self.geometry('{0}x{1}'.format(w,h))
        self.canvas = tk.Canvas(self, width = w, height = h)
        self.canvas.pack()
 
    
    def _grab_image(self):
        #grab and save the image
        img = ImageGrab.grab(bbox=(BBOX_LEFT,BBOX_TOP, BBOX_RIGHT, BBOX_BOTTOM))
        (w,h) = img.size
        w = int(w * IMG_RATIO)
        h = int(h * IMG_RATIO)
        img2 = img.resize((w, h), Image.ANTIALIAS)
        global g_tk_image
        g_tk_image = ImageTk.PhotoImage(img2)
        self.canvas.delete( 'all')
        self.canvas.create_image(w/2, h/2, image = g_tk_image)
        ##create some grids
        w_num = int(w/GRID_SIZE)
        h_num = int(h/GRID_SIZE)
        for i in range(w_num):
            self.canvas.create_line(i*GRID_SIZE, 0, i*GRID_SIZE, h)
        for j in range(h_num):
            self.canvas.create_line(0, j*GRID_SIZE, w, j*GRID_SIZE)
 
 
    def _Click(self):
        dx = self.end_pos[0] - self.start_pos[0]
        dy = self.end_pos[1] - self.start_pos[1]
        len = math.sqrt(dx * dx + dy * dy)
        t = len * TIME_COE
        print(dx, dy, t)
 
        self.ms.press(BBOX_LEFT, BBOX_TOP, BUTTON_ID)
        self.after(int(t), self._over)
    
    def _over(self):
        self.ms.release(BBOX_LEFT, BBOX_TOP,BUTTON_ID)
        self.focus_force()
 
    def _DrawPos(self):
        #draw the start position
        if self.st == 1:
            x = self.start_pos[0]
            y = self.start_pos[1]
        elif self.st == 2:
            x = self.end_pos[0]
            y = self.end_pos[1]
        self.canvas.create_oval(x-POS_SIZE, y-POS_SIZE, x+POS_SIZE, y+POS_SIZE, fill = 'yellow')
 
 
    def _MyEvent(self, event):
        #step 0, grab the picture
        if(self.st == 0):
            self._grab_image()
            self.st = 1
        #step 1, set set the first position
        elif(self.st == 1):
            self.start_pos = [event.x, event.y]
            self._DrawPos()
            self.st = 2
        elif(self.st == 2):
            self.end_pos = [event.x, event.y]
            self._DrawPos()
            self._Click()
            self.st = 0
    
    def _MouseMotion(self, event):
        x, y = event.x, event.y
        if self.c_mark_init == 1:
            self.canvas.delete(self.c_mark_h)
            self.canvas.delete(self.c_mark_v)
        self.c_mark_h = self.canvas.create_line(x - MARK_SIZE, y, x + MARK_SIZE, y, fill = 'red', width = 2)
        self.c_mark_v = self.canvas.create_line(x, y - MARK_SIZE, x, y + MARK_SIZE, fill = 'red', width = 2)
        self.c_mark_init = 1
 
if __name__ == "__main__":
    g_tk_image = None
    gui = GUI()
    gui.mainloop()
