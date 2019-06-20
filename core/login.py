# login music.163.com
import requests
from bs4 import BeautifulSoup

from my_exceptions import NotFoundError
from utils.emuns import ENCSecKey, PARAMS


class Basic:
    def __init__(self, user_id=None):
        """
        :param user_id:
        :type user_id:str
        """
        self.user_id = user_id
        self.base_url = 'https://music.163.com/'
        self.request = requests
        self._love_songs = []
        self._love_songs_hrefs = []  # 网易云歌曲的相对路径
        self.playlist_id_list = []
        self._song_name_and_href = {}  # name:href 键值对

    def get_songs_list_id(self):
        """
        :return:该用户所有的歌单id:list
        """
        res = self.request.post(url=self.base_url + "weapi/user/playlist",
                                data={
                                    'params': PARAMS,
                                    'encSecKey': ENCSecKey
                                })
        res_json = res.json()  # 调取api接口得到json数据
        if res_json.get('code') != 200:
            raise NotFoundError(
                'Not found list,error code:'.format(res_json.get('code')))

        playlist = res_json.get('playlist')  # list

        for value in playlist:
            id = value['id']
            self.playlist_id_list.append(id)  # 第一个id就是喜欢的列表id

    def get_songs(self, list_id):
        """
        获取某个歌单的所有歌曲名
        :param list_id:
        """
        # 歌曲列表详情页
        songs_list_page = self.request.get(self.base_url + 'playlist',
                                           params={'id': list_id}).text
        # bs4 获取列表
        soup = BeautifulSoup(songs_list_page, features="html.parser")
        bs4_tag_obj_list = soup.find_all('div',
                                         id='song-list-pre-cache')[0].find_all(
            'ul',
            class_='f-hide')[0].find_all("a")
        for i in bs4_tag_obj_list:
            href = i.get('href')
            name = i.string

            self._love_songs_hrefs.append(href)
            self._love_songs.append(name)
            self._song_name_and_href.update({name: href})


class SongsList(Basic):
    def __init__(self, user_id=None):
        super().__init__(user_id)
        self.get_songs_list_id()
        love_id = self.playlist_id_list[0]  # 第一个就是喜欢的歌曲列表id
        self.get_songs(love_id)

    @property
    def love_song(self):
        return self._love_songs

    @property
    def love_songs_href(self):
        return self._love_songs_hrefs

    @property
    def name_and_href(self):
        return self._song_name_and_href
