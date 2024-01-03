import unittest

from TwoSum.src.two_sum import two_sum


class TestTwoSum(unittest.TestCase):

    def test_two_sum_input_1(self):
        # Arrange
        inputs = [2, 7, 11, 15]
        # Act
        actual = two_sum(inputs, 9)
        # Assert
        assert actual == [0, 1]

    def test_two_sum_input_2(self):
        # Arrange
        inputs = [3, 2, 4]
        # Act
        actual = two_sum(inputs, 6)
        # Assert
        assert actual == [1, 2]

    def test_two_sum_input_3(self):
        # Arrange
        inputs = [3, 3]
        # Act
        actual = two_sum(inputs, 6)
        # Assert
        assert actual == [0, 1]
