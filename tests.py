import unittest
from unittest import TestCase

from func import get_users


class TestSolver(TestCase):
    def test_get_users(self):
        u_list = get_users()
        assert len(u_list) == 641

if __name__ == '__main__':
    unittest.main()
