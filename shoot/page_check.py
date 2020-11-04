"""

页面检查

"""
from PIL import Image

import environment
from util import image_util


def check_game_in_page(image):
    win_w, win_h = environment.env.resolution

    w = 100
    x1 = int(win_w / 2 - w / 2)
    x2 = int(x1 + w)
    y1 = 9
    y2 = 10

    colors = [
                # 134,50,22
                [[230, 255], [230, 255], [230, 255]]
             ]
    game_in_image = image.crop((x1, y1, x2, y2))
    find_res2 = image_util.find_color_count(game_in_image, colors, 10)
    if find_res2:
        return False

    find_res = image_util.find_color_count(game_in_image, colors, 2)
    # print('find_res {}'.format(find_res))
    # image_util.drawing_line(image, [[x1, x2, y1, y2]])
    # image.show()
    return find_res


def check_game_home(image):
    """
    见是否是游戏中页面
    :param image:
    :return:
    """
    configs = [
        (
            (2, 4, 250, 260),
            [
                # 134,50,22
                [[120, 140], [40, 60], [10, 40]]
            ],
            2
        ),
        (
            (2, 4, 450, 460),
            [
                # 170,62,14
                [[150, 200], [30, 90], [0, 40]]
            ],
            2
        ),
        (
            (2, 4, 650, 660),
            [
                # 119,47,14
                [[100, 140], [20, 70], [0, 50]]
            ],
            2
        ),
        (
            (1019, 1022, 550, 560),
            [
                # 139,59,14  140,62,14 137,57,15
                [[120, 160], [30, 90], [0, 100]]
            ],
            1
        )
    ]

    skip_error = 0
    max_skip_error = 4
    for config in configs:
        position, colors, max_count = config
        x1, x2, y1, y2 = position
        page_in_image = image.crop((x1, y1, x2, y2))
        find_res = image_util.find_color_count(page_in_image, colors, max_count)

        if not find_res:
            skip_error = skip_error + 1

        if skip_error >= max_skip_error:
            return True

        # print('find_res {}'.format(find_res))
        # image_util.position_line_drawing(image, position)

    # image.show()
    return False


if __name__ == '__main__':
    image2 = Image.open('../img/h1.bmp')
    check_game_in_page(image2)
