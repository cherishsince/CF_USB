"""

实时截屏

"""
import time

from util import image_util


def start(system_context):
    """
    开启 实时截屏
    :param system_context:
    :return:
    """
    while 1:
        try:
            # 获取截屏信息
            # now = time.time()
            # capture = image_util.capture((10, 10, 10, 10))
            capture = image_util.capture(None)
            system_context.capture = capture
            # 休眠
            # print(time.time() - now)
            time.sleep(0.03)
        except Exception as e:
            print(e)
