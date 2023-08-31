def search_target_in_rotated_array(nums: list[int], target: int) -> int:
    n = len(nums) - 1
    left, right = 0, n

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[left] <= nums[mid]:
            
            if nums[left] <= target and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        else:

            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

print(search_target_in_rotated_array([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2))
