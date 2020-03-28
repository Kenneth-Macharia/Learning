import io
from contextlib import redirect_stdout
from unittest import TestCase, main
from exercises.andela import (password_check, longer_string, switch_reverser, pig_latin,
                               check_question_marks)
from exercises.abs_learning_tasks import valid_chess_board


class UnitTests(TestCase):

    @staticmethod
    def longer_str_fetch_stdout(str1, str2):
        f = io.StringIO()

        with redirect_stdout(f):
            longer_string.longer_str_compare(str1, str2)
        capture = f.getvalue()

        return capture.strip()

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
        self.assertEqual(self.longer_str_fetch_stdout('', ''), '')
        self.assertEqual(self.longer_str_fetch_stdout(1, 'test'), '')
        self.assertEqual(self.longer_str_fetch_stdout('other', 2), '')
        self.assertEqual(self.longer_str_fetch_stdout('test', 'other'), 'other')
        self.assertEqual(self.longer_str_fetch_stdout('other', 'test'), 'other')
        self.assertEqual(self.longer_str_fetch_stdout(
            'test', 'that'), 'test that')

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

    def test_switch_reverser(self):
        self.assertEqual(switch_reverser.switcher(), None)
        self.assertEqual(switch_reverser.switcher([]), [])
        self.assertEqual(switch_reverser.switcher([1.1, 2]), [1.1, 2])
        self.assertEqual(switch_reverser.switcher(['!', 2]), ['!', 2])
        self.assertEqual(switch_reverser.switcher([2, 3, 1]), [1, 3, 2])
        self.assertEqual(switch_reverser.switcher([' ']), [' '])
        self.assertEqual(switch_reverser.switcher(['do', 3]), ['do', 3])
        self.assertEqual(switch_reverser.switcher(['d', 'o']), ['d', 'o'])
        self.assertEqual(switch_reverser.switcher(['do', 'that']), ['DO', 'THAT'])
        self.assertEqual(switch_reverser.switcher(['22', 'that']), ['22', 'that'])

    def test_pig_latin(self):
        self.assertEqual(pig_latin.pig_latin_converter(' '), '')
        self.assertEqual(pig_latin.pig_latin_converter('2will'), '')
        self.assertEqual(pig_latin.pig_latin_converter('!will'), '')
        self.assertEqual(pig_latin.pig_latin_converter('w$ill'), 'illw$ay')
        self.assertEqual(pig_latin.pig_latin_converter('will'), 'illway')
        self.assertEqual(pig_latin.pig_latin_converter('dog'), 'ogday')
        self.assertEqual(pig_latin.pig_latin_converter('category'), 'ategorycay')
        self.assertEqual(pig_latin.pig_latin_converter('chatter'), 'atterchay')
        self.assertEqual(pig_latin.pig_latin_converter('trash'), 'ashtray')
        self.assertEqual(pig_latin.pig_latin_converter('andela'), 'andelaway')
        self.assertEqual(pig_latin.pig_latin_converter('electrician'), 'electricianway')

    def test_q_mark_checker(self):
        self.assertEqual(check_question_marks.q_mark_checker(''), False)
        self.assertEqual(check_question_marks.q_mark_checker(
            'arrb6???4xxbl5???eee5'), True)
        self.assertEqual(check_question_marks.q_mark_checker(
            'acc?7??sss?3rr1??????5'), True)
        self.assertEqual(check_question_marks.q_mark_checker(
            '5??aaaaaaaaaaaaaaaaaaa?5?5'), False)
        self.assertEqual(check_question_marks.q_mark_checker(
            '9???1???9???1???9'), True)
        self.assertEqual(check_question_marks.q_mark_checker('aa6?9'), False)

if __name__ == '__main__':
    main()