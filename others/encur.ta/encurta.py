# -*- coding: utf-8 -*-
from __future__ import division
import hashlib  # used only for our 'better' shortener example


class Shortener(object):
    """
    Base shortener class. It uses a simple/dumb hash function.
    If we want a better hash function we can extend this one and just
    override the do_hex_hashing method.
    It's very important that the hashes always be the same for a given url, i.e.,
    they shouldn't be randomic. That way we can improve our speed for
    retrieving a url, and reduce our database entries.
    Usage:
        shortener = Shortener()

        shortened_url = shortener.generate_url(my_url)

    """
    VALID_CHARACTERS = 'a b c d e f g h i j k l m n o p q r s t u v x w y z '
    VALID_CHARACTERS += VALID_CHARACTERS.upper()
    VALID_CHARACTERS += '0 1 2 3 4 5 6 7 8 9'
    VALID_CHARACTERS = VALID_CHARACTERS.split()
    TOTAL_CHARS = len(VALID_CHARACTERS)
    # every number from 0 to 61 maps for a different digit
    char_mapper = {i: char_ for i, char_ in enumerate(VALID_CHARACTERS)}

    def do_hex_hashing(self, url):
        """
        Our simple hashing function.
        It just converts a string to a hexadecimal representation.
        """
        lst = []
        for ch in url:
            hv = hex(ord(ch)).replace('0x', '')
            if len(hv) == 1:
                hv += '0'
            lst.append(hv)
        return ''.join(lst)

    def _clean_url(self, url):
        """Cleans a given url from trailing slashes or prepends an implicit http"""
        if url.endswith('/'):
            url = url[:-1]
        if url.startswith('www.'):
            url = 'http://' + url
        return url

    def generate_url(self, url):
        """ Generates a shortened 4 digit hash. """
        url = self._clean_url(url)
        hex_hash = self.do_hex_hashing(url)

        # We use continuous divisions, retrieving the module for 62 on each
        # division and converting it to a char (from the char_mapper)
        int_hash = int(hex_hash, 16)
        shortened_url = ''
        for i in xrange(4):
            shortened_url += self.char_mapper[int_hash % self.TOTAL_CHARS]
            int_hash = int_hash // self.TOTAL_CHARS

        # save this hash to our DB for further retrieving
        self.persist_url(url, shortened_url)

        return shortened_url

    def persist_url(self, url, shortened_url):
        """
        Persist our shortened hash and the corresponding url for further
        retrieving. Since the hashes for a same url is always the same we
        wont save twice the same url on the database.
        This reduces our database size and
        enables a better performance (better indexing)
        """
        # some_function_that_saves_if_dont_exists_already(url, shortened_url)
        pass


class BetterShortener(Shortener):
    """
    A example of subclassing our shortener with a better hash algorithm.
    It uses a a 128 bits SHA from hashlib.
    """

    def do_hex_hashing(self, url):
        return hashlib.sha1(url).hexdigest()
