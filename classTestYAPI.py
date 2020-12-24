import unittest
from yd_app import YaDisk


class YAPITest(unittest.TestCase):

    def setUp(self):
        self.token = ''
        self.folder = YaDisk(self.token)

    def test_1(self):
        self.assertEqual(self.folder.create_folder('new'), '201')

    def test_2(self):
        self.assertEqual(self.folder.search_folder('new'), '200')

    def test_3(self):
        self.assertEqual(self.folder.create_folder('new'), '409')

    def test_4(self):
        new_token = self.token + 'qwe'
        self.assertEqual(YaDisk(new_token).create_folder('new'), '401')

    def test_5(self):
        self.assertEqual(self.folder.search_folder('new123'), '404')
        self.folder.delete_folder('new')

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
