import codewars_test as test
from sum_the_sum import sum_of_sums


@test.describe('Fixed tests')
def example_tests():
    @test.it('Example tests')
    def example_test_cases():
        test.assert_equals(sum_of_sums(3), 55)
        test.assert_equals(sum_of_sums(5), 630)
        test.assert_equals(sum_of_sums(100), 14740530850)