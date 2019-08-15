
# -*- coding: utf-8 -*-

from .context import ii

import os
import json
import unittest

class TestImgurInterface(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.SAMPLE_RISING_GALLERY_RESPONSE_FILENAME = os.path.abspath(
            os.path.join(os.path.dirname(__file__), 
                         'sample-data/rising-gallery.json')
            )

    def setUp(self):
        filename = TestImgurInterface.SAMPLE_RISING_GALLERY_RESPONSE_FILENAME
        with open(filename, 'r') as f:
            self.sample_rising_gallery_response = json.load(f)
        self.interface = ii.ImgurInterface()

    def test_image_is_gif(self):
        should_be_gif = self.sample_rising_gallery_response['data'][13]
        # line 1368 in rising-gallery.json
        # checking title just as a sanity check: is this the post we actually
        # want to test? 
        self.assertEqual(should_be_gif['title'], 'Hungry Squirrel')
        self.assertTrue(self.interface.image_is_gif(
                            should_be_gif['images'][0]))
        assert True

    def test_image_is_video(self):
        should_be_video = self.sample_rising_gallery_response['data'][22]
        # line 2373 in rising-gallery.json
        self.assertEqual(should_be_video['title'], 'Holy Shit')
        self.assertTrue(self.interface.image_is_gif(
                            should_be_video['images'][0]))
        assert True

    def test_filter_gifs(self):
        filtered = self.interface.filter_gifs_from_gallery_response(self.sample_rising_gallery_response)
        assert True


if __name__ == '__main__':
    unittest.main()