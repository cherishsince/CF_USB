"""

自动狙击

"""
import ctypes
import random
import time

from shoot import automatic_support


def start(system_context):
    # 获取盒子 操作
    lib, handle = system_context.box_lib, system_context.box_handle64
    while True:

        try:
            # 停止功能
            if system_context.automatic_function != 2:
                time.sleep(0.5)
                continue

            # 抓屏 image
            capture_image = system_context.capture

            # 是否开镜
            has_open_mirror = automatic_support.has_sniper_open_mirror(
                automatic_support.get_sniper_open_mirror_position_image(
                    capture_image, automatic_support.get_sniper_open_mirror_position()))

            # print('has_open_mirror {}'.format(has_open_mirror))
            if not has_open_mirror:
                time.sleep(0.03)
                continue

            # 存在红字，准备杀敌
            has_read = automatic_support.has_read_text(
                automatic_support.get_read_position_img(
                    capture_image, automatic_support.get_read_text_position()))

            if not has_read:
                # 休眠
                time.sleep(0.03)
                continue

            # 检查人物
            res = find_color(capture_image)
            if not res:
                # print('检查人物')
                time.sleep(0.03)
                continue

            # 狙击自动开枪
            lib.M_KeyPress(handle, 16, 1)
            time.sleep(0.1)
            # Q 切枪
            lib.M_KeyPress(handle, ctypes.c_uint64(20), 1)
            time.sleep(0.1)
            lib.M_KeyPress(handle, ctypes.c_uint64(20), 1)

            # 随休眠
            random_sleep()
        except Exception as e:
            print(e)


def find_color(img):
    try:
        win_w, win_h = 1024, 768
        ju_w = 4
        ju_h = 20
        ju_x1 = (win_w / 2 - ju_w / 2) + 2
        ju_x2 = ju_x1 + ju_w - 1
        ju_y1 = (win_h / 2 - ju_h / 2) + 1
        ju_y2 = ju_y1 + ju_h

        # 狙击 image
        juImg = img.crop((int(ju_x1), int(ju_y1), int(ju_x2), int(ju_y2)))
        # juImg.save('cccccc.png')
        # 检查红色
        colors = [
            # 新配置
            # 红色 255, 0, 0
            # [[200, 255], [0, 60], [0, 60]],
            [[200, 255], [0, 200], [0, 180]],
            # 蓝色 0,0,255
            [[10, 50], [10, 50], [0, 255]],
            # 黑色 17,17,17
            [[16, 70], [16, 70], [16, 70]],
            # 换色 177,114,1 - 203,166,99
            [[177, 203], [114, 166], [0, 99]],
            # 白色 177,186,188 - 250,251,241
            [[177, 255], [186, 255], [188, 255]],
        ]
        # 图片信息
        has_find, color_index = find_color_tools(juImg, colors, 1)
        if has_find:
            # 删除已找到的
            colors.pop(color_index)
            has_find, color_index = find_color_tools(juImg, colors, 1)

            if has_find:
                # 删除已找到的
                colors.pop(color_index)
                has_find, color_index = find_color_tools(juImg, colors, 1)
                return has_find
        # 没找到返回 False
        return False
    except Exception as e:
        print(e)


def find_color_tools(img, colors, max_count):
    # 图片信息
    width, height = img.size
    pixel = img.load()
    count = 0
    for j in range(0, height):  # 遍历所有宽度的点
        # 使用的是 np_img， x y 坐标相反
        x, y = 0, j
        rgb = pixel[x, y]
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        for i in range(len(colors)):
            color_rgb = colors[i]
            if (color_rgb[0][0] <= r <= color_rgb[0][1]
                    and color_rgb[1][0] <= g <= color_rgb[1][1]
                    and color_rgb[2][0] <= b <= color_rgb[2][1]):
                # 则这些像素点的颜色改成  其他色色值
                count = count + 1
                if count >= max_count:
                    return True, i

    return False, -1


def get_random_time():
    # 调用 box 开枪 随机休眠 避免 36-2
    sleeps = [0.01, 0.02, 0.03, 0.008]
    return sleeps[random.randint(0, 3)]


def random_sleep():
    # 调用 box 开枪 随机休眠 避免 36-2
    time.sleep(get_random_time())
