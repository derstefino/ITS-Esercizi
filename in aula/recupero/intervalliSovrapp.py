def merge_interval(intervals:list[list[int]]) -> list:

    if not intervals:
        return []
    
    if len(intervals) == 1:
        return intervals[:]
    

    else:

        for interval in intervals:

            if interval[1] >= intervals[((intervals.index(interval) + 1) % len(intervals))][0] and interval[1] <= intervals[((intervals.index(interval) + 1) % len(intervals))][1]:
                interval[1] = intervals[((intervals.index(interval) + 1) % len(intervals))][1]
                intervals.remove(intervals[(intervals.index(interval) + 1)]) 
                
        
        return intervals
    




print(merge_interval([[1, 4], [4, 5]]))