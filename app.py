import logging

import PyHook3
import pythoncom

import environment
import resource
from drive import box_drive64
# 启动线程池
from pm3 import pm3
from shoot import automatic_sniper, automatic_rifle, real_time_capture, event_agent
from util import image_util

_executor = environment.env.executor
# 初始化系统上下文
_systemContext = environment.SystemContext()


def on_mouse_event(event):
    global _systemContext
    # print(event.Message)
    # 513 左键按下  514 左键弹起
    if event.Message == 513:
        # print('左键按下')
        _systemContext.mouse_left_state = 1
        return True
    elif event.Message == 514:
        # print('左键按下')
        _systemContext.mouse_left_state = 2
        return True
    return True


def on_keyboard_event(event):
    """
    键盘事件监听
    :param event:
    :return:
    """
    global _systemContext
    # print(event.KeyID)
    if event.KeyID == 117:
        # print('f7')
        logging.info('开启 - 自动步枪')
        _systemContext.automatic_function = 1
        # 提示音乐
        pm3.play_open()
    elif event.KeyID == 118:
        # print('f7')
        logging.info('开启 - 自动狙击')
        _systemContext.automatic_function = 2
        # 提示音乐
        pm3.play_open()
    elif event.KeyID == 35:
        # 退出功能
        _systemContext.automatic_function = 100
        # 提示音乐
        pm3.play_close()
    return True


def print_banner():
    """
    打印 banner
    :return:
    """
    print(' ')
    logging.info("加载成功...")
    logging.info("Tip: 游戏分辨率为 1024 * 768.")
    logging.info("==========================================================")
    logging.info("            欢迎使用 Box USB 驱动小精灵")
    logging.info("")
    logging.info("    F6自动[步枪]  F7自动[狙击]  End 关闭功能")
    logging.info("    [切换功能]先 End 关闭当前功能.")
    logging.info("==========================================================")


# 入口
if __name__ == '__main__':
    try:
        # 设置 logging 级别
        logging.basicConfig(level=environment.env.logging_level)

        # 加载 box 驱动文件
        drive_path = resource.resource_path('box64.dll')
        if environment.env.usb_has_default == 2:
            lib, handle = box_drive64.inmmit(drive_path, None, None)
        else:
            lib, handle = box_drive64.init(drive_path, environment.env.usb_vid, environment.env.usb_pid)

        # 设置 box 驱动
        _systemContext.box_lib = lib
        _systemContext.box_handle = handle
        _systemContext.box_handle64 = handle

        # 初始化 截屏
        _systemContext.capture = image_util.capture(None)

        # 打印 banner
        print_banner()

        # 开启自动狙击
        _executor.submit(event_agent.mouse_left_agent, _systemContext)
        # 开启自动狙击
        _executor.submit(real_time_capture.start, _systemContext)
        # 开启自动狙击
        _executor.submit(automatic_sniper.start, _systemContext)
        # 开启自动步枪
        _executor.submit(automatic_rifle.start, _systemContext)

        # 监听事件
        hm = PyHook3.HookManager()
        hm.KeyDown = on_keyboard_event
        hm.HookKeyboard()
        hm.MouseAll = on_mouse_event
        hm.HookMouse()
        pythoncom.PumpMessages()
    except Exception as e:
        print(e)
