def search_helper(nums, target, low, high):
    if(low == high):
        if(nums[low] == target):
            return low
        else:
            return -1
    
    if(abs(low - high) == 1):
        if(nums[low] == target):
            return low
        elif(nums[high] == target):
            return high
        else:
            return -1        
    
    
    mid = int((low + high)/2)
    
       
    if(target >= nums[mid]):
        return search_helper(nums, target, mid, high)
    else:
        return search_helper(nums, target, low, mid)
    

def search(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if(len(nums) == 0):
        return -1    
    
    low = 0
    high = len(nums)-1
    
    print(search_helper(nums, target, low, high))
    if(search_helper(nums, target, low, high) == -1):
        print("False")
    else:
        print("True")


search([1, 2, 3, 4, 5], 1)

        
    
            
            
        