"""

    自动开枪的，公共部分，超类

"""
import environment
from util import image_util

"""

 判断是否 狙击开启
 
"""


def get_sniper_open_mirror_position():
    """
    狙击开镜 position
    :return:
    """
    win_w, win_h = environment.env.resolution
    # capture_image = environment.env.capture
    ju_w = 6
    ju_h = 2
    ju_x1 = (win_w / 2 - ju_w / 2) + 2
    ju_x2 = ju_x1 + ju_w - 1
    ju_y1 = (win_h / 2 - ju_h / 2) + 3
    ju_y2 = ju_y1 + ju_h
    return int(ju_x1), int(ju_y1), int(ju_x2), int(ju_y2)


def get_sniper_open_mirror_position_image(image, open_mirror_position):
    """
    获取 开镜图片
    :param image:
    :param open_mirror_position:
    :return:
    """
    # 狙击 image
    open_mirror_image = image.crop(open_mirror_position)
    return open_mirror_image


def has_sniper_open_mirror(image):
    """
    是否狙击开镜
    :param image:
    :return:
    """
    pix = image.load()
    # 开枪红色 1 0
    # 色值移动 5 0
    r, g, b = pix[1, 0]
    colors = [
        [[250, 255], [0, 5], [0, 5]]
    ]
    for colorRgb in colors:
        if (colorRgb[0][0] <= r <= colorRgb[0][1]
                and colorRgb[1][0] <= g <= colorRgb[1][1]
                and colorRgb[2][0] <= b <= colorRgb[2][1]):
            return True
    return False


"""

判断是否 红字

"""


def get_read_text_position():
    """
    获取红字的 position
    :return:
    """
    # 定义识别红字 box
    resolution_w, resolution_h = environment.env.resolution

    w = 30
    h = 20
    x1 = int(resolution_w / 2 - w / 2)
    y1 = int(resolution_h / 2 + 40)
    x2 = int(x1 + w)
    y2 = int(y1 + h)
    return x1, y1, x2, y2


def get_read_position_img(img, read_text_position):
    """
    获取 position 图片
    :param img:
    :param read_text_position:
    :return:
    """
    return img.crop(read_text_position)


def has_read_text(read_image):
    """
    是否 是红字
    :param read_image:
    :return:
    """
    colors = [
        [[150, 255], [0, 70], [0, 70]],
    ]
    max_count = 5
    has_find = image_util.find_color_count(read_image, colors, max_count)
    return has_find
