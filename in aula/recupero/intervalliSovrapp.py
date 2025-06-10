def merge_interval(intervals:list[list]) -> list:

    if not intervals:
        return []
    
    if len(intervals) == 1:
        return intervals[:]
    
    