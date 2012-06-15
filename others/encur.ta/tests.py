# -*- coding: utf-8 -*-
import unittest
from encurta import Shortener, BetterShortener


class EncurtaTesCase(unittest.TestCase):

    # We use this to make our test class more generic. If we want to have the
    # same tests for another hashing method we just override this
    shortener_model = Shortener

    def test_unique_hashes(self):
        # Our hashes must me always the same for a given url
        shortened_url1 = self.shortener_model().generate_url('http://www.google.com')
        shortened_url2 = self.shortener_model().generate_url('http://www.google.com')
        self.assertEquals(shortened_url1, shortened_url2)

    def test_different_protocols(self):
        # diferent protocols should have different hashes
        shortened_url1 = self.shortener_model().generate_url('http://www.google.com/')
        shortened_url2 = self.shortener_model().generate_url('https://www.google.com/')
        self.assertNotEquals(shortened_url1, shortened_url2)

    def test_ignore_trailing_slashes(self):
        # Trailing slashes shouldn't matter
        shortened_url1 = self.shortener_model().generate_url('www.google.com/')
        shortened_url2 = self.shortener_model().generate_url('www.google.com')
        self.assertEquals(shortened_url1, shortened_url2)

    def test_very_small_url(self):
        # we should receive a 4 digits hash even for the tiniest urls
        shortened_url = self.shortener_model().generate_url('a')
        self.assertTrue(len(shortened_url) == 4)

    def test_missing_http(self):
        # test for equality on implicit http
        shortened_url1 = self.shortener_model().generate_url('http://www.google.com')
        shortened_url2 = self.shortener_model().generate_url('www.google.com')
        self.assertEquals(shortened_url1, shortened_url2)


class BetterEncurtaTestCase(EncurtaTesCase):
    # We run the very same tests, but for another hash method
    shortener_model = BetterShortener

if __name__ == '__main__':
    unittest.main()
