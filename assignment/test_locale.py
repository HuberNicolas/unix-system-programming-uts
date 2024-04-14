import unittest
from unittest.mock import patch, mock_open
import sys
from io import StringIO
import my_locale


class TestLocaleScript(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def tearDown(self):
        sys.stdout = self.held

    def test_empty_file_no_locales(self):
        test_args = ['locale.py', '-a', './data/empty_argument_file.csv']
        with patch('builtins.open', mock_open(read_data=''), create=True):
            with patch('sys.argv', test_args):
                my_locale.main()
                self.assertEqual(sys.stdout.getvalue(), "No locales available\n")

    def test_empty_file_no_charmaps(self):
        test_args = ['locale.py', '-m', './data/empty_argument_file.csv']
        with patch('builtins.open', mock_open(read_data=''), create=True):
            with patch('sys.argv', test_args):
                my_locale.main()
                self.assertEqual(sys.stdout.getvalue(), "No charmaps available\n")

    def test_language_not_present(self):
        test_args = ['locale.py', '-l', 'German', './data/language_specific_argument_file.csv']
        file_content = 'locale,English,en_US\ncharmap,English,ISO-8859-1'
        with patch('builtins.open', mock_open(read_data=file_content), create=True):
            with patch('sys.argv', test_args):
                my_locale.main()
                self.assertEqual(sys.stdout.getvalue(), "No locales and charmaps in this language\n")

    def test_version_info_with_file_exist(self):
        test_args = ['locale.py', '-v', './data/full_argument_file.csv']
        with patch('os.path.isfile', return_value=True):
            with patch('sys.argv', test_args):
                my_locale.main()
                self.assertIn(
                'Nicolas Huber\n'
                        '25061944\n'
                        'Friday 17 May 2024', sys.stdout.getvalue())

    def test_invalid_option(self):
        test_args = ['locale.py', '-z', './data/full_argument_file.csv']
        with patch('sys.argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                my_locale.main()
            self.assertIn('Error: Invalid option -z', sys.stdout.getvalue())

    def test_file_not_found(self):
        test_args = ['locale.py', '-a', './data/non_existent_file.csv']
        with patch('sys.argv', test_args):
            with self.assertRaises(SystemExit) as cm:
                my_locale.main()
            self.assertIn('Error: The file ./data/non_existent_file.csv does not exist or is not readable.',
                          sys.stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
