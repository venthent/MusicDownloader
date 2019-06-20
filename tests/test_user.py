from unittest import TestCase

from core.login import Basic, SongsList


class TestBasic(TestCase):

    def setUp(self):
        self.b = Basic('56510390')

    def test_get_song_list_id(self):
        self.b.get_songs_list_id()
        print(self.b.playlist_id_list)

    def test_get_songs(self):
        self.b.get_songs('55501219')
        print(self.b._love_songs)


class TestSongList(TestCase):
    def setUp(self):
        self.song = SongsList()

    def test_love_songs(self):
        print(self.song.love_song)

    def test_love_songs_href(self):
        self.assertTrue(self.song.love_songs_href)
        self.assertTrue(isinstance(self.song.love_songs_href, list))
        # print(self.song.love_songs_href)

    def test_name_and_href(self):
        self.assertTrue(self.song.name_and_href)
        self.assertTrue(isinstance(self.song.name_and_href,dict))
        # print(self.song.name_and_href)
