#Wed Aug 5, 2026

def max_end3(nums):
  if nums[0] > nums[-1]:
    biggest = nums[0]
  else:
    biggest = nums[-1]
    
  return [biggest, biggest, biggest]

#
def middle_way(a, b):
  mid1 = a[1]
  mid2 = b[1]
  return [mid1, mid2]

#
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    sum = nums[0] + nums[1]
    return sum

#
def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

#
fruits = [apple, banana, cherry, dragonfruit]

for fruit in fruits:
  print fruit

#
def rotate_left3(nums):
  x = nums.pop(0)
  nums.append(x)
  return nums
