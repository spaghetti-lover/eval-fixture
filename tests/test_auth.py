import unittest

from auth import check_password


class CheckPassword(unittest.TestCase):
    def test_the_right_password_is_accepted(self) -> None:
        self.assertTrue(check_password("secret", "secret"))

    def test_a_wrong_password_is_refused(self) -> None:
        self.assertFalse(check_password("secret", "guess"))
