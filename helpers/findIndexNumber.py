def findIndexNumber(array_to_find_index = []):
  #  O(1) -> Constant time
  left_sum = []
  right_sum = []
  result = -1
  
  array_length = len(array_to_find_index)
  left_sum.insert(0, array_to_find_index[0])

  #  O(n)
  for left_to_right in range(1, array_length, 1):
    sum_before = left_sum[left_to_right - 1] + array_to_find_index[left_to_right]
    left_sum.insert(left_to_right, sum_before)

  #  O(1) -> Constant time
  array_to_find_index.reverse()
  right_sum.insert(0, array_to_find_index[0])

  #  O(n)
  for right_to_left in range(1, array_length, 1):
    sum_after = right_sum[right_to_left - 1] + array_to_find_index[right_to_left]
    right_sum.insert(right_to_left, sum_after)

  right_sum.reverse() # Because i need to find the interception

  #  O(n)
  for left_to_right_full in range (1, array_length, 1):
    if left_sum[left_to_right_full] == right_sum[left_to_right_full]:
      result = left_to_right_full # This is the index found
      break

  return result

