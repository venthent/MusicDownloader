from threading import Thread

import requests
from tornado import gen, httpclient, ioloop

from core.login import SongsList


# 从第三方网站获取歌曲的下载地址
class DownLoadUrl:
    def __init__(self, base_song_url=None):
        self.base_url = 'http://www.jbsou.cn/'  # 下载歌曲的第三方网站地址
        self.source_urls = []  # 歌曲资源的源地址
        if base_song_url is None:
            self.base_song_url = 'https://music.163.com/#'
        else:
            self.base_song_url = base_song_url

    def get_source_url(self, song_href, source_urls):
        """
        :param song_href: base_song_url+song_href构成参数post到第三方的接口
        :param source_urls :list
        :return: a music source url
        """
        response = requests.post(self.base_url,
                                 data={
                                     'input': self.base_song_url + song_href,
                                     'filter': 'url',
                                     'type': '_',
                                     'page': 1,
                                 },
                                 headers={
                                     'Origin': 'http://www.jbsou.cn',
                                     'X-Requested-With': 'XMLHttpRequest'
                                 }).json()
        if response.get('code') != 200:
            print('Post error')
        else:
            source_url = response.get('data')[0].get('url')
            title = response.get('data')[0].get('title')
            source_urls.append([title, source_url])

    def get_source_urls_multi(self, song_hrefs):
        """
        多线程获取歌曲的下载地址
        :param song_hrefs:list,etc.:['/song?id=619579']
        """
        threads = []
        for href in song_hrefs:
            t = Thread(target=self.get_source_url,
                       args=(href, self.source_urls))
            threads.append(t)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

    def get_source_url_async(self, song_hrefs):
        pass


class DownLoadUrlAdvance(DownLoadUrl):
    def __init__(self, song_hrefs, base_song_url=None):
        """
        :param song_hrefs:list
        :param base_song_url:
        """
        super().__init__(base_song_url)
        self.song_hrefs = song_hrefs

    @property
    def source_urls_multi(self):
        self.get_source_urls_multi(self.song_hrefs)
        print(self.source_urls)
        return self.source_urls

    # def


# 多线程下载


class DownloadHelperMulti:
    def __init__(self):
        self.songs = SongsList()
        self.songs_href = self.songs.love_songs_href  # list

    def download(self, name, url, path='/home/'):
        r = requests.get(url)  # requests object
        # TODO:if r.code!=200
        with open(path + name + '.' + url.split('.')[-1], 'wb') as f:
            f.write(r.content)

    def download_multi(self):
        download_url = DownLoadUrlAdvance(
            self.songs_href).source_urls_multi  # list,like:[[name,url]]
        threads = []
        for item in download_url:
            name = item[0]
            url = item[1]
            threads.append(Thread(target=self.download, args=(name, url,)))

        for t in threads:
            t.start()

        for t in threads:
            t.join()


