class Interview:
    # Programming interview

# Here are a selection of tasks.

# Solving more tasks is naturally better, but solving a single harder task deeply is more impressive than making light progress on all the tasks.
# A better algorithmic design can be worth more than a full implementation of a mediocre algorithm.
# You can use external tools, but solving a problem on your own is more impressive than using GPT4/google.
# (some of these problems may have been selected specifically because GPT4 can not solve them outright)

# For each task, there are roughly three detail levels of solution:
# 1. rough algorithmic design in english
# 2. pseudo code solution
# 3. working code

# You will share your screen while working on the problem and some find it natural to explain/narrate as they code, but that is up to you.
# We will watch you work but not interrupt or comment until the end, unless requested.  For any problem you can ask for hints/help, and you can use external tools.
# You can use any language for problems that don't specify the language.
# When you are done reply to this email with your answers (attach any files as needed).



# ## Query System

# 3. Create a system which performs queries on an array of json structs/maps (a table), where both the query and the table are specified in json.
# Each query is composed of a logical conjunction (and) of any number of column/field subqueries, where each subquery is composed of a column name, an op which can be one of ">", ">=", "<", "<=", "==", and a value to compare against

#Query json:
# {"query": "...COLUMN2 > 4..."}
#Table json
# [{column1: ...}, {column2, ...}, {column3, ...}]    
    

#class Conjuction:
#   columnName
#   operator
#   value       
# findRowWhereConjunctionIsTrue(Conjunction)
# findRowWhereAllConjunctionsAreTrue(List<Conjunction> conjunctions....)    

# ## Prediction system

# 4. Create/design a real-time prediction system which predicts the probability a machine will have a downtime fault in the next minute, hour, or day (GPU error, internet disconnect, reboot, or disk error)
    
# Use Machine Learning to predict the probability a machine will have a downtime fault in the next minute, hour, or day (GPU error, internet disconnect, reboot, or disk error)
#   1) If you have really specific data where you have a data about how often a machine with a specific GPU has GPU errors, internet disconnects, reboots, or disk errors, you can train a machine learning model on that data
#   2) If you have more general data about machines with GPUs and how often they have GPU errors, internet disconnects, reboots, or disk errors, you can train a machine learning model on that data
#   3) If you have only have even more general data about machines with only CPUs, etc. and how often they have internet disconnects, reboots, or disk errors, you can train a machine learning model on that data
#   4) Weighted approach where you train your machine model on all three types of data and give different weights to the predictions related to the 3 approaches

# ## IAM Permissions

# 5. Create a function intersect_permissions which performs the intersection of two permission trees.  Each permission tree is a json object which defines the scope of allowed API calls, according to the following rules:
#  - a key mapping to an empty dict/set allows access to anything under that key
#  - a key mapping to a non empty dict/set allows access only to the defined children under that key
#  - the key name 'constraints' is special and defines constraints on parameters of a specific api call (leaf/bottom of the tree)

#  Examples:

# // an admin key, not very constrained
# rights0 = {"api": {"user_read": {}, "admin_read": {}, "user_write": {}, "admin_write": {}, "constraints": {}, "machine_read": {}, "instance_read": {}, "machine_write": {}, "instance_write": {}}}

# // more constrained user key
# rights2 = {"api": {"misc": {}, "user_read": {}, "instance_read": {}, "instance_write": {}}}

# // specific constrained key
# rights4 = {"api": {"instance_read": {"api.instance.request_logs": {"constraints": {"id": {"eq": 382834}}}}, "instance_write": {} } }

# intersect(rights0,rights2) = {"api": {"user_read": {}, "instance_read": {}, "instance_write": {}}}
# intersect(rights2,rights4) = {"api": {"instance_read": {"api.instance.request_logs": {"constraints": {"id": {"eq": 382834}}}}, "instance_write": {} } }


# extra: now add support for wildcard which allow access to any other children of a node:
# // constrains request_logs, but not other instance_read children
# rights5 = {"api": {"instance_read": {"api.instance.request_logs": {"constraints": {"id": {"eq": 382834}}}, "*":{}}, "instance_write": {} } }

# Problem 5 looks like a specific instance of problem 6

# ## Algorithms

# Parallel preferred

# 6. create a function to (parallel) compute the intersection of two sets
    # {0:1, 1:2, 2:4, 3:7, 4:8}
    # {0:1 }
# An idea could be to use a divide and conquer algorithm or something like what merge sort does where it keeps splitting the data into halves
    #how can I iterate through both in parallel? timing might off with multithreading
    #i wonder if you could come up with O(logN) algorithm where you keep halving the process
    #brute force would be iterate each elements of smaller set and check if it exists in larger set
    #if it does, add to result set
    #time: O(n) where n is len(min(setA, setB))
    #space: O(n) where n is len(min(setA, setB))

    def intersection(self, setA, setB):
        result = set()
        if len(setA) < len(setB):
            if setA:
                for element in setA:
                    if element in setB:
                        result.add(element)
        else:
            if setB:
                for element in setB:
                    if element in setA:
                        result.add(element)     
        return result                   

# 7. create a function to (parallel) compute the dot product of two large sparse vectors
    

    


# 1. write a data structure and functions which allows for storing a numeric time series and quickly querying the sum of a specific subrange
# (if you want you can assume the series is dense: that a value is defined for all times within the valid range t_min and t_now)
    

# 2. write a data structure and functions which allows for storing a numeric time series and quickly querying the max of a specific subrange

# ## Time Series

    
#Approach 1:
  #List timestamps
  #sum(int start, int end) 
  # sum  
  # for  time in range(start,end + 1)
  # val = time_series_map[time]
  #     sum += val
  # time: O(n)
  # space: O(m) where m = all timestamps       

    class TimeSeries:    
        timestampsMap = {}
        times = []

        def __init__(self, timestampsMap, times):
            self.timestampsMap = timestampsMap
            self.times = times

        def add_time_and_val_to_map(self, time, val):
            self.timestampsMap[time] = val

        def add_time_to_list(self, time):
            self.times.append[time]  

        def get_val_from_map(self, time):
            return self.timestampsMap[time]      


    def sum(self, start, end, timeSeries):
        sum = 0 
        for time in range(start,end + 1):
            if timeSeries.timestampsMap:
                val = timeSeries.get_val_from_map(time)
                sum += val
        return sum    
    
    
    def maxVal(self, start, end, timeSeries):
        maxValue = None
        if timeSeries.timestampsMap:
            maxValue =  timeSeries.get_val_from_map(start)
            for time in range(start,end + 1):                
                maxValue = max(maxValue, timeSeries.get_val_from_map(time))
        return maxValue 

if __name__== '__main__':
    


    interview = Interview()

    # Intersection  Algorithms ex.
# Ex. 1
# setA = {1,2,3,4}, setB =  {1,2}  
    
    # Ex. 2
# setA ={1,2} , setB = {1,2,3,4} 
    
# Ex. 3
# setA = {}, setB =  {1,2,3,4}   
    
    # Ex. 4
# setA ={}, setB = {}   
    set1A = {1,2,3,4}
    set1B = {1,2}  
    expectedInter1 = {1,2}
    actualInter1 = interview.intersection(set1A, set1B)
    assert expectedInter1 == actualInter1, "failed test case 1 of Intersection  Algorithms"

    # set2A = {1,2,3,4}
    # set2B = {1,2}  
    # expectedInter1 = {1,2}
    # actualInter1 = interview.intersection(set1A, set1B)
    # assert expectedInter1 == actualInter1, "failed test case 1 of Intersection  Algorithms"


    #Sum examples
#Ex. 1 
# Time Series
# Map    
# {0:1, 1:2, 2:4, 3:7, 4:8}
#input: sum(0, 3)
#output: 14   

#Ex. 2 
# Time Series
# Map    
# {0:1, }
#input: sum(0, 0)
#output: 1   

#Ex. 3 
# Time Series
# Map    
# {}
#input: sum(0, 0)
#output: 0   
    
  

    
    timestampsMap1 = {0:1, 1:2, 2:4, 3:7, 4:8}
    times1 = [0, 1, 2,3, 4]
    timeSeries1 = interview.TimeSeries(timestampsMap1, times1)
    expected1 = 14
    actual1 = interview.sum(0,3, timeSeries1)
    assert expected1 == actual1, "failed test case 1 of sum"

    timestampsMap2 = {0:1}
    times2 = [0]
    timeSeries2 = interview.TimeSeries(timestampsMap2, times2)
    expected2 = 1
    actual2 = interview.sum(0,0, timeSeries2)
    assert expected2 == actual2, "failed test case 2 of sum"


    timestampsMap3 = {}
    times3 = []
    timeSeries3 = interview.TimeSeries(timestampsMap3, times3)
    expected3 = 0
    actual3 = interview.sum(0,0, timeSeries3)
    assert expected3 == actual3, "failed test case 3 of sum"

    
#Max Examples
    #Ex. 1 
# Time Series
# Map    
# {0:1, 1:2, 2:4, 3:7, 4:8}
#input: max(0, 3, timeSeries1)
#output: 7   

    expectedMax1 = 7
    actualMax1 = interview.maxVal(0, 3, timeSeries1)
    assert expectedMax1 == actualMax1, "failed test case 1 of max"

    #Ex. 2 
# Time Series
# Map    
# {0:1, 1:1}
#input: max(0, 1, timeSeries2)
#output: 1   

    timestampsMap4 = {0:1,1:1}
    times4 = [0,1]
    timeSeries4 = interview.TimeSeries(timestampsMap4, times4)
    expectedMax2 = 1
    actualMax2 = interview.maxVal(0, 1, timeSeries4)
    assert expectedMax1 == actualMax1, "failed test case 2 of max"

    
#Ex. 3 
# Time Series
# Map    
# {}
#input: max(0, 0, timeSeries3)
#output: None 
    expectedMax3 = None
    actualMax3 = interview.maxVal(0,0, timeSeries3)
    assert expectedMax3 == actualMax3, "failed test case 3 of max"


