"""

配置环境
"""
from concurrent.futures import ThreadPoolExecutor
import logging

from util import image_util


def is_debug():
    """
    获取环境 配置
    :return:
    """
    return True
    # return False


class SystemContext:
    # 盒子驱动
    box_lib = None
    box_handle = None
    box_handle64 = None
    # 鼠标代理 1 按下状态 2 弹起状态  100 关闭
    mouse_left_state = 100
    # 自动开枪步枪 1 自动狙击 2 关闭为 100
    automatic_function = 100
    # 全局的截屏
    capture = None


"""
环境配置
"""


class env:
    # 日志级别
    logging_level = logging.INFO
    # usb 芯片是否默认端口启动
    usb_has_default = 1
    # 主线程
    executor = ThreadPoolExecutor(max_workers=8)
    # vid, pid
    usb_vid = 0xc230
    usb_pid = 0x6899
    # 分辨率
    resolution = 1025, 768
