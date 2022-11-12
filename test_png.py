'''
读取图片的坐标
'''
import cv2
import time
import win32gui, win32ui, win32con
import os

'''1、窗口截图'''
def window_capture(filename,w=1920,h=1080):
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    return True


g_rectangle = [0, 0, 0, 0] #设置初始值坐标
clicked = False
g_startPoint = [0, 0]
def startRoi(path):
    cv2.namedWindow("IMG_Show", 0)            # 创建画布
    cv2.resizeWindow("IMG_Show", 1920, 1080)  # 设置长和宽
    cv2.setMouseCallback("IMG_Show", onMouse) # 连接鼠标
    # 按"Esc"退出
    print("如果想要退出窗口，点击按钮 ESC,退出窗口...")
    while cv2.waitKey(30) != 27:             #监听事件
        global frame
        frame = cv2.imread(path,cv2.IMREAD_COLOR)  #读取图片数据
        # 画矩形
        '''
        由（x_min，x_max）组成，为绘制的边框的左上角；
        (g_rectangle[0], g_rectangle[1]), (g_rectangle[2], g_rectangle[3]):设置为绘制的边框的左上角和绘制的边框的右下角
        (0, 0, 255):指定边框的颜色，由（B,G,R）组成，当为（255,0，0）时为绿色，可以自由设定；
        1:线条的粗细值，为正值时代表线条的粗细（以像素为单位）
        '''
        cv2.rectangle(frame, (g_rectangle[0], g_rectangle[1]), (g_rectangle[2], g_rectangle[3]), (0, 0, 255), 2)
        cv2.imshow("IMG_Show", frame)
    # cv2.destroyWindow("IMG_Show")

'''
event:当前发生的鼠标事件类型
x和y:发生鼠标事件时鼠标在图像位置的x，y坐标
flags:  cv2_EVENT_FLAG_* (MouseEventFlags)类型的变量
param: 自定义的传递给 setMouseCallback 函数调用的参数
'''
# x和y： 发生鼠标事件时鼠标在图像位置的x，y坐标
def onMouse(event, x, y, flags, param):
    global clicked
    global g_rectangle
    global g_startPoint

    if event == cv2.EVENT_MOUSEMOVE:  # 滑动
        if clicked == True:
            #当鼠标点击时，打印一下信息
            g_rectangle[0] = g_startPoint[0]
            g_rectangle[1] = g_startPoint[1]
            #实时获取，对应变化后的x，y坐标
            g_rectangle[2] =  x
            g_rectangle[3] =  y
            print("坐标:%s" % g_rectangle)
    # 左键按下事件
    if event == cv2.EVENT_LBUTTONDOWN: # 左键点击
        #获取鼠标第一时间点击的坐标
        g_startPoint[0] = x
        g_startPoint[1] = y
        clicked = True
    # 左键弹起事件
    if event == cv2.EVENT_LBUTTONUP:   # 左键放开
        print("====================选中框的坐标：===========================")
        print("矩形框左上角坐标：")
        print(g_rectangle[0], g_rectangle[1])
        print("矩形框右下角坐标：")
        print(g_rectangle[2], g_rectangle[3])
        print("矩形框宽度：")
        print(g_rectangle[2]-g_rectangle[0])
        print("矩形框高度：")
        print(g_rectangle[3]-g_rectangle[1])
        clicked = False

if __name__ =="__main__":
    path = r"pi.png"
    if not os.path.isdir:
        os.mkdir(path)
    ret =  window_capture(filename=path)
    time.sleep(0.2)
    if ret == True:
        startRoi(path)
