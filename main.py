import os
import random
import time

from Dll.Reg import RegDm

dm = RegDm.Reg()


def 鼠标单击(x, y):
    a = dm.MoveTo(x + random.randint(1, 20), y + random.randint(1, 20)) == 1
    b = dm.LeftClick() == 1
    return a and b


def bmpfile_names(file_dir):
    fileNames = ""
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.bmp':
                fileNames = fileNames + file + "|"
    return fileNames[0:len(fileNames) - 1]


def 找图(图片名称):
    # 判断界面
    rst = dm.findpic(0, 0, 1920, 1080, 图片名称, '000000', 0.9, 0)
    print(rst)
    if rst != (-1, -1, -1):
        pass
    else:
        print("没有找到图片：" + 图片名称)
    print(rst)
    return rst


def 找图点击(图片名称):
    rs = dm.findpic(0, 0, 1920, 1080, 图片名称, '000000', 0.6, 0)
    if rs != (-1, -1, -1):
        鼠标单击(rs[0], rs[1])
        return
    else:
        print("没有找到图片：" + 图片名称)


def 随机延迟():
    time.sleep(random.randrange(1, 3, 1))


def 刷御魂(times):
    找图点击("主界面探索.bmp")
    随机延迟(1, 3)
    执行次数 = 0
    print("开始执行刷御魂：" + str(执行次数))
    while times > 执行次数:
        # 点击刷御魂按钮

        随机延迟(1, 3)
        执行次数 += 1


def 随机延迟(start, end):
    time.sleep(random.randrange(start, end, 1))

    #


if __name__ == '__main__':
    dm.setpath(os.path.split(os.path.realpath(__file__))[0] + "\\img")
    ret = dm.reg("xf30557fc317f617eead33dfc8de3bdd4ab9043", "xfqphyzoxouw700")  # 如果ret=1表示收费功能注册成功
    childHwd = dm.enumwindow(0, 'Phone-343747c7', 'Qt5151QWindowIcon', 1 + 2)
    print('游戏窗口句柄:%s' % childHwd, ret)
    dm.MoveWindow(int(childHwd), 0, 0)
    rdm_ret = dm.BindWindow(int(childHwd), "gdi", "dx.mouse.raw.input", "dx.mouse.raw.input", 0)
    if rdm_ret == 1:
        pass
    else:
        print("绑定失败")

    bmps = bmpfile_names(os.path.split(os.path.realpath(__file__))[0] + "\\img")
    # 鼠标单击(354, 131)
    # 鼠标单击(164,412)
    # 随机延迟(3, 5)d
    # 鼠标单击(150, 411)
    # 随机延迟(3, 5)
    # 鼠标单击(210, 227)
    # 获取前端传入的选项
    inputStr = '刷御魂'
    执行选项 = inputStr.split("|")
    print(执行选项)
    if "刷御魂" in 执行选项:
        刷御魂(22)
