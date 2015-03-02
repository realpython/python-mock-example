import mock
import unittest

from google import google_calc_addition


class TestGoogleCalc(unittest.TestCase):

    def test_google_calc_addition_without_mock(self):

        problem_one = google_calc_addition(1, 1)
        problem_two = google_calc_addition(1, 2)
        problem_three = google_calc_addition(1, 3)
        problem_four = google_calc_addition(1, 4)

        self.assertEqual(problem_one, '1 + 1 = 2')
        self.assertEqual(problem_two, '1 + 2 = 3')
        self.assertEqual(problem_three, '1 + 3 = 4')
        self.assertEqual(problem_four, '1 + 4 = 5')

    def test_google_calc_addition_with_mock(self):

        google_calc_addition_one = mock.Mock(return_value='1 + 1 = 2')
        google_calc_addition_two = mock.Mock(return_value='1 + 2 = 3')

        self.assertEqual(google_calc_addition_one(1, 1), '1 + 1 = 2')
        self.assertEqual(google_calc_addition_two(1, 2), '1 + 2 = 3')


if __name__ == '__main__':
    unittest.main()
