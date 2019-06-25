from unittest import TestCase

from core.download import DownloadHelperMulti, DownLoadUrl, DownLoadUrlAdvance


class TestDownLoadUrl(TestCase):
    def setUp(self):
        self.dlu = DownLoadUrl()

    def test_get_source_url(self):
        l = []
        a = self.dlu.get_source_url('/song?id=643982', l)
        self.assertTrue(l)
        print(l)

    def test_get_source_urls_multi(self):
        self.dlu.get_source_urls_multi(
            ['/song?id=662235', '/song?id=22808301', '/song?id=449818741',
             '/song?id=5410290', '/song?id=28828120', ])
        print(self.dlu.source_urls)
        self.assertTrue(self.dlu.source_urls)

    # def test


class TestDownLoadUrlAdvance(TestCase):
    def setUp(self):
        self.adv = DownLoadUrlAdvance(
            song_hrefs=['/song?id=662235', '/song?id=22808301',
                        '/song?id=449818741',
                        '/song?id=5410290', '/song?id=28828120', ])

    def test_source_urls_multi(self):
        print(self.adv.source_urls_multi)
        self.assertTrue(self.adv.source_urls_multi)
        self.assertTrue(isinstance(self.adv.source_urls_multi, list))


class TestDownLoadHelperMulti(TestCase):
    def setUp(self):
        self.dl = DownloadHelperMulti()

    def test_download(self):
        self.dl.download(name='test',
                         url='http://m10.music.126.net/20190624180140/f6ba7676'
                             '09a0b43f119cf4e3ed18dd36/ymusic/363b/72ef/7661/0b'
                             '373b6cdfc54e3022ef436c3ad58ec3.mp3')  # 此url很快就过期

    def test_download_muti(self):
        self.dl.download_multi()
