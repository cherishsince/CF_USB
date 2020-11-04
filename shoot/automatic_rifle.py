"""

自动步枪

"""
import ctypes
import random
import time

import app
from shoot import automatic_support
from shoot.page_check import check_game_in_page


def start(system_context):
    try:
        # 获取盒子 操作
        lib, handle = system_context.box_lib, system_context.box_handle64
        # 射击的 count
        shoot_count = 0
        max_shoot_count = 0
        while 1:
            # 停止功能
            if system_context.automatic_function != 1:
                time.sleep(0.5)
                continue

            # 是否手动开枪
            mouse_left_state = system_context.mouse_left_state
            # print('mouse_left_state {}'.format(mouse_left_state))
            if mouse_left_state == 1 or mouse_left_state == 2:
                shoot_count = 0
                random_sleep()
                continue

            # 抓屏 image
            capture_image = system_context.capture

            # 存在红字，准备杀敌
            has_read = automatic_support.has_read_text(
                automatic_support.get_read_position_img(
                    capture_image, automatic_support.get_read_text_position()))

            # 红字判断

            if not has_read:
                # 0: 弹起状态；1:按下状态；-1: 失败
                key_state = lib.M_KeyState(handle, ctypes.c_uint64(16))
                if key_state == 1:
                    lib.M_KeyUp(handle, ctypes.c_uint64(16))
                    # print('颜色小于 1 {}'.format(mouse_left_state))

                # 重置射击 count
                shoot_count = 0
                # 随机休眠
                random_sleep()
                continue

            # 连射次数
            # print('key_state {} shoot_count {}'.format(key_state, shoot_count))
            key_state = lib.M_KeyState(handle, ctypes.c_uint64(16))
            if key_state == 1:
                if shoot_count >= max_shoot_count:
                    lib.M_KeyUp(handle, ctypes.c_uint64(16))
                    shoot_count = 0
                    time.sleep(0.1)
                else:
                    shoot_count = shoot_count + 1
                    continue

            # 按下 M 不弹起
            key_state = lib.M_KeyState(handle, ctypes.c_uint64(16))
            if key_state == 0:
                lib.M_KeyDown(handle, ctypes.c_uint64(16))
                max_shoot_count = get_random_max_shoot_count()

            # 射击 count + 1
            shoot_count = shoot_count + 1
    except Exception as e:
        print(e)


def get_random_max_shoot_count():
    max_count = [500, 1000, 1500, 800, 1300]
    return max_count[random.randint(0, 4)]


def get_random_time():
    """
    获取随机事件
    :return:
    """
    # 调用 box 开枪 随机休眠 避免 36-2
    sleeps = [0.03, 0.03, 0.03, 0.03]
    # sleeps = [0.04, 0.04, 0.04, 0.04]
    return sleeps[random.randint(0, 3)]


def random_sleep():
    """
    随机休眠
    :return:
    """
    # 调用 box 开枪 随机休眠 避免 36-2
    time.sleep(get_random_time())
