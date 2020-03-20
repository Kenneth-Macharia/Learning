from unittest import TestCase, main
from exercises.andela import password_check, longer_string
from exercises.abs_learning_tasks import valid_chess_board


class UnitTests(TestCase):

    def test_password_check(self):
        self.assertEqual(password_check.password_checker('ABFETBJ'), '')
        self.assertEqual(password_check.password_checker('sftrew'), '')
        self.assertEqual(password_check.password_checker('2934567'), '')
        self.assertEqual(password_check.password_checker('aF1#t '), '')
        self.assertEqual(password_check.password_checker('*&%$@!^'), '')
        self.assertEqual(password_check.password_checker('2w3E*'), '')
        self.assertEqual(password_check.password_checker('ABd*234@1'), 'ABd*234@1')
        self.assertEqual(password_check.password_checker(
            'ABd*234@1,a F1#,2w3E*,2We3345!'),'ABd*234@1,2We3345!')

    def test_longer_string(self):
        self.assertEqual(longer_string.longer_str_compare('', ''), ['',''])
        self.assertEqual(longer_string.longer_str_compare(1, 'test'), [''])
        self.assertEqual(longer_string.longer_str_compare('other', 2), [''])
        self.assertEqual(longer_string.longer_str_compare('test', 'other'), ['other'])
        self.assertEqual(longer_string.longer_str_compare('that ', 'test'), ['that '])
        self.assertEqual(longer_string.longer_str_compare(
            'test', 'that'), ['test','that'])

    def test_is_valid_chess_board(self):
        self.assertEqual(valid_chess_board.is_valid_chess_board({'1h': 'w-King', \
            '6c': 'b-Queen', '2j': 'w-Bishop', '5h': 'b-Queen', '3e': 'w-King'}), False)
        self.assertEqual(valid_chess_board.is_valid_chess_board({'1h': 'w-King', \
            '6c': 'b-Queen', '2g': 'w-Bishop', '5h': 'b-Queen', '9e': 'w-King'}), False)
        self.assertEqual(valid_chess_board.is_valid_chess_board({'1h': 'w-King', \
            '6c': 'b-Queen', '2g': 'w-Bishop', '5h': 'b-Quen', '3e': 'w-King'}), False)
        self.assertEqual(valid_chess_board.is_valid_chess_board({'1h': 'w-King', \
            '6c': 'b-Queen', '2g': 'u-Bishop', '5h': 'b-Queen', '3e': 'w-King'}), False)
        self.assertEqual(valid_chess_board.is_valid_chess_board({'1h': 'King', \
            '6c': 'b-Queen', '2g': 'w-Bishop', '5h': 'b-Queen', '3e': 'w_King'}), False)
        self.assertEqual(valid_chess_board.is_valid_chess_board({'1h': 'w-King', \
            '6c': 'b-queen', '2g': 'w-Bishop', '5h': 'b-Queen', '3e': 'w-King'}), False)
        self.assertEqual(valid_chess_board.is_valid_chess_board({'1h': 'w-King', \
            '6c': 'b-Queen', '2g': 'w-Bishop', '5h': 'w-Queen', '3e': 'w-King'}), False)
        self.assertEqual(valid_chess_board.is_valid_chess_board({'1h': 'w-King', \
            '6c': 'b-Queen', '2g': 'b-Bishop', '5h': 'b-Queen', '3e': 'w-King'}), False)
        self.assertEqual(valid_chess_board.is_valid_chess_board({'1h': 'w-King', \
            '6c': 'b-Queen', '2g': 'w-Bishop', '5h': 'b-Queen', '3e': 'w-King'}), True)


if __name__ == '__main__':
    main()