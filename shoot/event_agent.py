"""

事件代理

"""
import ctypes.wintypes
import time

from shoot import page_check


def mouse_left_agent(system_context):
    """
    事件代理 坐标左键代理到 M ,用于 CF 开枪
    :param system_context:
    :return:
    """
    while 1:

        try:
            # 检查是否是游戏页面
            capture_image = system_context.capture
            has_game_in = page_check.check_game_in_page(capture_image)
            if not has_game_in:
                time.sleep(0.03)
                continue

            # box 操作驱动
            lib, handle = system_context.box_lib, system_context.box_handle64

            # 0: 弹起状态；1:按下状态；-1: 失败
            key_state = lib.M_KeyState(handle, ctypes.c_uint64(16))
            mouse_left_state = system_context.mouse_left_state

            # print('key_state {} '.format(key_state))
            if mouse_left_state == 1 and key_state == 0:
                # 处罚 click 事件
                lib.M_KeyDown(handle, ctypes.c_uint64(16))

                # 瞬狙
                # if system_context.automatic_function == 2:
                #     system_context.mouse_left_state = 100
                # 右键开镜
                # lib.M_RightClick(handle)
                # time.sleep(0.1)
                # # 狙击自动开枪
                # lib.M_KeyPress(handle, 16, 1)
                # time.sleep(0.1)
                # # Q 切枪
                # lib.M_KeyPress(handle, ctypes.c_uint64(20), 1)
                # time.sleep(0.1)
                # lib.M_KeyPress(handle, ctypes.c_uint64(20), 1)
                # system_context.mouse_left_click = 100
                # continue

            elif mouse_left_state == 2:
                lib.M_KeyUp(handle, ctypes.c_uint64(16))
                system_context.mouse_left_state = 100

            # 休眠事件
            time.sleep(0.03)
        except Exception as e:
            print(e)