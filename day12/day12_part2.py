
from tqdm import tqdm


cache = {}

def count(pattern, nums):
    if pattern == '':
        return nums == ()
    
    if nums == ():
        return '#' not in pattern
    
    result = 0 

    if (pattern, nums) in cache:
        return cache[(pattern,nums)]

    if pattern[0] in '?.':
        result += count(pattern[1:], nums)
    
    if pattern[0] in '?#':
        if len(pattern)>=nums[0] and '.' not in pattern[:nums[0]] and (len(pattern)==nums[0] or pattern[nums[0]] != '#'):
            result += count(pattern[nums[0]+1:], nums[1:])

    cache[(pattern,nums)] = result
    return result


total = 0
for line in tqdm(open("day12/input.txt")):
    pattern, nums = line.split()
    pattern = "?".join([pattern]*5)
    nums = tuple(map(int, nums.split(',')))*5

    total += count(pattern, nums)
print(total)