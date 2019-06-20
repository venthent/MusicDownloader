import threading

import requests

from core.login import SongsList


# 多线程下载
class DownloadHelperMulti:
    def __init__(self):
        song_list = SongsList()


# with open('test.mp3', 'wb') as f:
#     f.write(r.content)
# # # #
