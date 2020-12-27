import unittest
from unittest.mock import patch
import quine


@patch('quine.print')
class TestQuine(unittest.TestCase):
    @property
    def file_contents(self) -> str:
        with open('quine.py') as f:
            return ''.join(f.readlines())

    def test(self, mock_print):
        self.assertIsNone(quine.f())
        actual = self.file_contents
        self.assertEqual(actual[-1], '\n')
        mock_print.assert_called_once_with(actual[:-1])
