class FindDuplicatesInSequenceOfElements:


    #Finding Duplicates in Sequence Elements of Problem
    #Finding Duplicate Rows in Database Table is a more specific instance of that problem
    #in practice, you may have to look at your space complexity and figure out how much RAM/disk usage that would become
    def findDuplicates(self, nums):
        #Approach 1:
        #use a hashmap to keep track of num:count
        #res = []
        #map = {}
        #for num in  nums
        #if num in map
        #   map[num] += 1
        #else 
        #   map[num] = 1
        #for key in map
        #   if map[key] > 1
        #       res.append(map[key])
        #return res
        #time: O(n)
        #space: O(n) 

        #Approach 2:
        #iterate through nums
        #   add elements to set called found
        #   if curr_num in found
        #       result.append(curr_num)
        #time: O(n)
        #space: O(n)

        #Approach 3:
        # Given n == nums.length and 1 <= nums[i] <= n 
        # iterate through each idx, num in nums
        #   if abs(num) >= 0
        #       nums[abs(num)-1] *=  -1 #marking the value at index=num - 1 as negative means num was visited
        #   if num < 0:
        #       result.append(idx + 1)    
        res = []
        for idx, num in enumerate(nums):
            index = abs(num)-1 
            if nums[index] < 0:  
                res.append(abs(num))
            nums[index] *= -1     
        return res    


if __name__== '__main__':
    findDuplicatesInSequenceOfElements = FindDuplicatesInSequenceOfElements()

    nums1 = [4,3,2,7,8,2,3,1]
    expectedOutput1 = [2,3]
    actualOutput1 = findDuplicatesInSequenceOfElements.findDuplicates(nums1)
    print(actualOutput1)
    assert expectedOutput1 == actualOutput1, "failed test case 1 of findDuplicates"


    nums2 = [1,1,2]
    expectedOutput1 = [1]
    actualOutput1 = findDuplicatesInSequenceOfElements.findDuplicates(nums2)
    assert expectedOutput1 == actualOutput1, "failed test case 2 of findDuplicates"

    nums = [1]
    expectedOutput1 = []
    actualOutput1 = findDuplicatesInSequenceOfElements.findDuplicates(nums)
    assert expectedOutput1 == actualOutput1, "failed test case 3 of findDuplicates"

