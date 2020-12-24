import unittest
from app import check_document_existance
from app import get_doc_owner_name
from app import get_doc_shelf
from app import add_new_shelf
from app import delete_doc
from unittest.mock import patch


class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_1(self):
        self.assertEqual(check_document_existance('11-2'), True)
        self.assertEqual(check_document_existance('2207 87623123'), False)

    def test_2(self):
        with patch('builtins.input', return_value='11-2'):
            self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')

    def test_3(self):
        with patch('builtins.input', return_value='11-2'):
            self.assertEqual(get_doc_shelf(), '1')

    def test_4(self):
        with patch('builtins.input', return_value='25'):
            self.assertEqual(add_new_shelf(), ('25', True))

    def test_5(self):
        with patch('builtins.input', return_value='1'):
            self.assertEqual(add_new_shelf(), ('1', False))

    def test_6(self):
        with patch('builtins.input', return_value='11-2'):
            self.assertEqual(delete_doc(), ('11-2', True))

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()


