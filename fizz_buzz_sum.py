class FizzBuzzSum:

    #Problem: Fizz Buzz Sum

    #How many times does a multiple of 3 or 5 appear from 0 to N?
    #Approach 1:
    #Find how many times a multiple of 3 appears from 0 to N by dividing N/3
    #Use sum of first N natural numbers formula on the multiples_of_3 to find sum_of_multiples_of_3
    #threeSum = 3 * sum_of_multiples_of_3
    #Find how many times a multiple of 5 appears from 0 to N by dividing N/5
    #Use sum of first N natural numbers formula on the multiples_of_5 to find sum_of_multiples_of_5
    #fiveSum = 5 * sum_of_multiples_of_5
    #Find how many times a multiple of 3 overlaps with a multiple of 5
    #   Find how many times a multiple of 15 appears from 0 to N by dividing N/15
    #   Use sum of first N natural numbers formula on the multiples_of_15 to find sum_of_multiples_of_15
    #fifteen_sum = 15 * sum_of_multiples_of_15
    #return threeSum + fiveSum - fifteen_sum 
    #time: O(1)
    #space: O(1)

    def sum_of_first_n_natural_numbers(self, n):
        return n * (n + 1) / 2;

    def fizz_buzz_sum(self, n):
        multiples_of_3 = n // 3
        sum_of_multiples_of_3 = self.sum_of_first_n_natural_numbers(multiples_of_3)
        three_sum = 3 * sum_of_multiples_of_3

        multiples_of_5 = n // 5
        sum_of_multiples_of_5 = self.sum_of_first_n_natural_numbers(multiples_of_5)
        five_sum = 5 * sum_of_multiples_of_5

        multiples_of_15 = n // 15
        sum_of_multiples_of_15 = self.sum_of_first_n_natural_numbers(multiples_of_15)
        fifteen_sum = 15 * sum_of_multiples_of_15

        return three_sum + five_sum - fifteen_sum
    
if __name__== '__main__':   

    fizzBuzzSum = FizzBuzzSum()
    #Ex. 1
    #Input: n = 15
    #Output: 3 + 6 + 9 + 12 + 15 + 5 + 10 = 3(1 + 2 + 3 + 4 + 5) + 5(1 + 2) = 3(15) + 5(3) = 60 
    n1 = 15 
    expected1 = 60
    actual1 = fizzBuzzSum.fizz_buzz_sum(n1)
    assert expected1 == actual1, "failed test case 1 of fizz_buzz_sum"
    #Ex. 2
    #Input: n = 2
    #Output: 0
    n1 = 2
    expected1 = 0
    actual1 = fizzBuzzSum.fizz_buzz_sum(n1)
    assert expected1 == actual1, "failed test case 2 of fizz_buzz_sum"
    #Ex. 3
    #Input: n = 0
    #Output: 0
    n1 = 0
    expected1 = 0
    actual1 = fizzBuzzSum.fizz_buzz_sum(n1)
    assert expected1 == actual1, "failed test case 3 of fizz_buzz_sum"
    #Ex. 4
    #Input: n = 3
    #Output: 3
    n1 = 3
    expected1 = 3
    actual1 = fizzBuzzSum.fizz_buzz_sum(n1)
    assert expected1 == actual1, "failed test case 4 of fizz_buzz_sum"
    #Ex. 5
    #Input: n = 5
    #Output: 3(1) + 5(1) = 8
    n1 = 5
    expected1 = 8
    actual1 = fizzBuzzSum.fizz_buzz_sum(n1)
    assert expected1 == actual1, "failed test case 5 of fizz_buzz_sum"
       #Ex. 6
    #Input: n = 17
    #Output: 3 + 6 + 9 + 12 + 15 + 5 + 10 = 3(1 + 2 + 3 + 4 + 5) + 5(1 + 2) = 3(15) + 5(3) = 60 
    n1 = 17
    expected1 = 60
    actual1 = fizzBuzzSum.fizz_buzz_sum(n1)
    assert expected1 == actual1, "failed test case 6 of fizz_buzz_sum"

