# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]


# Solution one
def two_sum(nums, target):
    _index_value_dict = {}
    _list = []
    for inx, num in enumerate(nums):
        for item in _index_value_dict.items():
            if item[1] + num == target:
                _list.append(item[0])
                _list.append(inx)
                return _list
        _index_value_dict.update({inx: num})

# Solution two
def two_sum_number(nums, target):
    _data = {}
    for inx, num in enumerate(nums):
        complement = target - num
        if complement in _data:
            return [_data[complement], inx]
        _data[num] = inx

