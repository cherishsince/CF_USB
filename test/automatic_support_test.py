"""

测试

"""
from PIL import Image

from shoot import automatic_support

if __name__ == '__main__':
    img = Image.open('../img/JU_KAIJIN1.bmp')
    mirror_img = automatic_support.get_sniper_open_mirror_position_image(
        img, automatic_support.get_sniper_open_mirror_position())
    print(automatic_support.has_sniper_open_mirror(mirror_img))
    mirror_img.show()