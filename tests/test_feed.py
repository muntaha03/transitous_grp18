import unittest

def is_valid_url(url):
    return url.startswith("http://") or url.startswith("https://")

#tests
class TestTransitFeeds(unittest.TestCase):
    def test_valid_url_http(self):
        self.assertTrue(is_valid_url("http://google.com"))
        
    def test_valid_url_https(self):
        self.assertTrue(is_valid_url("https://transitous.org"))
        
    def test_invalid_url(self):
        self.assertFalse(is_valid_url("ftp://files.com"))

if __name__ == '__main__':
    unittest.main()