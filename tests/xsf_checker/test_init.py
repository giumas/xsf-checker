import unittest


class TestXsfCheckerInit(unittest.TestCase):

    def test_has_version(self):
        from xsf_checker import __version__
        self.assertIsNot(len(__version__), 0)

    def test_is_version_more_than_1(self):
        from xsf_checker import __version__
        self.assertGreaterEqual(int(__version__.split('.')[0]), 1)

    def test_has_author(self):
        from xsf_checker import __author__
        self.assertIsNot(len(__author__), 0)

    def test_has_multiple_authors(self):
        from xsf_checker import __author__
        self.assertGreater(len(__author__.split(';')), 0)

    def test_has_license(self):
        from xsf_checker import __license__
        self.assertIsNot(len(__license__), 0)

    def test_has_apache_in_license(self):
        from xsf_checker import __license__
        self.assertTrue("apache" in __license__.lower())


def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.TestLoader().loadTestsFromTestCase(TestXsfCheckerInit))
    return s
