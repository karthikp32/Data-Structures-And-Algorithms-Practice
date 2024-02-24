import timeit
import statistics
from random import randint
from matplotlib import pyplot

def binsearch(nums, n):
    lo, hi = 0, len(nums)
    while hi > lo:
        mid = (lo + hi) // 2   # still in range [lo, hi)
        x = nums[mid]
        if x == n:
            return mid
        if n < x:
            hi = mid
        if n > x:
            lo = mid + 1
    return None

def linear_search_iterative(nums, n):
    for idx, val in enumerate(nums):
        if val == n:
            return idx
    return None



if __name__ == '__main__':
    # a = (0, 1, 3, 4)
    # b = (-5, -2, 0)
    # cases = (
    #     # find in any position, even size
    #     (a, 0, 0),
    #     (a, 1, 1),
    #     (a, 3, 2),
    #     (a, 4, 3),
    #     # find in any position, odd size
    #     (b, -5, 0),
    #     (b, -2, 1),
    #     (b, 0, 2),
    #     # fail to find
    #     (a, 2, None),
    #     (b, -3, None),
    # )
    sizes = range(200)
    binary_search_timings = []
    linear_search_timings = []
    for arrSize in sizes:
        nums = [randint(0,10000) for val in range(arrSize)]
        binary_search_timings.append(timeit.timeit(lambda: binsearch(nums, 23), number=3))
        linear_search_timings.append(timeit.timeit(lambda: linear_search_iterative(nums, 23), number=3))
    print("binary search took a median of " + str(statistics.median(binary_search_timings) * 1000000) + " microseconds")
    print("linear search took a median of " + str(statistics.median(linear_search_timings) * 1000000) + " microseconds")

    pyplot.plot(sizes, binary_search_timings, linear_search_timings)
    pyplot.savefig('comparing_binary_search_and_iterative_search_in_time_vs_num_of_items_in_list.png')
    #There is a dip in the time it takes to find 23 in a list of size 80 I think because it finds the 23 earlier in the list while searching with iterative search.
    pyplot.show()
