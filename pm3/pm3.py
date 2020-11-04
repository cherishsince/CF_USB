import os
import winsound

import resource


def play_open():
    path = resource.resource_path(os.path.join('pm3', 'snap1.ogg'))
    winsound.PlaySound(path, flags=1)


def play_close():
    path = resource.resource_path(os.path.join('pm3', 'snap2.ogg'))
    winsound.PlaySound(path, flags=1)


if __name__ == '__main__':
    play_open()
    # play_close()
