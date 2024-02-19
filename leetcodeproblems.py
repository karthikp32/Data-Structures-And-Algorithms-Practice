class LeetcodeProblems:
    
    def insertNewInterval(self, intervals, newInterval):
        #Approach 1:
        # prevInterval = intervals[0]
        #Iterate through intervals
        #if newInterval[1] < currInterval[0] or currInterval[1] < newInterval[0]:
        #   if currInterval[0] <= prevInterval[1]
        #       set prevInterval[1] = Math.max(currInterval[1], prevInterval[1])       
        #       remove currInterval from intervals
        #else 
         #   set currInterval[1] = Math.max(newInterval[1],currInterval[1])
        # prevInterval = currInterval
        # prevInterval = intervals[0]
        #Iterate through intervals
        #   if currInterval[0] <= prevInterval[1]
        #       set prevInterval[1] = Math.max(currInterval[1], prevInterval[1])       
        #       remove currInterval from intervals
        #   else:
        #      prevInterval = currInterval
        # time: O(n)
        # space: O(1)
        result = []
        for currInterval in intervals:
            # curr interval's range is before new interval's range
            if currInterval[1] < newInterval[0]:
                result.append(currInterval)
            # curr interval's range is after new interval's range so we insert    
            elif currInterval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = currInterval
            # curr interval's range is overlapping with new interval's range so we update new interval to have combined range  
            elif currInterval[1] >= newInterval[0] or currInterval[0] <= newInterval[1]:
                newInterval[0] = min(currInterval[0], newInterval[0]) 
                newInterval[1] = max(newInterval[1], currInterval[1])

        result.append(newInterval)
        return result           



if __name__== '__main__':

    leetcodeProblems = LeetcodeProblems()

    intervals4 = [[1,5],[12,16]]
    newInterval4 = [6,10]
    expectedOutput4 = [[1,5],[6,10],[12,16]]
    actualOutput4 = leetcodeProblems.insertNewInterval(intervals4, newInterval4)
    print(actualOutput4)
    assert expectedOutput4 == actualOutput4, "failed test case 4"

    # [[1,2],[3,8],[8,10],[12,16]]
    intervals2 = [[1,2],[3,5],[6,7],[8,10],[12,16],[20,24]]
    newInterval2 = [4,8]
    expectedOutput2 = [[1,2],[3,10],[12,16],[20,24]]
    actualOutput2 = leetcodeProblems.insertNewInterval(intervals2, newInterval2)
    print(actualOutput2)
    assert expectedOutput2 == actualOutput2, "failed test case 2"
    

    intervals1 = [[1,3],[6,9]]
    newInterval1 = [2,5]
    expectedOutput1 = [[1,5],[6,9]]
    actualOutput1 = leetcodeProblems.insertNewInterval(intervals1, newInterval1)
    print(actualOutput1)
    assert expectedOutput1 == actualOutput1, "failed test case 1"
    
    intervals3 = [[1,5],[12,16]]
    newInterval3 = [2,4]
    expectedOutput3 = [[1,5],[12,16]]
    actualOutput3 = leetcodeProblems.insertNewInterval(intervals3, newInterval3)
    print(actualOutput3)
    assert expectedOutput3 == actualOutput3, "failed test case 3"

