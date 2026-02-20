import allure
from unittest import TestCase, main
from Homework_lesson_7.lesson_7 import sum_numbers, average, reverse, longest_word


@allure.title ("Test sum of numbers")
class SumNumbersTest(TestCase):
    def test_sum_positive_numbers(self):
        """
        test if sum of positive numbers is equal 15
        """
        result = sum_numbers(5, 10)
        # self.assertEqual(15, result)
        assert 15 == result

    def test_sum_minus_numbers(self):
        """
        test if sum of negative numbers is equal -50
        """
        result = sum_numbers(-20, -30)
        # self.assertEqual(-50,result)
        assert -50 == result


    def test_sum_not_equal(self):
        """
        test if sum of numbers is not equal 5
        """
        result = sum_numbers(10, 15)
        # self.assertNotEqual(5, result)
        assert 5 != result

    def test_sum_negative(self):
        """
        test if sum of not int / float value will raise an error
        """
        result = sum_numbers('7', '3')
        self.assertEqual(10, result)


@allure.title ("Test average numbers")
class AverageNumbersTest(TestCase):

    def test_average_number_equal(self):
        """
        test if average number of list numbers is 20
        """
        result = average([10, 15, 35])
        # self.assertEqual(20, result)
        assert 20 == result

    def test_average_not_equal(self):
        """
        test if average number of list numbers is not 30
        """
        result = average([10, 15, 35])
        # self.assertNotEqual(30, result)
        assert 30 != result

    def test_average_in_list(self):
        """
        test if average number of list numbers is in another list
        """
        result = average([10, 15, 35])
        # self.assertIn(result, [100, 20, 50])
        assert result in [100, 20, 50]

    def test_average_negative(self):
        """
        test if not entering any data will raise an error
        """
        result = average([])
        self.assertEqual(10, result)

@allure.title ("Test opposite text string")
class OppositeTextStringTest(TestCase):

    def test_reversed_string_equal(self):
        """
        test if reversed word is equal to "olleh"
        """
        result = reverse('hello')
        # self.assertEqual('olleh', result)
        assert 'olleh' == result

    def test_reversed_string_not_equal(self):
        """
        test if reversed word is not equal to "hello"
        """
        result = reverse('hello')
        # self.assertNotEqual('hello', result)
        assert 'hello' != result

    def test_reversed_negative(self):
        """
        test if entering not a string value will raise an error
        """
        result = reverse(100)
        self.assertEqual('001', result)


@allure.title ("Test longest word")
class LongestWordTest(TestCase):
    def test_longest_word_equal(self):
        """
        test if the longest word is Kateryna
        """
        result = longest_word(['hello', 'Kateryna'])
        # self.assertEqual('Kateryna', result)
        assert 'Kateryna' == result

    def test_longest_word_not_equal(self):
        """
        test if the longest word is not hello
        """
        result = longest_word(['hello', 'Kateryna'])
        # self.assertNotEqual('hello', result)
        assert 'hello' != result

if __name__ == '__main__':
    main(verbosity=2)